from django.db import models
from django.contrib.auth.models import User, UserManager
from django import forms 


# Create your models here.

class Notebook(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name
    

class Note(models.Model):
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)
    category = models.CharField(blank=True,max_length=40)
    title = models.CharField(max_length=40)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(self.body[0:50])


