"""Faça um programa python que repita a mensagem “Introduza a Letra ‘a’: ” até que se 
verifique a sua inserção."""

while True:
    digit = str(input("Introduza a letra 'a':"))

    if digit != "a":
        print("Letra Inválida. Tente novamente.")
        continue
    else:
        print("Letra Inválida")
        break 


