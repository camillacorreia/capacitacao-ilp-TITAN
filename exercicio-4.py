#Faça um programa que tenha 2 dicionários (um para homem e outro para mulher) e que peça para o usuário o nome,
# a idade e o sexo. Se for homem, os dados entram como chave e valor no dicionário dos homens e o mesmo se
# aplica para as mulheres. Além disso, deve existir uma lista que contenha todas as chaves.
#Deve existir também a opção de exibir todos os elementos dessa lista.

man = {}
woman = {}
total = []

while 1:

    alternativa = int(input("Digite 1 para adicionar um novo elemento e 2 para listar elementos: "))

    if alternativa == 1:
        chave = input("Digite o nome: ")
        valor = int(input("Digite a Idade: "))
        sexo = int(input("Digite o sexo, 1- Masculino e 2- Feminino: "))
        
        if sexo == 1:
            man[chave] = valor
            total.append(chave)
    
        if sexo == 2:
            woman[chave] = valor
            total.append(chave)
    elif alternativa == 2:
        print(total)
        
    print(man,woman)