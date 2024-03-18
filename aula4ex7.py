estoque_atual = int(input("Digite a quantidade atual em estoque:"))
estoque_max = int(input("Digite a quantidade maxima em estoque:"))
estoque_min = int(input("Digite a quantidade minima em estoque:"))
estoque_media = (estoque_min + estoque_max) / 2
print(estoque_media)
if estoque_atual >= estoque_media:
    print("Não efetuar compra.")
else:
    print("Efetuar compra.")