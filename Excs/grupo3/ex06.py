"""Dada uma série de 20 valores reais no intervalo [0, 15], faça um programa python que 
calcule e escreva a média aritmética destes valores. Entretanto se a média obtida for 
maior que 8 deverá ser atribuída 10 para a média."""

soma = 0

for i in range(0,20):
    n = int(input("Introduza um valor entre 0-15: "))
    if n > 15 or n < 0:
        print("Valor inválido.")
        continue 
    soma = soma + n 

media = soma/20

if media > 8:
    media = 10

print(f"A media é {media}")

