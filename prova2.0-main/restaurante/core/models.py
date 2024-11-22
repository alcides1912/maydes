
# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome = models.CharField(max_length=255)  # Campo para o nome do cliente
    email = models.EmailField(unique=True)             # Campo para o e-mail do cliente
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Mesa(models.Model):
    numero = models.IntegerField(unique=True)  # Número da mesa
    capacidade = models.IntegerField()  # Capacidade da mesa

    def __str__(self):
        return f'Mesa {self.numero} (Capacidade: {self.capacidade})'


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relaciona a reserva com o cliente
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)  # Relaciona a reserva com a mesa
    data_reserva = models.DateField()
    hora_entrada = models.TimeField()  # Horário de entrada
    hora_saida = models.TimeField()     # Horário de saída
    num_pessoas = models.IntegerField()

    def __str__(self):
        return f'Reserva de {self.cliente.nome} na {self.mesa} para {self.num_pessoas} pessoas'

from django.db import models

class Comida(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)  # Relaciona a reserva com a mesa
    comidas = models.ManyToManyField(Comida)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mesa {self.mesa} - {self.criado_em.strftime("%d/%m/%Y %H:%M")}'

class Evento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_hora = models.DateTimeField()
    cardapio = models.ManyToManyField(Comida, related_name="eventos")
    
    def __str__(self):
        return f'{self.nome} - {self.data_hora.strftime("%d/%m/%Y %H:%M")}'