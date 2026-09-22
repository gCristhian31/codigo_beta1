from rest_framework.routers import DefaultRouter
from .views import LibroViewSet,ArticuloTecnologicoViewSet,EstudianteViewSet , PrestamoViewSet

router = DefaultRouter()
router.register('libros', LibroViewSet)
router.register('articulos', ArticuloTecnologicoViewSet)
router.register('estudiantes', EstudianteViewSet)
router.register('prestamos',PrestamoViewSet)

urlpatterns = router.urls
