 #Faça um programa python para ler a base e a altura de 50 triângulos e imprimir a sua área.

lista = []

for i in range(50):
    base = float(input(f'Digite a base do triângulo {i+1}: '))
    altura = float(input(f'Digite a altura do triângulo {i}: '))
    area = (base * altura) / 2
    lista.append(area)
    print(f'A área do triângulo {i} é: {area}')
print(f'A área total dos triângulos é: {sum(lista)}')
print('-' * 30)
print()





