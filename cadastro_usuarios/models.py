from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()


    def __str__(self):
        return f'Objeto: {self.nome} do Modelo: {self.__class__.__name__}'