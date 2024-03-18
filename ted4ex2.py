num_de_macas = int(input("Digite o numero de macas: "))
if num_de_macas < 12:
    valor_da_maca = 1.30
elif num_de_macas >= 12:
    valor_da_maca = 1.00
valor_total = num_de_macas * valor_da_maca
print(f"Foram {num_de_macas} maças, por isso cada uma saiu por R${valor_da_maca}.\nO total da compra foi de {valor_total}.")