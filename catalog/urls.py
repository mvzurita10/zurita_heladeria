from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SaborViewSet, ProductoViewSet

router = DefaultRouter()
router.register(r"sabores", SaborViewSet, basename="sabores")
router.register(r"productos", ProductoViewSet, basename="productos")

urlpatterns = []
urlpatterns += router.urls