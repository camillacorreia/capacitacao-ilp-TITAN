#Crie um jogo de forca que um jogador irá digitar a palavra secreta e então outros
#jogadores tentarão acertar qual é a palavra e terão 5 tentativas para acertar.

print('*********************************')
print('***Bem vindo ao jogo da forca!***')
print('*********************************')

import random

def acumularvalor():
    dicionario = {"Nome": [], "Animal": [], "Cor": []}
    while True:
        tipo = input(f"Adcione uma palavra ao tema\n"
                     "[1] para Nome\n"
                     "[2] para Animal\n"
                     "[3] para Cor\n"
                     "[4] inicar JOGO\n"
                     "Digite sua opção: ")

        if tipo == "4":
            break

        if not tipo == "1" and not tipo == "2" and not tipo == "3":
            print("Valor inválido, tente novamente")
            continue

        elif tipo == "1":
            dicionario["Nome"].append(input("Diga um nome: ").lower())

        elif tipo == "2":
            dicionario["Animal"].append(input("Diga um animal: ").lower())

        else:
            dicionario["Cor"].append(input("Diga uma cor: ").lower())
    return dicionario

def palavrasecreta(dicionario):
    while True:
        escolha = input("[1] Nome\n"
                        "[2] Animal\n"
                        "[3] Cor\n"
                        "Escolha um tema: ")

        if escolha != "1" and escolha != "2" and escolha != "3":
            print("Valor inválido, tente novamente")
            continue

        elif escolha == "1":
            secreta = random.choice(dicionario["Nome"])

        elif escolha == "2":
            secreta = random.choice(dicionario["Animal"])

        else:
            secreta = random.choice(dicionario["Cor"])
        return secreta

def analizador(quantidade, secreta):
    digitados = []
    vida = 5
    print(f"A palavra secreta tem {quantidade} letras")

    while True:
        if vida == 0:
            print("VOCÊ PERDEU O JOGO!!!!")
            break

        print(f"Você tem {vida} pontos de vida!")
        chute = input("Dê seu melhor chute: ").lower()

        if not chute in secreta:
            vida -= 1
            print("Você errou")

        digitados.append(chute)
        reveletion = ""

        for letra in secreta:
            if letra in digitados:
                reveletion += letra
            else:
                reveletion += "*"

        print(reveletion)

        if not "*" in reveletion:
            print("VOCÊ GANHOU!!")
            break


dicionario = acumularvalor()

print("Vamos começar!!!")

secreta = palavrasecreta(dicionario)

quantidade = len(secreta)

analizador(quantidade, secreta)