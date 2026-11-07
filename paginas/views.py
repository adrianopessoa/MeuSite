from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def inicio(request):
    dados = {
        "nome" : "Adriano",
        "idade" : 38,
        "altura" : 1.76,
        "pets" : ["pipoca", "mel"]        
    }
    return render(request, "inicio.html", dados)

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