from django.db import models

# Create your models here.
class Produto(models.Model):
  nome = models.CharField(max_length=100)
  preco = models.FloatField()
  quantidade = models.IntegerField()
  fabricacao = models.CharField(max_length=10)

  class Meta:
    verbose_name = 'Produto'
    verbose_name_plural = 'Produtos'
    ordering = ['-preco']

  def __str__(self):
    return self.nome  