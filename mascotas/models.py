from django.db import models

class Responsable(models.Model):
    nombre = models.CharField(null=False, max_length=200)
    correo = models.EmailField(unique=True, null=False, max_length=200)
    rut = models.CharField(null=False, max_length=15)

    class Meta:
        verbose_name_plural = "Responsables"
        ordering = ["nombre"]

    def __str__(self):
        return f"Nombre: {self.nombre} Correo: {self.correo} Rut: {self.rut}"

class Mascota(models.Model):
    responsable_id = models.ForeignKey(Responsable, on_delete=models.CASCADE, related_name="mascotas", null=False)

    nombre = models.CharField(null=False, max_length=200)
    anio_nacimiento = models.PositiveIntegerField(null=False)
    especie = models.CharField(null=False, max_length=200)

    class Meta:
        verbose_name_plural = "Mascotas"
        ordering = ["nombre"]

    def __str__(self):
        return f"Nombre: {self.nombre} Año nacimiento: {self.anio_nacimiento} Especie: {self.especie}"
