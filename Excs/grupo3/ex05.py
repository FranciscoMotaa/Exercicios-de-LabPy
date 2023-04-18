"""Elabore um programa python que permita encontrar o maior e menor número de uma
série de números positivos fornecidos (deve parar quando for introduzido -1)."""

maior = 0
menor = 999999

x = 1

while(x != -1):
    x = int(input("Introduza um nr (digite -1 para parar): "))
    if(x == -1):
        break
    elif(x > maior):
        maior = x
    elif(x < menor):
        menor = x

print(f"O maior numero é {maior} e o menor é {menor}")






