velocidade_atual = float(input("Digite a velocidade atual:"))
limite = 80

if velocidade_atual < limite:
    print("Voce está abaixo do limite.")
else:
    excesso_velocidade = velocidade_atual - limite
    valor_multa = excesso_velocidade * 5.00
    print(f"O carro está acima da velocidade permitida, multa de R${valor_multa} por {excesso_velocidade}km/h acima do limite.")

