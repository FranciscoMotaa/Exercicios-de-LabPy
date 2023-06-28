"""Elabore um programa python que permita calcular a média de um aluno atendendo às
notas obtidas em dois testes. O programa deve apresentar se o aluno foi aprovado ou
reprovado, tendo em conta que um aluno aprova sempre que a média é superior ou
igual a 10 valores."""

n1 = float(input("Introduza a primeira nota: "))
n2 = float(input("Introduza a segunda nota: "))

media = (n1+n2)/2

if media >= 10:
    print(f"APROVADO {media}")
else:
    print(f"REPROVADO {media}")
    



