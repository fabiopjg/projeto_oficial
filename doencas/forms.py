from django.forms.models import ModelForm

from .models import Doenca

class DoencaForm(ModelForm):
  class Meta:
    model = Doenca
    exclude = ['enfermeiro']
    fields = '__all__'