import random

print('Sorteio de Alunos para o Professor')

print('Digite a seguir o Nome dos Alunos a ser Sorteados')

a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))

Alunos = (a1,a2,a3,a4)
Sorteio = random.choice(Alunos)

print('O Sortudo aluno sortudo foi {} Parabens!! '.format(Sorteio))