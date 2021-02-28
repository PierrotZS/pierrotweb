from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.utils import timezone
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    episode = models.CharField(max_length=4, null=True)
    videolink = models.CharField(max_length=100, null=True)
    desc = models.TextField()
    image = CloudinaryField('image')
    pub_date = models.DateTimeField(auto_now=True)

