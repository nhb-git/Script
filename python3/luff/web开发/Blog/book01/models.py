from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    pub_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish = models.ForeignKey(
        to='Publish', to_field='id', on_delete=models.CASCADE
    )
    authors = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.name


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    author_detail = models.OneToOneField(
        to='AuthorDetail', to_field='id', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Publish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self):
        return self.name


class AuthorDetail(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    telephone = models.CharField(max_length=32)
    addr = models.CharField(max_length=128)
    birthday = models.DateField()

    def __str__(self):
        return self.telephone


class PageDemo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    email = models.EmailField()
    tel = models.CharField(max_length=30)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.name
