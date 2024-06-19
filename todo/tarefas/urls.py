from django.urls import path
from . import views

app_name = 'tarefa'
urlpatterns = [
    path('lista-categorias/', views.lista_categorias, name='lista_categorias'),
    path('nova-categoria/', views.nova_categoria, name='nova_categoria'),
    path('editar-categoria/?<id_categoria>', views.editar_categoria, name='editar_categoria'),
    path('delete-categoria/?<id_categoria>', views.delete_categoria, name='delete_categoria'),
    path('nova-tarefa/', views.nova_tarefa, name='nova_tarefa'),
    path('editar-tarefa/?<id_tarefa>', views.editar_tarefa, name='editar_tarefa'),
    path('delete-tarefa/?<id_tarefa>', views.delete_tarefa, name='delete_tarefa'),
    path('buscar', views.search, name='search'),
    path('detalhes-tarefa/?<id_tarefa>', views.detalhes_tarefa, name='detalhes_tarefa'),
]