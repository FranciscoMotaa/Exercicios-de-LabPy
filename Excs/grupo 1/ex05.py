"""Elabore um programa python que faça a classificação qualitativa de uma nota de um aluno
segundo os seguintes níveis: [0,5[ = péssimo; [5,8[ = mau; [8,10[ = insuficiente;
[10,12[ = suficiente; [12,16[ = bom; [16,20] = excelente. Valide o valor introduzido."""

nota = float(input("Introduza a nota do aluno (0-20): "))

if nota >20:
    print("Nota inválida")
elif nota>=0 and nota<5:
    print("Péssimo")
elif nota>=5 and nota<8:
    print("mau")
elif nota>=8 and nota<10:
    print("Insuficiente")
elif nota>=10 and nota<12:
    print("suficiente")
elif nota>=12 and nota<16:
    print("bom")
elif nota>=16 and nota<=20:
    print("excelente")
