from django.db import models
#clase de Django que ya incluye campos y mecanismos de autenticación:
from django.contrib.auth.models import AbstractUser

from django.conf import settings

# Create your models here.
#1)Clase libro 
class Libro(models.Model):
    idLibro = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    anioPublicacion = models.IntegerField()


    def __str__(self):
        return self.nombre

    
#2)Clase articuloTecnologico
class ArticuloTecnologico(models.Model):
    idArticulo = models.BigAutoField(primary_key=True)
    tipo = models.CharField(
        max_length=20,
        choices=[
            ('audifonos', 'Audífonos'),
            ('tablet', 'Tablet'),
            ('notebook', 'Notebook'),
        ],
    )

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.idArticulo}"



# 3)Clase estudiante
class Estudiante(models.Model):
    idEstudiante = models.BigAutoField(primary_key=True)
    nombreCompleto = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    correoInstitucional = models.EmailField()
    telefono = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.nombreCompleto} - {self.rut}"


 # 4)Clase profesor
class Profesor(models.Model):
    idProfesor = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"



# 5)Clase Usuario
class Usuario(AbstractUser):
    idUsuario = models.BigAutoField(primary_key=True)
    rol = models.CharField(
        max_length=20,
        choices=[
            ('jefe', 'Jefe de biblioteca'),
            ('bibliotecario', 'Bibliotecario'),
            ('practicante', 'Practicante'),
        ],
    )

    def __str__(self):
        return f"{self.username} - {self.get_rol_display()}"


#6)Clase Restriccion
class Restriccion(models.Model):
    idRestriccion = models.BigAutoField(primary_key=True)

    tipoRestriccion = models.CharField(
        max_length=20,
        choices=[
            ('libro', 'Libro'),
            ('tecnologico', 'Artículo tecnológico'),
        ],
    )

    fechaRestriccion = models.DateField()

    estadoRestriccion = models.CharField(
        max_length=20,
        choices=[
            ('activa', 'Activa'),
            ('retirada', 'Retirada'),
        ],
        default='activa',
    )

    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.PROTECT,
        related_name='restricciones',
    )

    def __str__(self):
        return (
            f"{self.estudiante} - "
            f"{self.get_tipoRestriccion_display()} - "
            f"{self.get_estadoRestriccion_display()}"
        )



# 7) Clase Prestamo
class Prestamo(models.Model):
    idPrestamo = models.BigAutoField(primary_key=True)

    fechaPrestamo = models.DateField()
    fechaVencimiento = models.DateField()
    fechaDevolucion = models.DateField(
        null=True,
        blank=True,
    )

    estadoPrestamo = models.CharField(
        max_length=20,
        choices=[
            ('activo', 'Activo'),
            ('atrasado', 'Atrasado'),
            ('devuelto', 'Devuelto'),
        ],
        default='activo',
    )

    libro = models.ForeignKey(
        Libro,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='prestamos',
    )

    articuloTecnologico = models.ForeignKey(
        ArticuloTecnologico,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='prestamos',
    )

    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='prestamos',
    )

    profesor = models.ForeignKey(
        Profesor,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='prestamos',
    )

    registradoPor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='prestamosRegistrados',
    )

    devolucionRegistradaPor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='devolucionesRegistradas',
    )

    def __str__(self):
        return f"Préstamo {self.idPrestamo}"