from django.db import models

# Create your models here.
class Groupe(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    groupe = models.ForeignKey('Groupe', on_delete=models.CASCADE)