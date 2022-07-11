from django.db import models

from accounts.models import Enfermeiro


class Doenca(models.Model):
    enfermeiro = models.ForeignKey(Enfermeiro, on_delete=models.SET_NULL, null=True)
    nome = models.CharField(max_length=200)
    medicamentos = models.TextField()
    tratamento = models.TextField()
    sintomas = models.TextField()
    evitar = models.TextField()

    