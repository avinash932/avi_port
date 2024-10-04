from django.db import models


# Create your models here.

class Project(models.Model):
    project_image=models.ImageField()
    project_title=models.CharField(max_length=50)
    description=models.CharField(max_length=200, blank=True)
    refer=models.URLField(blank=True)
    

   
    
class Skill(models.Model):
    name=models.CharField(max_length=25)
    percent=models.IntegerField()
    des=(models.CharField(max_length=70))
    
class Qualification(models.Model):
    name=models.CharField(max_length=50, blank=True)
    year=models.IntegerField(blank=True)
    grade=models.CharField(max_length=10, blank=True)
    description=models.CharField(max_length=200, blank=True)
    icon=models.CharField(max_length=50,blank=True)