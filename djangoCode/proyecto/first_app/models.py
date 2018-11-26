from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)


    #additional classes
    portfolio_site = models.URLField(blank=True,verbose_name="tu sitio con http://")

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True,verbose_name="Imagen del perfil: ")

    def __str__(self):
        return self.user.username

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellidoP = models.CharField(max_length=30)
    apellidoM = models.CharField(max_length=30)
    numcta= models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    mesa = models.CharField(max_length=2,primary_key=True)
    def __str__(self):
        return self.mesa

class Asientos(models.Model):
    asiento = models.CharField(max_length=2,primary_key=True)
    status = models.BooleanField()
    mesa = models.ForeignKey(Reserva)

    def __str__(self):
        return self.asiento

class Reservaciones(models.Model):
    user = models.ForeignKey(User)
    asientos = models.ForeignKey(Asientos)
    def __str__(self):
        template = 'Reserva del usuario {0.user} asientos: {0.asientos}'
        return template.format(self)
#
# class Detalle(models.Model):
#     usuario = models.ForeignKey(Usuario)
#     reservaciones = models.ForeignKey(Reservaciones)
#     fecha = models.DateField(auto_now=True)
#     cantidad = models.IntegerField()
#     apartado = models.DecimalField(max_digits=10, decimal_places=2)
#     subtotal = models.DecimalField(max_digits=10, decimal_places=2)
#     IVA = models.DecimalField(max_digits=10, decimal_places=2)
#     total = models.DecimalField(max_digits=10, decimal_places=2)
#     def __str__(self):
#         return self.Id_Venta
# #
# class Topic(models.Model):
#     top_name = models.CharField(max_length=264,unique=True)
#
#     def __str__(self):
#         return self.top_name
#
# class Webpage(models.Model):
#     topic = models.ForeignKey(Topic)
#     name = models.CharField(max_length=264,unique=True)
#     url = models.URLField(unique=True)
#
#     def __str__(self):
#         return self.name
#
# class AccessRecord(models.Model):
#     name = models.ForeignKey(Webpage)
#     date = models.DateField()
#
#     def __str__(self):
#         return str(self.date)
