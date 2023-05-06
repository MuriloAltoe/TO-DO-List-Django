from django import forms
from .models import modelLista

class modelListaForm(forms.ModelForm):
    class Meta:
        model = modelLista
        fields = ('tarefa', 'data')
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'})
        }
