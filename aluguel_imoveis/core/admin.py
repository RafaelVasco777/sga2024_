# core/admin.py

from django.contrib import admin
from .models import Proprietario, Cliente, Imovel, Contrato, Pagamento
from django.utils.html import format_html

@admin.register(Proprietario)
class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'email')
    search_fields = ('nome', 'cpf', 'email')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'email')
    search_fields = ('nome', 'cpf', 'email')


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'endereco', 'cidade', 'estado', 'valor_aluguel', 'proprietario')
    list_filter = ('tipo', 'cidade', 'estado')
    search_fields = ('endereco', 'cidade', 'proprietario__nome')
    readonly_fields = ('imagem_preview',)

    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="150" />'.format(obj.imagem.url))
        return "Sem imagem"

    imagem_preview.short_description = 'Pré-visualização da Imagem'

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'imovel', 'data_inicio', 'data_fim', 'ativo')
    list_filter = ('ativo', 'data_inicio', 'data_fim')
    search_fields = ('cliente__nome', 'imovel__endereco')

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'contrato', 'data_pagamento', 'valor', 'pago')
    list_filter = ('pago', 'data_pagamento')
    search_fields = ('contrato__id',)
