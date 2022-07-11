from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, DateTimeInput

from .models import CustomUser, Aluno, Enfermeiro

class UserForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ['username', 'first_name', 'last_name', 'email', 'telefone', 'genero', 'categoria']

class UserEditForm(UserChangeForm):
  password = None
  class Meta:
    model = CustomUser
    fields = ['username', 'first_name', 'last_name', 'email', 'telefone', 'genero', 'categoria']

class AlunoForm(ModelForm):
  class Meta:
    model = Aluno
    fields = '__all__'

class EnfermeiroForm(ModelForm):
  class Meta:
    model = Enfermeiro
    exclude = ['user']
    fields = '__all__'
    widgets = {
      'atendimento': DateTimeInput(
        attrs={ 'type': 'datetime-local' },
        format='%Y-%m-%dT%H:%M'
      )
    }

