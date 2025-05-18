from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Contatto(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    cognome = models.CharField(max_length=50, blank=False, null=False)
    telefono = models.CharField(max_length=10, unique=True, blank=False, null=False)

    def __str__(self):
        return f"{self.nome} {self.cognome}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nome', 'cognome', 'telefono'], name='unique_contatto')
        ]