from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=80, help_text='Nome da Empresa')
