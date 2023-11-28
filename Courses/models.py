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

    def __str__(self):
        return self.course


class Blog(models.Model):
    title = models.CharField(blank=False, max_length=300)
    intro = models.TextField(blank=False)
    link = models.CharField(blank=False, max_length=200)
    img = models.ImageField(default='quiz.jpg')
    date = models.DateTimeField(auto_created=True)