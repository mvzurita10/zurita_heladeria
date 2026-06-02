from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Sabor, Producto
from .serializers import SaborSerializer, ProductoSerializer
from .permissions import IsAdminOrReadOnly

class SaborViewSet(viewsets.ModelViewSet):
    queryset = Sabor.objects.all().order_by("id")
    serializer_class = SaborSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["nombre_sabor"]
    ordering_fields = ["id", "nombre_sabor"]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.select_related("sabor").all().order_by("-id")
    serializer_class = ProductoSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["sabor"]
    search_fields = ["nombre_sabor", "conteo_productos_disponibles"]
    ordering_fields = ["id", "nombre_sabor", "conteo_productos_disponibles"]

    def get_queryset(self):
        qs = super().get_queryset()
        conteo_productos_disponibles_min = self.request.query_params.get("conteo_productos_disponibles_min")
        conteo_productos_disponibles_max = self.request.query_params.get("conteo_productos_disponibles_max")
        if conteo_productos_disponibles_min:
            qs = qs.filter(anio__gte=int(conteo_productos_disponibles_min))
        if conteo_productos_disponibles_max:
            qs = qs.filter(anio__lte=int(conteo_productos_disponibles_max))
        return qs

    def get_permissions(self):
        # Público: SOLO listar productos
        if self.action == "list":
            return [AllowAny()]
        return super().get_permissions() 