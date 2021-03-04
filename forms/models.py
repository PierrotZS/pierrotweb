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
