from django.db import models


class Person(models.Model):
    nombreCompleto = models.CharField(max_length=70)
    interes = models.CharField(max_length=60)
    telefono = models.CharField(max_length=9, null=False)
    email = models.EmailField(unique=True, null=False)
    ciudad = models.CharField(max_length=30)
    eliminado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nombreCompleto

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100, null=False)
    eliminado = models.BooleanField(default=False)


class t_user(models.Model):
    username = models.CharField(max_length=200, null=False, unique=True)
    contra = models.CharField(max_length=200, null=False)


class t_cliente(models.Model):
    nombre = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    telefono = models.CharField(max_length=150, null=False)
    direccion = models.TextField(blank=False)

    def __str__(self):
        return self.nombre
