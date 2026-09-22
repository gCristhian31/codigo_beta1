from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Libro,
    ArticuloTecnologico,
    Estudiante,
    Profesor,
    Restriccion,
    Prestamo,
)

admin.site.register(Libro)
admin.site.register(ArticuloTecnologico)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Restriccion)
admin.site.register(Prestamo)