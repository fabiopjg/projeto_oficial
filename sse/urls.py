from django import views
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

from accounts.views import listar_alunos, detail_aluno

urlpatterns = [
    path('', RedirectView.as_view(url="/eventos", permanent=True)),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('eventos/', include('eventos.urls')),
    path('doencas/', include('doencas.urls')),
    path('alunos/', listar_alunos, name='listar_alunos'),
    path('alunos/<int:id_aluno>', detail_aluno, name='detail_aluno'),
]
