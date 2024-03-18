temperatura = int(input("Digite a temperatura atual: "))
if temperatura < 15:
    print("Está frio.")
elif 15 <= temperatura <= 25:
    print("Esta ameno.")
else:
    print("Esta calor.")
