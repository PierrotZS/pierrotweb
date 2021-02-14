from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/posts', null=True)
    pub_date = models.DateTimeField(auto_now=True)
