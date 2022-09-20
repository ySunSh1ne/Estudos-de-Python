print('Simulação de compra de dolar')

M = float(input("Digite o Valor que você possui na sua conta corrente: "))
C = float(input('Digite a Cotação atual do Dolar: '))

print('Com {} voce pode comprar {} em Dolar Hoje com a Cotação de {}'.format(M, (M//C), C))
