#Elabore um programa que de entre dois números fornecidos pelo utilizador, permita
#encontrar o menor deles.

nr1 = int(input("Introduza o primeiro numero: "))
nr2 = int(input("Introduza o segunda número: "))

if nr1>nr2:
    print(f"O {nr1} é maior que o número {nr2}")
else:
    print(f"O {nr2} é maior que o número {nr1}")

