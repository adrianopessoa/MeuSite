from django.shortcuts import render, redirect
from .forms import ProjetoForm

# Create your views here.

from django.http import HttpResponse

from .models import Album, Categoria, Projetos

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

def categoria(request):
    contexto ={
        "categ" : Categoria.objects.all(),
    }
    return render(request, "categorias.html", contexto)

def novo_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/projetos/")
    else:
        form = ProjetoForm()
    return render(request, "novo_projeto.html",
                  {"form": form})