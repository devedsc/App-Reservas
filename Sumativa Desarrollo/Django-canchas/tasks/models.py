from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creada = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(
        null=True, blank=True
    )  # sirve para las canchas
    important = models.BooleanField(default=False)  # sirve para las canchas
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (
            self.titulo
            + "-"
            + self.user.username  # Marca error, pero funciona igual nose xq
        )  # Sirve para mostrar titulo de dato en bd
