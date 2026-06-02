from django.db import models

class Sabor(models.Model):
    nombre_sabor = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.nombre_sabor

class Helado(models.Model):
    sabor = models.ForeignKey(Sabor, on_delete=models.PROTECT, related_name="helados")

    def __str__(self):
        return f"{self.sabor.nombre_sabor}"