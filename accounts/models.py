from pyexpat import model
from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  categorias = [
    ('aln', 'Aluno'),
    ('efm', 'Enfermeiro')
  ]
  generos = [
    ('mas', 'Masculino'),
    ('fem', 'Feminino'),
    ('!01', 'Não binário')
  ]
  categoria = models.CharField(max_length=3, choices=categorias, default='aln')
  telefone = models.IntegerField(default=000000000)
  genero = models.CharField(max_length=3, choices=generos)

class Turma(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

class Aluno(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  matricula = models.CharField(max_length=15)
  idade = models.IntegerField(default=18)
  nome_responsavel = models.CharField(max_length=100)
  tel_responsavel = models.IntegerField('Telefone do Responsavel', default=000000000)
  turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True)
  patologias = models.TextField()


class Enfermeiro(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  idade = models.IntegerField(default=18)
  atendimento = models.DateTimeField()
  
  