"""pierrotwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from forms import views
from pierrotwebsite import settings

urlpatterns = [
                  path('admindjango', admin.site.urls),
                  path('', views.HelloView.as_view(), name='home'),
                  path('anime/<int:pk>', views.post, name='post'),
                  path('watch/<int:id>/th', views.watchth, name='watchth'),
                  path('watch/<int:id>/raw', views.watchraw, name='watchraw'),
                  path('watch/<int:id>/en', views.watchen, name='watchen'),
                  path('watchtest', views.watchtest, name='watchtest'),
                  path('register', views.register, name='register'),
                  path('friendship', views.Friend.as_view(), name='freindship'),
                  path('addfriendship', views.AddFriend, name='addfreindship'),
                  path('addfriendshipform', views.addfriendform, name='addfriendshipform'),
                  path('addfriendshipsuccess', views.fsuccess, name='addfriendshipsuccess'),
                  path('register_success', views.addUser),
                  path('test', views.test, name='test'),
                  path('testadd', views.test, name='testadd'),
                  path('login', views.login, name='login'),
                  path('login_success', views.loginsuccess),
                  path('logout', views.logout, name='logout'),
                  path('admin', views.admin, name='admin'),
                  path('adminpost', views.AdminPost.as_view(), name='adminpost'),
                  path('adminaddpostform', views.AdminAddPostForm.as_view(), name='adminaddpostform'),
                  path('adminaddpost', views.admin_add_post, name='adminaddpost'),
                  path('admincatagory', views.AdminCatagory.as_view(), name='admincatagory'),
                  path('adminaddcatagory', views.admin_add_catagory, name='adminaddcatagory'),
                  path('admineditpostform/<int:pk>', views.admin_edit_post_form, name='admineditpostform'),
                  path('admineditpost/<int:pk>', views.admin_edit_post, name='admineditpost'),
                  path('admindeletepost/<int:pk>', views.admin_delete_post, name='admindeletepost'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
