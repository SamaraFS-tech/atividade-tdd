import pytest
from unittest.mock import MagicMock
from pedido.pedido import Item, Pedido, contar_frete_gratis

# =============================================================
# EXEMPLO — um teste pronto, para você copiar o formato
# =============================================================

def test_exemplo_quantidade_total(pedido_pequeno):
    # 1 café + 2 pães de queijo = 3 unidades
    assert pedido_pequeno.quantidade_total() == 3


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug. Cada teste deve FALHAR
# no código original. Não altere src/pedido/pedido.py ainda.
# =============================================================
# Subtotal deve ser preço x quantidade
def test_subtotal_considera_quantidade(pedido_pequeno):
    # 6,00 + (2 x 4,50) = 15,00
    assert pedido_pequeno.subtotal() == 15.0


# Frete grátis a partir de 50,00 (inclusive)
def test_frete_gratis_com_subtotal_exatamente_50():
    pedido = Pedido("Teste", [Item("Combo", 25.0, 2)])  # subtotal 50,00
    assert pedido.tem_frete_gratis() is True


# Item mais caro = maior PREÇO UNITÁRIO
def test_item_mais_caro_usa_preco_unitario():
    pedido = Pedido("Teste", [Item("A", 10.0, 5), Item("B", 20.0, 1)])
    assert pedido.item_mais_caro().nome == "B"


# Item mais barato = menor PREÇO UNITÁRIO
def test_item_mais_barato_usa_preco_unitario():
    pedido = Pedido("Teste", [Item("A", 10.0, 5), Item("B", 20.0, 1)])
    assert pedido.item_mais_barato().nome == "A"


# Desconto percentual sobre o subtotal
def test_total_com_desconto_percentual():
    pedido = Pedido("Teste", [Item("A", 100.0, 1)])
    assert pedido.total_com_desconto(10) == 90.0



# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_frete_gratis(pedidos) -> int
# Escreva os testes ANTES de implementar a função
def test_contar_frete_gratis_todos(pedido_grande):
    outro = Pedido("Teste", [Item("A", 50.0, 1)])
    assert contar_frete_gratis([pedido_grande, outro]) == 2

def test_contar_frete_gratis_nenhum(pedido_pequeno):
    assert contar_frete_gratis([pedido_pequeno]) == 0

def test_contar_frete_gratis_lista_mista(pedido_pequeno, pedido_grande):
    assert contar_frete_gratis([pedido_pequeno, pedido_grande]) == 1

def test_contar_frete_gratis_lista_vazia():
    assert contar_frete_gratis([]) == 0
# Requisito 2 — situacao(unidades_indisponiveis) -> str
# Escreva os testes ANTES de implementar o método



# Requisito 3 — sugerir_frete_gratis(sms_service) -> None
# Use MagicMock para simular o serviço de SMS
# Escreva os testes ANTES de implementar o método
