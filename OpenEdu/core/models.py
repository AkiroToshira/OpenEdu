from django.db import models


class Articles(models.Model):
    articles_data = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.name
