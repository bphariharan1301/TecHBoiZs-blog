from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.enums import Choices
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)     
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    portfolio_url = models.CharField(max_length=100, null=True, blank=True)
    fb_url = models.CharField(max_length=100, null=True, blank=True)
    insta_url = models.CharField(max_length=100, null=True, blank=True)
    twitter_url = models.CharField(max_length=100, null=True, blank=True)
    linkedin_url = models.CharField(max_length=100, null=True, blank=True)
    pinterest_url = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    category = models.CharField(max_length=100, default='coding')
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    snippet = models.CharField(max_length=255, default='Snippet to be Added')
    published_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts_likes')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self): # returns likes count 
        return self.likes.count()
 


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments' , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    # def get_absolute_url(self):
        # return HttpResponseRedirect(reverse('article_detail', args=[str(Post.id)]))