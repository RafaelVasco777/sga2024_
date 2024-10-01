from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Proprietario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)  
    telefone = models.CharField(max_length=15)  
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)  
    telefone = models.CharField(max_length=15)  
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Imovel(models.Model):
    TIPO_CHOICES = [
        ('Apartamento', 'Apartamento'),
        ('Casa', 'Casa'),
        ('Comercial', 'Comercial'),
    ]

    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE, related_name='imoveis')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)  
    descricao = models.TextField()
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    imagem = models.ImageField(upload_to='imoveis/', null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} em {self.endereco}, {self.cidade}/{self.estado}"

class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contratos')
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='contratos')
    data_inicio = models.DateField(default=timezone.now)
    data_fim = models.DateField()
    garantia = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"Contrato {self.id} - {self.cliente.nome} - {self.imovel}"

class Pagamento(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='pagamentos')
    data_pagamento = models.DateField(default=timezone.now)
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"Pagamento {self.id} - Contrato {self.contrato.id}"
