from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView, TemplateView, View
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404


# Create your views here.

class HelloView(ListView):
    model = Post
    template_name = 'main/index.html'
    ordering = ['-pub_date']
    context_object_name = 'posts'
    paginate_by = 20

@staff_member_required(login_url='login')
def admin(request):
    return render(request, 'admin/adminme.html')


class AdminPost(ListView):
    model = Post
    template_name = 'admin/adminpost.html'
    ordering = ['-pub_date']
    context_object_name = 'posts'
    paginate_by = 8

def post(request, pk):
    return render(request, 'main/post.html', {'post': Post.objects.get(pk=pk)})

def watch(request, id):
    return render(request, 'main/video.html', {'post': Post.objects.get(id=id)})

@staff_member_required(login_url='login')
def admin_delete_post(request, pk):
    Post.objects.get(pk=pk).delete()
    return redirect('adminpost')


class AdminAddPostForm(TemplateView):
    template_name = 'admin/adminaddpostform.html'


@staff_member_required(login_url='login')
def admin_add_post(request):
    Post(title=request.POST.get('title'), desc=request.POST.get('desc'), image=request.FILES.get('image'), episode=request.POST.get('episode'), videolink=request.POST.get('videolink')).save()
    return redirect('adminpost')


@staff_member_required(login_url='login')
def admin_edit_post_form(request, pk):
    return render(request, 'admin/admineditpostform.html', {'post': Post.objects.get(pk=pk)})


@staff_member_required(login_url='login')
def admin_edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.title = request.POST.get('title')
    post.desc = request.POST.get('desc')
    if request.FILES.get('image') is not None:
        post.image = request.FILES.get('image')
    post.save()
    return redirect('adminpost')



def register(request):
    return render(request, 'main/register.html', )


def login(request):
    return render(request, 'main/base.html', )


def addUser(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request, 'UserName Already Use')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Use')
            return redirect('/register')
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname,
            )
            user.save()
        return render(request, 'main/result.html')
    else:
        messages.info(request, 'Password Not Correct')
        return redirect('/register')


def loginsuccess(request):
    username = request.POST['username']
    password = request.POST['password']

    # login
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        messages.info(request, 'No Data in System')
        return redirect('/login')


def logout(request):
    auth.logout(request)
    return redirect('/')

def test(request):
    return render(request, 'error/404.html')
