from django.db import models
from myReference.utils import unique_slug_generator 
from myReference.utils2 import unique_slug_generator_page
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Create your models here.
class Post(models.Model):
    tittle = models.CharField(max_length=100 , default= "")
    category = models.CharField(max_length=100 , default= "")
    data = models.TextField(null=True , blank= True)
    pdf = models.FileField(null=True , blank= True)
    slug = models.SlugField(max_length=200, null=True , blank= True)
    def __str__(self):
        return str(self.tittle)

def slug_generator(sender , instance , *args , **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

    
pre_save.connect( slug_generator ,sender = Post )

class category(models.Model):
    tittle = models.CharField(max_length=100 , default= "")
    data = models.TextField(null=True , blank= True)
    pdf = models.FileField(null=True , blank= True)
    slug = models.SlugField(max_length=200, null=True , blank= True)
    def __str__(self):
        return str(self.tittle)

def slug_generator_page(sender , instance , *args , **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_page(instance)

pre_save.connect( slug_generator_page ,sender = category )