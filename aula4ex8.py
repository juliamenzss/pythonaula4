valor_compra = float(input("Digite o valor da sua compra:"))
if valor_compra >= 100:
    desconto = valor_compra * 0.10
elif valor_compra >=50:
    desconto = valor_compra * 0.05
else:
    desconto = 0
valor_total = valor_compra - desconto
print(f"Sua compra era de {valor_compra}, com desconto de {desconto} reais, ficou por {valor_total}.")