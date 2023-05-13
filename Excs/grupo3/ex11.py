"""Elaborar um programa python que leia as notas de uma turma de, no máximo, 60 alunos 
num exame de uma disciplina e calcule a sua média. O professor deve apenas inserir as 
notas dos alunos que fizeram o exame, não sendo imperativo que haja a inserção das 60 
notas visto que podem existir alunos que tenham faltado ao exame"""

nota = 0
soma = 0
count = 0

for i in range(60): 
    nota = float(input("Introduza a nota do aluno (digite -1 se quiser parar): "))
    if nota == -1:
        break
    soma = soma + nota 
    count = count + 1
media = soma/count

print(f"A media da turma é de {media}")



