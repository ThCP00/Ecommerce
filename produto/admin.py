from django.contrib import admin
from .models import Categoria, Produto



@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('icone', 'nome_produto', 'categoria', 'preco', 'ativo','quantidade')
    list_editable = ('preco','ativo','quantidade')

admin.site.register(Categoria)
