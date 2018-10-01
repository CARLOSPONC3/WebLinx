from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellidoP = models.CharField(max_length=30)
    apellidoM = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
