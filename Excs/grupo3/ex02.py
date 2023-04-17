"""Elabore um programa python que permita aceitar e visualizar de seguida o nome de 20 
pessoas."""
nomes = []

for i in range(20):
    nome =input("Introduza o nome da pessoa: ")
    nomes.append(nome)

print(f"{nomes}\n")

