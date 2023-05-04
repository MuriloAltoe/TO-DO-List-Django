from django.db import models

class modelLista(models.Model):
    tarefa = models.CharField('tarefa',max_length=70)
    dia = models.IntegerField('dia')
    mes = models.IntegerField('mes')
    ano = models.IntegerField('ano')

    def __str__(self):
        return self.tarefa

    class Meta:
        verbose_name_plural = 'o que fazer'
        verbose_name = 'o que fazer'