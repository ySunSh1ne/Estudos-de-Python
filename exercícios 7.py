V = float(input('Coloque o valor do Produto a ser descontado: '))
D = float(input('Digite a % do desconto: '))

VD = V - (V * D / 100)

print('O Produto de {}reais está com desconto de {}% e sai por apenas {}REAIS!!!!'.format(V,D,VD))