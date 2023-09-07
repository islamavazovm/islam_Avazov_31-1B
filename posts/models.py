from django.db import models

# Create your models here.


class Review(models.Model):
    nickname = models.CharField(max_length=40)
    country = models.CharField(max_length=60)
    comment = models.CharField(max_length=350)
    grade = models.FloatField(default=0, max_length=5.0)
    create_data = models.DateTimeField(auto_now_add=True)
    modification_data = models.DateTimeField(auto_now=True)

class Category(models.Model):
    kind_food = models.CharField(max_length=50)
    count = models.IntegerField(default=0)
#
class Product(models.Model):
    image = models.ImageField(upload_to='product_image',blank=True,null=True)
    title = models.CharField(max_length=50)
    price = models.FloatField()
    compound = models.TextField(blank=False)

    #m2m
    connection = models.ManyToManyField(Category, related_name='category')
    connection_review = models.ManyToManyField(Review,related_name='connection_review')

class Post(models.Model):
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    rate = models.FloatField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

