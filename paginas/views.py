from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjetoForm, CategoriaForm, MusicaForm

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

def nova_musica(request):
    if request.method == "POST":
        form = MusicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/musicas/")
    else:
        form = MusicaForm()
    return render(request, "novo_musica.html",
                    {"form": form})

def categoria(request):
    contexto ={
        "categ" : Categoria.objects.all(),
    }
    return render(request, "categorias.html", contexto)

def nova_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/categorias/")
    else:
        form = CategoriaForm()
    return render(request, "nova_categoria.html",
                  {"form": form})

def novo_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/projetos/")
    else:
        form = ProjetoForm()
    return render(request, "novo_projeto.html", {"form": form})

def detalhe_projeto(request, id):
    projeto = get_object_or_404(Projetos, id=id)
    return render(request, "detalhe_projeto.html", 
                  {"projeto": projeto})

def editar_projeto(request, id):
    projeto = get_object_or_404(Projetos, id=id)
    if request.method == "POST":
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect("/projetos/")
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, "novo_projeto.html", {"form": form})

def excluir_projeto(request, id):
    projeto = get_object_or_404(Projetos, id=id)
    if request.method == "POST": 
        projeto.delete()
        return redirect("/projetos/") 
    return render(request, "excluir_projeto.html", {"projeto": projeto})