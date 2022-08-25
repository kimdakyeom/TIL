from django.db import models

class Director(models.Model):
    name = models.TextField()
    debut = models.DateTimeField()
    country = models.TextField()

class Genre(models.Model):
    title = models.TextField(null=True,default='')

class Movie(models.Model):
    director = models.ForeignKey(Director,on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    title = models.TextField()
    opening_date = models.DateField(null=True,default='')
    running_time = models.IntegerField(null=True,default='')
    screening = models.BooleanField(null=True,default='')