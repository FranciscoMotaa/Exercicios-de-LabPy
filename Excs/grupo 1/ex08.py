#Elabore um programa python que de entre três números fornecidos pelo utilizador,
#permita encontrar o maior deles.

nr1 = int(input("Introduza o primeiro número: "))
nr2 = int(input("Introduza o segundo número: "))
nr3 = int(input("Introduza o terceiro número: "))

if nr1>nr2 and nr1>nr3:
    print(f"O maior número é {nr1}")
elif nr2>nr1 and nr2>nr3:
    print(f"O maior número é {nr2}")
elif nr3 > nr1 and nr3 > nr2:
    print(f"O maior número é {nr3}")
elif nr1 == nr2 and nr1 == nr3 and nr2 == nr3:
    print("Os números são todos iguais")
