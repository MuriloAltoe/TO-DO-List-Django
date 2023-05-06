from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from core.models import modelLista
from datetime import date

from .forms import FormTarefa

def verificar_tarefas(request):
    dia_de_hoje = date.today()
    select_tarefas = modelLista.objects.all()
    mensagem_para_tela = ''
    Tarefas = {
        'tarefas_do_dia' : mensagem_para_tela
    }
    all_tarefas = ''

    for cursor_tarefa in select_tarefas: 
        if (cursor_tarefa.data_tarefa == dia_de_hoje):
            all_tarefas = all_tarefas + ' -> ' + cursor_tarefa.tarefa     
    
    mensagem_para_tela = 'Hoje temos as seguintes tarefas: ' + str(all_tarefas)

    if mensagem_para_tela == 'Hoje temos as seguintes tarefas: ':
        mensagem_para_tela = 'Sem tarefas para hoje'
    Tarefas = {
        'tarefas_do_dia' : mensagem_para_tela
    }        
    
    return render(request, 'index.html', Tarefas)

def cadastro(request):
    if request.method == 'POST':
        form_atividade = FormTarefa(request.POST)
        if form_atividade.is_valid():
            modelLista.objects.create(**form_atividade.cleaned_data)
            return redirect('/')
        else:
            contexto = {
                'form_atividade': form_atividade
            }
            return render (request, 'cadastro.html', contexto)
    else:
        contexto = {
            'form_atividade': FormTarefa()
        }
        return render (request, 'cadastro.html', contexto)
