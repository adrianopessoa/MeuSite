from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Olá! Este é o meu primeiro site</h1>"
                        "<a href = 'contato/'>Contato</a> | "
                        "<a href = '/sobre/'>Sobre</a>"
                        )

def sobre(request):
    return HttpResponse("<h1>Sobre mim</h1>"
                        "<p>Meu nome é Adriano.</p>"
                        "<a href = '/'>Inicio</a> | "
                        "<a href = '/contato/'>Contato</a>"
                        )

def contato(request):
    return HttpResponse("<h1>Contato</h1>"
                        "<p>E-mail: adrianopessoa17@gmail.com</p>"
                        "<a href = '/'>Inicio</a> | "
                        "<a href = '/sobre/'>Sobre</a>"
                        )