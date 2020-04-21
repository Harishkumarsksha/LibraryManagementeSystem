from django.db import models

# Create your models here.


class Book(models.Model):

    name = models.CharField(max_length=200, null=True)
    picture = models.ImageField(null=True, blank=True)
    Author = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    description = models.TextField(max_length=500, null=True)

    def __str__(self):

        return ("{0} {1}".format(self.name, self.Author))
