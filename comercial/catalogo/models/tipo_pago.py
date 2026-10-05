from django.db import models


class TipoPago(models.Model):

    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    descripcion = models.CharField(
        max_length=255, null=True, verbose_name="Descripción")

    created_at = models.DateTimeField(verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(verbose_name="Fecha de actualización")

    def __str__(self):
        return f"id: {self.id} - Nombre: {self.nombre}"
