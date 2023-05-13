"""Faça um algoritmo que sendo dada a medida de 2 catetos de um triângulo retângulo, 
calcule a medida da hipotenusa."""

a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjacente: '))
c = (a**2 + b**2)**(1/2) 

print(f"A medida da hipotenusa é de {c}")





