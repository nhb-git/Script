from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=32)
    pub_date = models.DateField()


class Author(models.Model):
    pass


class Publish(models.Model):
    pass


class AuthorDetail(models.Model):
    pass
