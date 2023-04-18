"""Elabore um programa python que permita encontrar o maior de um conjunto de números 
gerados aleatoriamente. A geração deve terminar quando for gerado um múltiplo de 7. 
Apresente o maior número e quantos números foram gerados."""

import random 
count = 0
x = 0

while True:
    x = random.randint(0, 100)
    print(x)
    count = count + 1
    if x % 7 == 0:
        break

print(f"foram gerados {count} nrs")





