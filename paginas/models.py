from django.db import models

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    genero = models.TextField()
    nota = models.FloatField()
    album_do_ano = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Projetos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ano = models.IntegerField()
    categoria = models.ForeignKey(
        Categoria,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )

    def __str__(self):
        return self.nome

