from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from .views import LibroViewSet,ArticuloTecnologicoViewSet,EstudianteViewSet , PrestamoViewSet

router = DefaultRouter()
router.register('libros', LibroViewSet)
router.register('articulos', ArticuloTecnologicoViewSet)
router.register('estudiantes', EstudianteViewSet)
router.register('prestamos',PrestamoViewSet)

urlpatterns = router.urls
=======
from .views import LibroViewSet, ArticuloTecnologicoViewSet, RestriccionViewSet, LibroMasPrestadoViewSet, LibroPorAnioViewSet
router = DefaultRouter()

router.register(
    'libros-disponibles',
    LibroViewSet,
    basename='libro-disponible',
)

router.register(
    'articulos-disponibles',
    ArticuloTecnologicoViewSet,
    basename='articulo-disponible',
)

router.register(
    'restricciones',
    RestriccionViewSet,
    basename='restriccion',
)
router.register(
    'libros-mas-prestados',
    LibroMasPrestadoViewSet,
    basename='libro-mas-prestado',
)

router.register(
    'libros-por-anio',
    LibroPorAnioViewSet,
    basename='libro-por-anio',
)


urlpatterns = router.urls
>>>>>>> d464479 (15:43)
