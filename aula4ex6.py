num_conta = int(input("Escreva o número da sua conta:  "))
saldo = float(input("Digite seu saldo de conta: "))
credito = float(input("Digite seu valor de credito: "))
saldo_atual = saldo + credito
if saldo_atual >= 0:
    print(f"Seu saldo atual é de {saldo_atual} então seu saldo está positivo.")
else:
    print(f"Seu saldo é de {saldo_atual} então seu saldo é negativo.")