"""Elabore um programa python que permita calcular a soma dos 20 primeiros números 
pares positivos."""

soma = 0

for i in range(20):
    if i % 2 == 0: 
        soma = soma + i

print(f"A soma dos 20 primeiros elementos pares é de {soma}")



