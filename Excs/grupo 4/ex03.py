"""O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem 
do distribuidor e dos impostos (aplicados sobre o custo de fábrica). Supondo que a 
percentagem do distribuidor seja de 12% e os impostos de 45%, implemente um algoritmo 
que leia o custo de fábrica do carro e imprima o custo ao consumidor final.""" 

custo = float(input("Introduza o custo de fábrica: "))
custo_distr = custo * 0.12
custo_impostos = custo * 0.45
custo_final = custo + custo_distr + custo_impostos

print(f"O custo final ao consumidor é de {custo_final}")

