from django.db import models

# Create your models here.
'''
publish -- book  一对多
'''


# 作者
class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    author_detail = models.OneToOneField(
        to='AuthorDetail', to_field='nid', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


# 作者详情表
class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)

    def __str__(self):
        return str(self.telephone)


# 出版社表
class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()


class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publish_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish = models.ForeignKey(to='Publish', to_field='nid', on_delete=models.CASCADE)
    read_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)

    authors = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.title

