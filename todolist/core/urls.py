from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.verificar_tarefas),
    path('cadastro', views.cadastro)
]