from django.db import models

class Produto(models.Model):
    produto_nome = models.CharField(max_length=200)
    produto_marca = models.CharField(max_length=100)
    produto_categoria = models.CharField(max_length=100)
    produto_valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    produto_estoque = models.IntegerField(default = 1)
    produto_avaliacao = models.IntegerField(default = 1)

    def __str__(self):
        return self.produto_nome
