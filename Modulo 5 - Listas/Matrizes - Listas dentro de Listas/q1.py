"""
Dada a matriz abaixo, que representa uma tabela de notas de 3 alunos em 3 provas, escreva
um programa que acesse e imprima na tela especificamente a nota da segunda prova do
terceiro aluno.

Python

# pos 0
# pos 1, 2 ,3
lista = [jjrweiojre,fhdskfj,jreotrioeu]

notas = [
 [8.5, 7.0, 9.0], # Aluno 1
 [6.0, 5.5, 7.5], # Aluno 2
 [10.0, 9.5, 8.0] # Aluno 3
]

aluno = notas[0] # linha
nota = aluno[0] # coluna

notaPosica0_aluno2 = notas[1][0]
"""

# Memoria

notas = [
 [8.5, 7.0, 9.0], # Aluno 1
 [6.0, 5.5, 7.5], # Aluno 2
 [10.0, 9.5, 8.0] # Aluno 3
]

print(notas[2][1])