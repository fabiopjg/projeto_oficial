from django.db import models

from accounts.models import Enfermeiro


class Evento(models.Model):
  enfermeiro = models.ForeignKey(Enfermeiro, on_delete=models.SET_NULL, null=True)
  tema = models.CharField(max_length=200)
  descricao = models.TextField()
  data = models.DateTimeField()
  lugar = models.CharField(max_length=100)
  apresentadores = models.CharField(max_length=200)
 
  

