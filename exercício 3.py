Nome = str(input('Digite o Nome do Aluno: '))
Ano = str(input('Digite o Ano em que o Aluno ({}) está:'.format(Nome)))
N1 = float(input('Digite a Primeira Nota: '))
N2 = float(input('Digite a Segunda Nota: '))
N3 = float(input('Digite a Terceira Nota:'))
N4 = float(input('Digite a Quarta nota: '))

Soma = N1 + N2 + N3 + N4

print('O Aluno ({}) do {}° ano  Tirou a Media de ({}) '.format(Nome,Ano,(Soma/4)))