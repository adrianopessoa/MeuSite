from django import forms
from .models import Projetos, Categoria, Album

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projetos
        fields = ["nome", "descricao", "ano", "categoria"]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome"]

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["titulo", "ano", "genero", "nota", "album_do_ano"]