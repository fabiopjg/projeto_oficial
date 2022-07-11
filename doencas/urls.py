from django.urls import path

from . import views 

urlpatterns = [
    path('', views.listar, name='listar'),
    path('criar/', views.criar, name='criar'),
    path('excluir/<int:doenca_id>', views.excluir, name='excluir'),
    path('editar/<int:doenca_id>', views.editar, name="editar"),
    path('<int:doenca_id>', views.detail, name='detail'),
]