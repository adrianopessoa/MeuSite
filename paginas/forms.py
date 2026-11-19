from django import forms
from .models import Projetos

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projetos
        fields = ["nome", "descricao", "ano", "categoria"]