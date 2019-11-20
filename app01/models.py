from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)

class Publisher(models.Model):
    name = models.CharField(max_length=32)

class Book(models.Model):
    title=models.CharField(max_length=32)
    pub=models.ForeignKey('Publisher',on_delete=models.CASCADE)

class Author(models.Model):
    name=models.CharField(max_length=32)
    books=models.ManyToManyField('Book')