from django.forms import ModelForm
from django.forms.widgets import DateTimeInput

from .models import Evento

class EventoForm(ModelForm):
  class Meta:
    model = Evento
    exclude = ['enfermeiro']
    fields = '__all__'
    widgets = {
      'data': DateTimeInput(
        attrs={ 'type': 'datetime-local' },
        format='%Y-%m-%dT%H:%M'
      )
    }

