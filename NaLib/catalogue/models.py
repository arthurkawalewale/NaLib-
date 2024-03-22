from django.db import models


# Create your models here.
class Catalogue(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    ISBN = models.IntegerField()
    Type = models.CharField(max_length=200)
    Category = models.CharField(max_length=200)
    YearPublished = models.DateField()
    Available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
