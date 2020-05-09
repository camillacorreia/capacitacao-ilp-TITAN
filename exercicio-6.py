#Crie um programa que leia dois valores e mostre um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos Números
# [5] Sair
#Seu programa deve executar a ação solicitada em cada caso.

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro:'))
opção = 0
while opção != 5:
    print ('---'*8)
    print ('''
    [01] somar
    [02] multiplicar 
    [03] maior
    [04] novos números
    [05] sair do programa''')
    opção = int(input('>>>'))
    if opção == 1:
        soma =  n1 + n2
        print ('A soma entre {} é {} e igual a {}'.format(n1,n2,soma))
    elif opção == 2:
        mult = n1 + n2
        print ('A multiplicação de {} é {} e igual a {}'.format(n1,n2,mult))
    elif opção == 3:
        if n1 > n2:
            print ('O maior dos números {} e {} é o {}'.format(n1,n2,n1))
        if n1 < n2:
            print ('O maior dos números {} e {} é o {}'.format(n1,n2,n2))
        if n1 == n2:
            print ('Os números são iguais'.format(n1,n2))
    elif opção == 4:
        n1 = int(input('Digite um número:'))
        n2 = int(input('Digite outro:'))
print ('Fim do programa')
