import random

def jogar():

    imprime_mensagem_de_abertura()

    palavra_secreta = carrega_palavra()

    letras_acertadas = inicializa_letras(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    chances = 6

    print("Você possui {} chances!".format(chances))

    while(not enforcou and not acertou):

        chute = input("Qual letra ?: ")
        chute = chute.strip().upper()

        if(chute == palavra_secreta):
            print("Você advinhou toda a palavra!")
            print("A palavra era : {}".format(palavra_secreta))
            break

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            chances -= 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        if(chances == 0):
            continue
        print("Você possui {} chances ainda !".format(chances))
        print(letras_acertadas)
    if(acertou):
        print("Você ganhou!!")
        print("A palavra era : {}".format(palavra_secreta))
        mostra_trofeu()

    elif(enforcou):
        print("Você foi enforcado!!")
        print("A palavra era : {}".format(palavra_secreta))
        mostra_caveira()
    print("Fim de Jogo!")




def imprime_mensagem_de_abertura():
    print("********************************")
    print("** Bem vindo ao jogo de Forca **")
    print("********************************")

def carrega_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def mostra_trofeu():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mostra_caveira():
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")


def inicializa_letras(palavra_secreta):
    return ["_" for letra in palavra_secreta]

if(__name__=="__main__"):
    jogar()
