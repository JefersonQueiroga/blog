from django.db import models



class Categoria(models.Model):
    nome = models.CharField(max_length=150)


# Create your models here.
class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    data_criacao = models.DateField()

    def __str__(self):
        return self.titulo

