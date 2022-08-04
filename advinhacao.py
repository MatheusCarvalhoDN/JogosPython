import random

def jogar():

    print("*******************************")
    print("Bem vindo ao jogo de advinhação")
    print("*******************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade ?")
    nivel = int(input("Defina o nivel (1) Fácil (2) Médio (3) Dificil: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1 ,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Você digitou",chute_str)
        chute= int(chute_str)
        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100")
            continue

        if (numero_secreto == chute):
            print ("Você acertou e fez mais 600 pontos!!")
            pontos = pontos + 600
            break

        else:
            if (numero_secreto < chute):
                print("Numero secreto é menor que",chute)
                pontos_perdidos = abs(chute - numero_secreto)
                pontos = pontos - pontos_perdidos

            elif (numero_secreto > chute):
                print("Numero secreto é maior que", chute)
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

                rodada = rodada + 1

    print ("Fim de Jogo!")
    print("O numero secreto era {}".format(numero_secreto))
    print("Sua quantidade de pontos é {}".format(pontos))

if(__name__=="__main__"):
    jogar()