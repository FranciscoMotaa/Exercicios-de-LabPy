"""Faça um programa python que leia a partir do utilizador 30 números inteiros positivos e 
que apresente o menor deles."""
maior = 0
menor = 999999
variave = 23
for i in range(0,30):
    nr = int(input("Introduza um número inteiro: "))
    if(nr<menor):
        menor = nr
    elif(nr>maior):
        maior = nr

print(f"O maior número é {maior} e o menor é {menor}")

print(variave)



