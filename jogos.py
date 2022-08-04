import forca
import advinhacao

print("******************")
print("Escolha o seu jogo")
print("******************")

jogo = int(input("Qual jogo quer executar ? (1) Forca (2) Advinhação: "))

if (jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogando Advinhação")
    advinhacao.jogar()





