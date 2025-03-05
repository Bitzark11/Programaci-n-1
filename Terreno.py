import math

#Calculo del area del triangulo y rectangulo
base = float(input("ingrese la base del terreno - Triangulo: "))
altura = float(input("ingrese la altura del terreno - Triangulo: "))
altura_rectangulo = float(input("ingrese la altura del rectangulo: "))

#calcular area del terreno
triangulo = (base*altura)/2
rectangulo = base*altura_rectangulo
areatotal = triangulo + rectangulo

print (f"areatotal = {areatotal}")

radio = float(input("ingrese el radio del terreno circular: "))
circulo = math.pi * (math.pow(radio,2))

