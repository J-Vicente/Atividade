from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='images')