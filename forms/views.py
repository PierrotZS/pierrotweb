from django.shortcuts import render, redirect
from .models import Post, Catagory , FriendList
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

class Friend(ListView):
    model = FriendList
    template_name = 'friend/friend.html'
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


def watchth(request, id):
    return render(request, 'main/videoth.html', {'post': Post.objects.get(id=id)})


def watchraw(request, id):
    return render(request, 'main/videoraw.html', {'post': Post.objects.get(id=id)})


def watchen(request, id):
    return render(request, 'main/videoen.html', {'post': Post.objects.get(id=id)})


def watchtest(request):
    return render(request, 'main/testvideo.php')


@staff_member_required(login_url='login')
def admin_delete_post(request, pk):
    Post.objects.get(pk=pk).delete()
    return redirect('adminpost')


class AdminAddPostForm(TemplateView):
    template_name = 'admin/adminaddpostform.html'


@staff_member_required(login_url='login')
def admin_add_post(request):
    Post(title=request.POST.get('title'),
         desc=request.POST.get('desc'),
         episodeth=request.POST.get('episodeth'),
         videolinkth=request.POST.get('videolinkth'),
         episoderaw=request.POST.get('episoderaw'),
         videolinkraw=request.POST.get('videolinkraw'),
         episodeen=request.POST.get('episodeen'),
         videolinken=request.POST.get('videolinken'),
         image=request.FILES.get('image')).save()
    return redirect('adminpost')


@staff_member_required(login_url='login')
def admin_edit_post_form(request, pk):
    return render(request, 'admin/admineditpostform.html', {'post': Post.objects.get(pk=pk)})


@staff_member_required(login_url='login')
def admin_edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.title = request.POST.get('title')
    post.desc = request.POST.get('desc')
    post.episodeth = request.POST.get('episodeth')
    post.videolinkth = request.POST.get('videolinkth')
    post.episoderaw = request.POST.get('episoderaw')
    post.videolinkraw = request.POST.get('videolinkraw')
    post.episodeen = request.POST.get('episodeen')
    post.videolinken = request.POST.get('videolinken')
    if request.FILES.get('image') is not None:
        post.image = request.FILES.get('image')
    post.save()
    return redirect('adminpost')


class AdminCatagory(ListView):
    model = Catagory
    template_name = 'admin/admincatagorylist.html'
    context_object_name = 'posts'
    paginate_by = 8


def admin_add_catagory(request):
    catagory(tags=request.POST.get('tags')).save()
    return redirect('admincatagory')


def register(request):
    return render(request, 'main/register.html', )


def login(request):
    return render(request, 'main/login.html', )


def addUser(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request, 'ผู้ใช้นี้มีคนใช้แล้ว')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'อีเมลนี้ใช้งานแล้ว')
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
        messages.info(request, 'ไม่พบผู้ใช้นี้หรือรหัสผ่านไม่ถูกต้อง')
        return redirect('/login')


def logout(request):
    auth.logout(request)
    return redirect('/')


def test(request):
    return render(request, 'error/404.html')

def AddFriend(request):
    return render(request, 'friend/mainfriend.html')


def addfriendform(request):
    f = FriendList()
    f.name = request.POST.get('name')
    f.email = request.POST.get('email')
    f.tel = request.POST.get('tel')
    f.social = request.POST.get('social')
    f.message = request.POST.get('message')
    f.image = request.FILES.get('image')
    f.save()
    return redirect('freindship')

