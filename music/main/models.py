from django.db import models

# Create your models here.
class Genre(models.Model):
    name_en = models.CharField(max_length=500)
    name_ru = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name_ru
    
class Tracks(models.Model):
    title = models.CharField(max_length=500)
    duration = models.IntegerField()
    genre = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.title
    