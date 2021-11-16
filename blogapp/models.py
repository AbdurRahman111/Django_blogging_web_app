from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User


class blog_post(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    discription = RichTextField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True, upload_to='post_img')
    img2 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img3 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img4 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img5 = models.ImageField(blank=True, null=True, upload_to='post_img')
    img6 = models.ImageField(blank=True, null=True, upload_to='post_img')
    time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title


class Blogs_Comments(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Blog = models.ForeignKey(blog_post, on_delete=models.CASCADE)
    comment_subject = models.CharField(max_length=255)
    comment_text = models.TextField()
    time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.User.email + " - "+ self.Blog.title




class get_in_touch(models.Model):
    user_email = models.CharField(max_length=255)
    time = models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.user_email