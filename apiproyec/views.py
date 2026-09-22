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