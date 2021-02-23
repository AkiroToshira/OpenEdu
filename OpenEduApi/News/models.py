from django.db import models


class Article(models.Model):
    """"Стаття"""
    name = models.CharField(max_length=100)
    creation_date = models.DateField(auto_now=True)
    mini_description = models.CharField(max_length=500)
    description = models.TextField(max_length=5000)
    img = models.ImageField(upload_to='article', blank=True)

    def __str__(self):
        return self.name