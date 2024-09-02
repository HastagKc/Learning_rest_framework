from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    publication_year = models.CharField(max_length=4)

    def __str__(self):
        return self.title
