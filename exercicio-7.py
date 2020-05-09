#Crie um jogo de forca que um jogador irá digitar a palavra secreta e então outros
#jogadores tentarão acertar qual é a palavra e terão 5 tentativas para acertar.

print('*********************************')
print('***Bem vindo ao jogo da forca!***')
print('*********************************')

palavra_secreta = (input("Digite a palavra secreta: "))
acertou = False
enforcou = False

while(not acertou and not enforcou):
    chute = input('Qual a letra? ')

    posicao = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            print('Encontrei a letra {} na posição {}.'.format(letra, posicao))
        posicao = posicao + 1

    print('Jogando...')

print('Fim de jogo')