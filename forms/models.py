from django.db import models
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    episodeth = models.CharField(max_length=4, null=True)
    videolinkth = models.CharField(max_length=100, null=True)
    episoderaw = models.CharField(max_length=4, null=True)
    videolinkraw = models.CharField(max_length=100, null=True)
    episodeen = models.CharField(max_length=4, null=True)
    videolinken = models.CharField(max_length=100, null=True)
    desc = models.TextField()
    image = CloudinaryField('image', null=True)
    pub_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name="anime", on_delete=models.CASCADE, null=True)
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name_plural = "anime"

    def __str__(self):
        return str(self.title)

    def is_published(self):
        now = timezone.now()
        if now >= self.pub_date:
            return True
        return False


class Catagory(models.Model):
    tags = TaggableManager(blank=True)

class FriendList(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    tel = models.CharField(max_length=10)
    social = models.CharField(max_length=200)
    message = models.CharField(max_length=10000)
    picture = CloudinaryField('picture', null=True)
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "friend"

    def __str__(self):
        return self.name

    def is_published(self):
        now = timezone.now()
        if now >= self.pub_date:
            return True
        return False

    
class Friendzone(models.Model):
    nick = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    tel = models.CharField(max_length=10)
    social = models.CharField(max_length=200)
    message = models.CharField(max_length=10000)
    picture = CloudinaryField('picture', null=True)
    message2 = models.CharField(max_length=10000, null=True)
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "friendzone"

    def __str__(self):
        return self.nick

    def is_published(self):
        now = timezone.now()
        if now >= self.pub_date:
            return True
        return False