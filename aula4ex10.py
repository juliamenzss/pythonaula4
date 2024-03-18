lado1 = int(input("Insira o tamanho do 1º lado do triangulo:"))
lado2 = int(input("Insira o tamanho do 2º lado do triangulo:"))
lado3 = int(input("Insira o tamanho do 3º lado do triangulo:"))

if lado1 == lado2 == lado3:
    print("Esse triãngulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Esse triangulo é isósceles.")
else:
    print("Esse triangulo é escaleno.")
