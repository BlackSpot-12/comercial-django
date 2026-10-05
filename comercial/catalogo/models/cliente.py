from django.db import models


class Cliente(models.Model):

    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    telefono = models.CharField(max_length=9, verbose_name="Teléfono")

    correo = models.CharField(max_length=150, null=True, verbose_name="Correo")
    direccion = models.CharField(
        max_length=255, null=True, verbose_name="Dirección")

    created_at = models.DateTimeField(verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(verbose_name="Fecha de actualización")

    def __str__(self):
        return f"id: {self.id} - Cliente: {self.nombre} {self.apellido}"
