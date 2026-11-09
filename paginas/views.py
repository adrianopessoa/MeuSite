from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def inicio(request):
    contexto = {
        "nome" : "Adriano",
        "cidade" : "Jaboatão dos Gararapes",
        "curso" : ["Eletrotécnica", "Programação FullStack"],
        "hobbies" : ["Futebol", "Video Game", "Assistir Séries"],       
    }
    return render(request, "inicio.html", contexto)

def sobre(request):
    return HttpResponse("<h1>Sobre mim</h1>"
                        "<p>Meu nome é Adriano.</p>"
                        "<a href = '/'>Inicio</a> | "
                        "<a href = '/contato/'>Contato</a>"
                        )

def contato(request):
    return HttpResponse("<h1>Contato</h1>"
                        "<p>E-mail: adriano@email.com</p>"
                        "<a href = '/'>Inicio</a> | "
                        "<a href = '/sobre/'>Sobre</a>"
                        )