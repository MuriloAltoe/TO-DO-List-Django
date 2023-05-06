from .models import modelLista
from django.forms import ModelForm

class FormTarefa(ModelForm):
    class Meta:
        model = modelLista
        fields = ['tarefa','data_tarefa']


    def limpar_nome(self):
        nome_atividade = self.cleaned_data['tarefa']
        return nome_atividade.upper()
    
    def limpar(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data