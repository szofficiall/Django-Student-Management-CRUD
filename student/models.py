from django.db import models


# Create your models here.
class StudentData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True, max_length=254)

    def __str__(self):
        return self.name
