from random import randint

Resp = int(input('Entre 1 e 5 escolha o numero sorteado '))
Nr = randint(1, 5)


print('Verificando Resposta...')
print('Isso pode demorar um pouco')

if Nr == Resp:
    print('Voce acertou!!')
else:
    print('infelismente você errou;-;')
    print('A Resposta certa era {}'.format(Nr))