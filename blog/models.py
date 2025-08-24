from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
    