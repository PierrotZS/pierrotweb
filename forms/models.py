from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    episode = models.CharField(max_length=4, null=True)
    videolink = models.CharField(max_length=100, null=True)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/posts', null=True)
    pub_date = models.DateTimeField(auto_now=True)

