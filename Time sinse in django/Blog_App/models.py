from django.db import models
from django.contrib.auth.models import User

from scripts.utils import jalali_convert
from django.urls import reverse
from PIL import Image

class Category(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):


        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)

    def get_jalali_date(self):

        return jalali_convert(self.created)

    def __str__(self):

        return self.name


class BlogModel(models.Model):

    user=models.ForeignKey(User,on_delete=models.SET_NULL,related_name="blog",null=True,blank=True)
    titel=models.CharField(max_length=200)
    view=models.IntegerField(default=0)
    image=models.FileField(upload_to="media/blog/image")
    text=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    category=models.ManyToManyField(Category,related_name="blog")
    status=models.BooleanField(default=True)

    def get_absolut_url(self):


        return reverse("Blog_App:blog_detail",kwargs={"pk":self.id})

    def save(self,*args,**kwargs):

        super().save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)


    def get_jalali_date(self):


        return jalali_convert(self.created)

    def __str__(self):

        return self.titel
