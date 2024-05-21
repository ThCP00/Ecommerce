from django.db import models
from django.utils.safestring import mark_safe

class Categoria(models.Model):
    categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.categoria

class Produto(models.Model):
    nome_produto = models.CharField(max_length=500)
    img = models.ImageField(upload_to='post_img')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.FloatField()
    descricao = models.TextField()
    quantidade = models.IntegerField(default=1)
    ativo = models.BooleanField(default=True)

    @mark_safe
    def icone(self):
        return f'<img width="30px" src="/media/{self.img}">'

    def __str__(self):
        return self.nome_produto
    