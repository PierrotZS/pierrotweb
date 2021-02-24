"""Model for Blog."""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.utils import timezone
from cloudinary.models import CloudinaryField

class anime(models.Model):
    """Model for Blog."""
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="anime", on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)
    image = models.ImageField(upload_to='images/posts', null=True)
    episodeth = models.CharField(max_length=4)
    videolinkth = models.CharField(max_length=100)
    episoderaw = models.CharField(max_length=4)
    videolinkraw = models.CharField(max_length=100)
    episodeen = models.CharField(max_length=4)
    videolinken = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "anime"

    def __str__(self):
        return str(self.title)

    def is_published(self):
        now = timezone.now()
        if now >= self.pub_date:
            return True
        return False

class AnimeReport(models.Model):
    """Model for report."""
    TOPIC_CHOICES = (
        ('Video not load', 'Video not load'), ('Cant watch', 'Cant watch'), ('Not have episode', 'Not have episode'),
        ('Not have anime', 'Not have anime'), ('Others', 'Others')
    )

    blog = models.ForeignKey(Blog, related_name="reports", on_delete=models.CASCADE)
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    text = models.TextField(blank=True, default='')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '[Blog: %s] Topic: "%s" reported by %s, %s' \
               % (self.blog, self.topic, self.author, self.pub_date)