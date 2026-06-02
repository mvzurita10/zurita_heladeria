from rest_framework import serializers
from .models import Sabor, Producto

class SaborSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sabor
        fields = ["id", "nombre_sabor"]

class ProductoSerializer(serializers.ModelSerializer):
    total_productos = serializers.CharField(source="sabor.nombre", read_only=True)

    class Meta:
        model = Producto
        fields = ["id", "nombre_sabor", "conteo_productos_disponibles"]