salario = float(input("Digite o valor do seu salário:"))
if salario <= 2000:
    print("Imposto de renda isento.")
elif 2000.01 <= salario <= 3500:
    imposto = salario * 0.10
    print(f"O valor do salario é {salario}, e o valor do imposto é {imposto}")
else:
    imposto = salario * 0.15
    print(f"Ovalor do salario é {salario}, e o valor do imposto é {imposto}.")

