from django.db import models
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    label = models.ForeignKey('mynote.Label',default = False,max_length=200,blank=True,null = True)


    def __str__(self):
        return self.label




class Label(models.Model):
    label = models.CharField(max_length=200,default = False,null = True)
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.label
