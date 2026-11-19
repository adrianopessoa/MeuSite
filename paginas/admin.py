from django.contrib import admin

from  .models import Album

admin.site.register(Album)

from  .models import Categoria, Projetos

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ["nome", "ano", "categoria"]

admin.site.register(Categoria)
admin.site.register(Projetos, ProjetoAdmin)
