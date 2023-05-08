"""Elabore um programa python que simule uma aplicação que registe a pescaria de um 
barco de pesca. O barco, nos seus porões, pode carregar, no máximo, 150 Toneladas. A 
cada pescaria deve ser registado o valor pescado e somado ao pescado anteriormente. 
Quando atingir ou ultrapassar o valor máximo, a aplicação de terminar e o utilizador deve 
ser informado se tem, ou não, de deitar peixe ao mar e, em caso afirmativo, que 
quantidade."""

x_total = 0

while True:
    x = float(input("Introduza a quantidade pescada em toneladas: "))
    x_total += x
    print(x_total)
    if(x_total > 150):
        print("Você já pescou mais que a quantidade que o barco pode suportar")
        y = x_total - 150
        print(f"Voce deve deitar fora {y} toneladas para o barco suportar esse peso")
        break 






