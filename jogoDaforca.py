"""
REGRA: O jogador terar que acertas as letras da palavra sorteada.
A cada erro do jogador ele perde uma chance, sendo que ele tem 10 chances.
Acabando as chances o joga acaba e ele perde, porem se ele formar a palavra secreta, ele ganha!
"""

# variável com a palavra a ser adivinhada
palavra = "botafogo"

# lista vazia para coletar as letras
letras_usuario = []
# números de tentativas
chances = 7
# variável booleana
ganhou = False

# loop no True
while True:
    # loop para confirmar se a letra contem na palavra
    for letra in palavra :
        # condição se letra há ou não na palavra
        if letra.lower() in letras_usuario:

            print(letra, end=" ")
        else:
            print("_", end=" ")
    # print o número de chances    
    print(f"Você tem {chances} chances")
    # entrada dos dados
    tentativa = input("Escolha uma letra para adivinhar: ")
    # adiciona a letra digitada na lista
    letras_usuario.append(tentativa.lower())
    # verifica se a letra tem na palavra, se não, perde uma chance
    if tentativa.lower() not in palavra.lower():
        chances -= 1
    # se acerta todas as letras, jogo ganho
    ganhou = True
    # se acabar todas as chances, jogo perdido
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False
    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabéns, você ganhou. A palavra é {palavra }")
else:
    print(f"Você perdeu! A palavra era: {palavra } ")









