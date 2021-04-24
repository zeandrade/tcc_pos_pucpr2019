from django.urls import path

from . import views
app_name = 'exemplo'

urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('restrito/', views.restrito, name='restrito'),
    path('projetos/', views.pre_sql_safe, name='projetos'),
    path('projeto/<int:registro_id>/', views.sql_safe, name='projeto'),
    path('command-safe/', views.command_safe, name='command-safe'),
    path('pesquisa-exemplo/', views.pesquisa_exemplo, name='pesquisa-exemplo'),
]
