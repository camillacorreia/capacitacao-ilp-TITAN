#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando seu  preço normal e condição de pagamento:
# à vista, dinheiro ou cheque com 10% de desconto;
# à vista no cartão, com 5% de desconto;
# em até 2x no cartão com o preço normal;
# 3x ou mais no cartão com 20% de juros.

n1=float(input('digite o preço do produto:  '))
print('como deseja pagar?')
print('''         [1] à vista em dinheiro/cheque
         [2] à vista em cartão 
         [3] até 2x no cartão
         [4] 3x ou mais no cartão''')
n2 = float(input('digite sua escolha:  '))

if n2==1:
    p= (n1*10)/100
    print('Seu produto que custa {:.2f} irá custar {:.2f}'.format(n1,p))
elif n2==2:
    p= (n1*5)/100
    print('Seu produto que custa {:.2f} irá custar {:.2f}'.format(n1,p))
elif n2==3:
    p= (n1/2)
    print('Seu produto que custa {:.2f} irá custar {:.2f}'.format(n1,p))
elif n2==4:
    p= int(input('quantas parcelas?   '))
    juros = n1+(n1*0.2)
    final = juros /p
    
    print('Seu produto será parcelado em {} de {:.2f} com juros '.format(p,final))
    print('Seu produto que custa {:.2f} irá custar {:.2f}'.format(n1,juros))
else:
    print('Opção invalida')
