"""Elabore um programa python que permita, através da inserção dos lados de um
triângulo, identificar de que tipo de triângulo se trata (isósceles – dois lados iguais e
um diferente, equilátero – todos os lados iguais, escaleno – se todos os lados forem
diferentes)."""

l1 = float(input("Introduza o primeiro lado do triangulo: "))
l2 = float(input("Introduza o segundo lado do triangulo: "))
l3 = float(input("Introduza o terceiro lado do triangulo: "))

if l1 == l2 and l1 != l3 or l1 == l3 and l1!=l2 or l2==l3 and l2!= l3:
    print("O triangulo é isósceles!")
elif l1==l2 and l1 == l3 and l2 == l3:
    print("O triangulo é equilátero!")
elif l1 != l2 and l1 != l3 and l2 != l3:
    print("O triângulo é escaleno")