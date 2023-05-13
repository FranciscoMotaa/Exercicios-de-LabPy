"""Faça um programa que calcule a velocidade média de um veículo em (Km/h). Para tal o 
utilizador deverá introduzir a distância percorrida (em Km) e o tempo gasto a percorrer 
essa distância (em minutos). """ 

print('-'*30)

distancia = float(input("Introduz a distancia percorrida em km: "))
tempo = float(input("Introduz o tempo gasto em minutos: "))
velocidade = distancia/tempo 
print(f"A velocidade media do veículo é {velocidade}km/h")
