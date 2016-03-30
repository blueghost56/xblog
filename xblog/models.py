from __future__ import unicode_literals

from django.db import models

# Create your models here.

class NavigationBar(models.Model):
    categoryName=models.CharField(max_length=20)
    linkUrl=models.CharField(max_length=200)
    def __str__(self):
        return self.categoryName

class News(models.Model):
    title=models.CharField(max_length=200)
    publishDate=models.DateTimeField('date published')
    content=models.TextField()
    def __str__(self):
        return self.title
    