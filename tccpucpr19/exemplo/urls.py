from django.urls import path

from . import views
app_name = 'exemplo'

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:registro_id>/', views.ver_registro, name='registro'),

    path('<int:registro_id>/listar_atuacoes/',
         views.listar_atuacoes, name='listar_atuacoes'),

    path('atuacao/<int:atuacao_id>', views.ver_atuacao, name='atuacao'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),

    # esta rota "vulneravel" deve ser a última, para funcionar como uma rota padrão
    path('<parametro>/', views.vulneravel, name='vulneravel'),
]
