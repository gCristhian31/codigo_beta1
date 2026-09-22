from rest_framework import serializers
<<<<<<< HEAD
from .models import Libro, ArticuloTecnologico, Estudiante, Prestamo

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Libro
        fields = ['idLibro','titulo','autor','año_Publicacion']


class ArticuloTecnologicoSerializer(serializers.ModelSerializer):
    class Meta:
        model= ArticuloTecnologico
        fields = ['idArticulo','tipo']

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiante
        fields=[
            'idEstudiante',
            'nombre_Completo',
            'rut',
            'correo_Institucional',
            'telefono',
        ]

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Prestamo
        fields=[
            'idPrestamo',
            'libro',
            'articuloTecnologico',
            'estudiante',
            'profesor',
            'fechaPrestamo',
            'fechaVencimiento',
            'fechaDevolucion',
            'estadoPrestamo',
            'registradoPor',
            'devolucionRegistradaPor',
        ]
        read_only_fields=[
            'idPrestamo',
            'fechaDevolucion',
            'estadoPrestamo',
            'registradoPor',
            'devolucionRegistradaPor',
        ]
    def validate(self, attrs):
        libro = attrs.get('libro')
        articulo= attrs.get('articuloTecnologico')
        estudiante = attrs.get('estudiante')
        profesor = attrs.get('profesor')
        fecha_prestamo= attrs.get('fechaPrestamo')
        fecha_vencimiento=attrs.get('fechaVencimiento')

        if bool(libro)==bool(articulo):
            raise serializers.validationError('Selecciona un libro o un articulo tecnologico, no ambos.')

        if bool(estudiante)==bool(profesor):
            raise serializers.ValidationError('Selecciona un estudiante o un profesor, no ambos.')

        if profesor and libro:
            raise serializers.ValidationError('Los profesores solo pueden recibir articulos tecnologicos.')

        if fecha_prestamo is None or fecha_vencimiento is None:
            raise serializers.ValidationError('Debes indicar la fecha del prestamo y la del vencimiento.')

        dias = (fecha_vencimiento-fecha_prestamo).days

        if dias<0:
            raise serializers.ValidationError('El vencimiento no puede ser anterior al prestamo')

        if estudiante and dias not in [1,3,6]:
            raise serializers.ValidationError('El prestamo a estudanites debe durar 1, 3 o 6 dias.')
        pendientes=Prestamo.objects.filter(fechaDevolucion__isnull=True)

        if libro and pendientes.filter(libro=libro).exists():
            raise serializers.ValidationError('Este libro tiene un prestamo sin devolver.')

        if articulo and pendientes.filter(articuloTecnologico=articulo).exists():
            raise serializers.ValidationError('este articulo tiene un prestamo sin devolver')
        return attrs
        
        
=======
from .models import Libro,ArticuloTecnologico,Restriccion

#

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = [
            'idLibro',
            'nombre',
            'autor',
            'anioPublicacion',
        ]



#RN-3
class ArticuloTecnologicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticuloTecnologico
        fields = [
            'idArticulo',
            'tipo',
        ]


# RF-08 y RF-10 
class RestriccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restriccion
        fields = [
            'idRestriccion',
            'estudiante',
            'tipoRestriccion',
            'fechaRestriccion',
            'estadoRestriccion',
        ]
# RF-17: consulta de libros más prestados
class LibroMasPrestadoSerializer(serializers.ModelSerializer):
    totalPrestamos = serializers.IntegerField(read_only=True)

    class Meta:
        model = Libro
        fields = [
            'idLibro',
            'nombre',
            'autor',
            'anioPublicacion',
            'totalPrestamos',
        ]
>>>>>>> d464479 (15:43)
