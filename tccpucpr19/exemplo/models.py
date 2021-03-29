from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Registro(models.Model):
    registro_text = models.CharField(max_length=200)
    data_registro = models.DateTimeField('data de registro')

    def __str__(self):
        return self.registro_text

    def mostrar_recentes(self):
        return self.data_registro >= timezone.now() - datetime.timedelta(days=1)


class Atuacao(models.Model):
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    atuacao_text = models.CharField(max_length=200)
    minutos = models.IntegerField(default=0)
    data_historico = models.DateTimeField('date published')

    def __str__(self):
        return self.atuacao_text

    def mostrar_recentes(self):
        return self.data_historico >= timezone.now() - datetime.timedelta(days=1)
