from django.db import models
class modelLista(models.Model):
    tarefa = models.CharField('tarefa',max_length=70)
    data_tarefa = models.DateField('data_tarefa')

    class Meta:
        verbose_name_plural = 'o que fazer'
        verbose_name = 'o que fazer'

    def __str__(self):
        return self.tarefa