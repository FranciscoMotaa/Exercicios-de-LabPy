# Considere o seguinte jogo entre dois jogadores: O jogador A pensa num número entre 1 
# e 100. O jogador B tem n tentativas para descobrir esse número. Em cada tentativa o 
# jogador A deve dizer se o número que o jogador B disse é o correto ou se é maior ou 
# menor do que o número pensado. Escreva um programa que implemente este jogo sendo 
# o computador o jogador A.

import random 

nr_pensado = random.randint(0,100)
tentativas = 0

print("Pensei num número entre 0 a 100 adivinha qual foi!")
print("Tens 8 tentativas!")

for i in range(0,8):
    x = int(input("Introduz o número que achas que pensei que pensei: "))
    tentativas = tentativas + 1 
    if(x > nr_pensado):
         print("O número que pensei é menor")
    elif(x < nr_pensado):
         print("O número que pensei é maior")
    elif(x == nr_pensado):
         print(f"Acerteste! O nr que pensei foi o {nr_pensado}")
         break

if tentativas==8:
     print(f"Esgotaste as tuas tentivas o nr que pensei foi {nr_pensado}.")
        


