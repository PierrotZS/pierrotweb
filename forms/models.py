from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    episode = models.CharField(max_length=4, null=True)
    videolink = models.CharField(max_length=100, null=True)
    desc = models.TextField()
    image = CloudinaryField('image', null=True)
    pub_date = models.DateTimeField(auto_now=True)

