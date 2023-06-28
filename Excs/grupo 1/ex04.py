"""Implemente um programa em python que converta um valor em bytes para um formato
humanamente legível (Kilo, Mega, Giga ou Tera bytes consoante o múltiplo que melhor se
adapte a uma representação de fácil leitura do valor). Considere 1KBytes = 1024 Bytes.
Exemplo: 16548973 bytes = 15,78 MBytes."""

bytes = float(input("Introduza o valor em bytes: "))

op = input(("Quer converter para quê?\n[1]-kilobytes\n[2]-Megabytes\n[3]-Tera bytes\nIntroduza a sua opção: "))

if op == 1:
    print(f"{(bytes*1)/1024}Kbytes")
elif op == 2:
    print(f"{bytes*10^-6}MB")
elif op==3:
    print(f"{bytes*10^-12}TB")


