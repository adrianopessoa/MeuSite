from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Album
from .models import Projetos

def inicio(request):
    contexto = {
        "nome" : "Adriano",
        "curso" : ["Python", "Git", "Django"],       
    }
    return render(request, "inicio.html", contexto)

def sobre(request):
    contexto = {
        "cidade" : "Brasil",
        "hobbies" : ["Música", "Futebol", "Jogos", "Séries"],
    }
    return render(request, "sobre.html", contexto)

def contato(request):
    contexto = {
        "email" : "adriano@email.com",
        "telefone" : "(81) 99999-8888"
    }
    return render(request, "contato.html", contexto)

def projetos(request):
    contexto ={
        "proj" : Projetos.objects.all()
    }
    return render(request, "projetos.html", contexto)

def musicas(request):
    contexto ={
        "album": Album.objects.all(),
    }
    return render(request, "musicas.html", contexto)