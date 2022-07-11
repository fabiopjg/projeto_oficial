from django.contrib import admin

from .models import CustomUser, Aluno, Enfermeiro, Turma

admin.site.register([CustomUser, Aluno, Enfermeiro, Turma])
