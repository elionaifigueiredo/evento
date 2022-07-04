from django.contrib import admin
# Register your models here.
from jornada22.models import Inscrito, Banner, Palestrante,Evento, Organizador, Programacao


@admin.register(Inscrito)
class AdminInscrito(admin.ModelAdmin):
    list_display = ['nome','email','cpf']

@admin.register(Banner)
class AdminBanner(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Palestrante)
class AdminPalestrante(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Evento)
class AdminEvento(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Organizador)
class AdminOrganizador(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Programacao)
class AdminProgramacao(admin.ModelAdmin):
    list_display = ['nome','inicio','fim']

