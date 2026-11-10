from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def inicio(request):
    contexto = {
        "nome" : "Adriano",
        "curso" : ["Python", "Git", "Django"],       
    }
    return render(request, "inicio.html", contexto)

def sobre(request):
    contexto = {
        "cidade" : "Brasil",
        "hobbies" : ["Futebol", "Video Game", "Assistir Séries"],
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
        "proj" : ["Calculadora em Python", "Biblioteca com classes", "Meu site em Django"]
    }
    return render(request, "projetos.html", contexto)