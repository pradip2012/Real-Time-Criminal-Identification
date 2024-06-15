import datetime
from time import time

from django.db import models

types = [('arson','arson'),('assault and battery','assault and battery'),('bribery','bribery'),
        ('burglary','burglary'),('child abuse','child abuse'),('white-collar crime.','white-collar crime.'),
        ('counterfeiting','counterfeiting'),('cybercrime','cybercrime'),('drug use','drug use'),
        ('embezzlement','embezzlement'),('extortion','extortion'),('forgery','forgery'),('fraud','fraud'),
        ('hijacking','hijacking'),('homicide','homicide'),('incest','incest'),('kidnapping','kidnapping'),
        ('larceny','larceny'),('organized crime','organized crime'),('perjury','perjury'),('piracy','piracy'),
        ('prostitution','prostitution'),('rape','rape'),('robbery','robbery'),('sedition','sedition'),
        ('smuggling','smuggling'),('terrorism','terrorism'),('theft','theft'),('treason','treason'),('usury','usury'),('missing person','missing person')]

class Profile(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    date = models.DateField()
    phone = models.BigIntegerField()
    city = models.CharField(max_length=70)
    crime_type = models.CharField(choices=types,max_length=20,null=True,blank=False,default='arson')
    fir = models.CharField(max_length=500)
    detect = models.BooleanField(default=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name +' '+self.last_name


class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.last_face

