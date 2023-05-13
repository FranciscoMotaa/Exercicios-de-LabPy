#Dado um valor horário em horas, minutos e segundos, calcule o número de segundos 
#totais. 

horas = int(input("Introduza o número de horas: "))
minutos = int(input("Introduza o número de minutos: "))
segundos = int(input("Introduza o número de segundos: "))
print(horas*3600 + minutos*60 + segundos)

