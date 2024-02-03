"""
REGRA: O jogador terar que acertas as letras da palavra sorteada.
A cada erro do jogador ele perde uma chance, sendo que ele tem 10 chances.
Acabando as chances o joga acaba e ele perde, porem se ele formar a palavra secreta, ele ganha!
"""
from random import choice

palavra = "botafogo"

letras_usuario = []
chances = 7
ganhou = False


while True:
    for letra in palavra :
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    
    print(f"Você tem {chances} chances")

    tentativa = input("Escolha uma letra para adivinhar: ")

    letras_usuario.append(tentativa.lower())
    
    if tentativa.lower() not in palavra.lower():
        chances -= 1
        
    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False
    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabéns, você ganhou. A palavra é {palavra }")
else:
    print(f"Você perdeu! A palavra era: {palavra } ")









