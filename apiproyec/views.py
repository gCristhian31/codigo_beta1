<<<<<<< HEAD
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .models import Libro, ArticuloTecnologico, Estudiante, Prestamo
from .serializers import LibroSerializer, ArticuloTecnologicoSerializer, EstudianteSerializer, PrestamoSerializer
class LibroViewSet(viewsets.ModelViewSet):
    queryset= Libro.objects.all()
    serializer_class=LibroSerializer


    def get_queryset(self):
        queryset = Libro.objects.all()

        titulo=self.request.query_params.get('titulo')
        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)
        return queryset

class ArticuloTecnologicoViewSet(viewsets.ModelViewSet):
    queryset=ArticuloTecnologico.objects.all()
    serializer_class= ArticuloTecnologicoSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset=Estudiante.objects.all()
    serializer_class=EstudianteSerializer



class PrestamoViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset= Prestamo.objects.all()
    serializer_class= PrestamoSerializer
    permission_classes=[IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(registradoPor=self.request.user)
=======
from rest_framework import viewsets
from django.db.models import Count
from .permissions import EsJefe
from rest_framework.exceptions import ValidationError



from .models import Libro, ArticuloTecnologico,Restriccion
from .serializers import (
    LibroSerializer,
    ArticuloTecnologicoSerializer,
    RestriccionSerializer,LibroMasPrestadoSerializer
)


#vista Devuelve los libros que no tengan ningún préstamo activo o atrasado.
class LibroViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LibroSerializer
#consulta ORM que devuelve los libros que no tengan ningún préstamo activo o atrasado.
    def get_queryset(self):
        return Libro.objects.exclude(
            prestamos__estadoPrestamo__in=['activo', 'atrasado']
        )

#vista que consulta los artículos tecnológicos disponibles.
class ArticuloTecnologicoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArticuloTecnologicoSerializer
    #consulta ORM que devuelve los artículos tecnológicos que no tengan ningún préstamo activo o atrasado.
    def get_queryset(self):
        return ArticuloTecnologico.objects.exclude(
            prestamos__estadoPrestamo__in=['activo', 'atrasado']
        )

# RF-08 y RF-10 vista RestriccionViewSet permite consultar las restricciones activas de un estudiante para un tipo de recurso.
class RestriccionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RestriccionSerializer

    def get_queryset(self):
        estudiante = self.request.query_params.get('estudiante')
        tipo = self.request.query_params.get('tipo')
        #el identificador del estudiante debe ser un número entero positivo. Si no se proporciona o no es un número, devuelve un error.
        if estudiante is None or not estudiante.isdecimal():
            raise ValidationError({
                'estudiante': 'Debes indicar un identificador numérico.'
            })
        #“Si no se proporciona o no es libro o tecnologico, devuelve un error.
        if tipo not in ['libro', 'tecnologico']:
            raise ValidationError({
                'tipo': 'Debes indicar libro o tecnologico.'
            })

        return Restriccion.objects.filter(
            estudiante_id=int(estudiante),
            estadoRestriccion='activa',
            tipoRestriccion=tipo,
        )

# RF-17: consulta de libros más prestados
class LibroMasPrestadoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LibroMasPrestadoSerializer
    permission_classes = [EsJefe]


    def get_queryset(self):
        return (
            Libro.objects
            .annotate(totalPrestamos=Count('prestamos'))
            .filter(totalPrestamos__gt=0)
            .order_by('-totalPrestamos', 'idLibro')
        )


#RF- 18 Consultar libro por año de publicación. Esta vista permite consultar los libros publicados antes de un año determinado.
class LibroPorAnioViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LibroSerializer
    permission_classes = [EsJefe]


    def get_queryset(self):
        anio = self.request.query_params.get('anio')

        if anio is None or not anio.isdecimal():
            raise ValidationError({
                'anio': 'Debes indicar un año numérico.'
            })

        return Libro.objects.filter(
            anioPublicacion__lt=int(anio)
        ).order_by('anioPublicacion', 'idLibro')



>>>>>>> d464479 (15:43)
