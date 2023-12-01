from django.db import models

from django.contrib.auth.models import User
from PIL import Image


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    subject = models.CharField(max_length=200, blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name

class Courses(models.Model):
    course = models.CharField(max_length=200, blank=False)
    image = models.ImageField(default='comp.jpg')
    description = models.TextField(blank=False)
    price = models.IntegerField(blank=False)
    users = models.IntegerField(default=175)
    comments = models.IntegerField(default=56)

    def __str__(self):
        return self.course


class Blog(models.Model):
    title = models.CharField(blank=False, max_length=300)
    intro = models.TextField(blank=False)
    link = models.CharField(blank=False, max_length=200)
    img = models.ImageField(default='quiz.jpg')
    date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.IntegerField(blank=False)
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    link = models.CharField(max_length=300, blank=False, default='https://www.wikipedia.com')
    detail = models.TextField(blank=False)
    poster = models.ImageField(default='soon.jpeg')

    def __str__(self):
        return self.title


class Review(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(blank=False)
    star = models.IntegerField()
    img = models.ImageField(default='icon.png')

    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.CharField(max_length=100)
    img1 = models.ImageField(default='write.jpg')
    img2 = models.ImageField(default='write.jpg')
    img3 = models.ImageField(default='write.jpg')

    def __str__(self):
        return self.name