# tesoura > papel > pedra > tesoura <--- Regra do jogo

# importação biblioteca random <--- sortear aleatoriamente algumas das três opções 
from random import choice


# cria uma lista 
opçoes = ['tesoura', 'papel', 'pedra']
# "randomiza" uma das opções da lista
maquina = choice(opçoes)
# variável para o loop ser sempre True, até que seja False 
jogada = True

# loop em True
while jogada:
    # printa opções para o jogador
    print(" # tesoura\n # papel\n # pedra\n # sair")
    # entrada de dados do usuário
    player = input("Digite uma opção: ")

    # condições para escolha
    if maquina == player.lower():
        print("Jogo Empatado")
    elif player.lower() == 'tesoura':
        if maquina == 'papel':
            print(f"Você venceu! {player.lower()} CORTA {maquina}")
        else:
            print(f"Você perdeu! {maquina} QUEBRA {player.lower()}")
    elif player.lower() == 'papel':
        if maquina == 'pedra':
            print(f"Você Venceu! {player.lower()} COBRE {maquina}")
        else:
            print(f"Você perdeu! {maquina} COBRE {player.lower()}")
    elif player.lower() == 'pedra':
        if maquina == 'tesoura':
            print(f"Você venceu {player.lower()} QUEBRA {maquina}")
        else:
            print(f"Você perdeu {maquina} COBRE {player.lower()}")
    # opção para sair do jogo
    elif player.lower() == 'sair':
            jogada = False
    # para evitar que o jogador digite qualquer opção que não seja do jogo
    else:
        print("Jogada Inválida, digite alguma opção abaixo")
        print('-'*25)
    maquina = choice(opçoes)
