from django.contrib import admin
from .models import *


class cliente(admin.ModelAdmin):
    list_display = ("id", 'nombre', "email", "telefono", "direccion")
    list_display_links = ("nombre", "email", "telefono", "direccion")
    list_per_page = 25


class Persona(admin.ModelAdmin):
    list_display = ("id", "nombreCompleto", "interes", "telefono", "email", "ciudad", "eliminado")
    list_display_links = ("id", "nombreCompleto", "interes", "telefono", "email", "ciudad", "eliminado")
    list_per_page = 10


admin.site.register(t_cliente, cliente)
admin.site.register(Person,Persona)
