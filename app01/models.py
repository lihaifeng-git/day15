from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)

class Publisher(models.Model):
    name = models.CharField(max_length=32,verbose_name='出版社名称')
    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=32,verbose_name='书名')
    pub=models.ForeignKey('Publisher',on_delete=models.CASCADE,verbose_name='出版社名称')
    def __str__(self):
        return self.title

class Author(models.Model):
    name=models.CharField(max_length=32)
    books=models.ManyToManyField('Book')