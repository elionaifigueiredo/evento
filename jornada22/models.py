from distutils.command import upload
from django.db import models
from django.urls import reverse
# Create your models here.
class Inscrito(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    cpf = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return self.nome


class Banner(models.Model):
    nome = models.CharField(max_length=10)
    img = models.ImageField(upload_to='img')

    def __str__(self) -> str:
        return self.img.url

class Palestrante(models.Model):
    nome = models.CharField(max_length=20)
    img = models.ImageField('img')
    descricao = models.TextField(max_length=255)

    # class Meta:
    #     db_table = "registro"
    # def __str__(self) -> str:
    #     return self.nome

    def __str__(self) -> str:
        return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=50)
    data = models.DateTimeField(auto_created=True)
    local = models.CharField(max_length=250)
    sobre = models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.nome

class Programacao(models.Model):
    palestrante = models.ForeignKey(Palestrante, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()

    def __str__(self) -> str:
        return self.nome

class Organizador(models.Model):
    nome_menu = models.CharField(max_length=200)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=255)
    img = models.ImageField('img')
    contato = models.CharField(max_length=7)

    def __str__(self) -> str:
        return self.nome




