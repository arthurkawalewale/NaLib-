from django.db import models


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    qualification = models.TextField(max_length=300)
    contact_info = models.TextField(max_length=300)

    def __str__(self):
        return self.first_name + self.last_name
