from django.db import models

# Create your models here.

class Curso(models.Model):
    nome_curso = models.CharField(max_length=140)
    data_criacao = models.DateField()
    nome_coordenador = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_curso


class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=140)
    email = models.EmailField()
    data_nascimento = models.DateField()
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_aluno