from django.urls import path

from . import views

urlpatterns = [
    path('', views.editar_conta, name="editar_conta"),
    path('register/', views.register, name="signup"),
    path('register/aluno', views.registerAluno, name="signup"),
    path('register/enfermeiro', views.registerEnfermeiro, name="signup"),
]
