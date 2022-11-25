'''Pedra pepel tesoura simples'''
import random

#opções do jogo escolhidas aleatoriamente
options = ("pedra", "papel", "tesoura")
play = True

while play:

    player = None
    computer = random.choice(options)

    #laço de repetição para que o usuário insira corretamente a escolha
    while player not in options:
        player = input("Escolha entre pedra, papel ou tesoura: ")

    #exibição das escolhas
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    #verificação e exibição do resultado
    if player == computer:
        print("Empate!")
    elif player == "pedra" and computer == "tesoura":
         print("Vitória!")
    elif player == "papel" and computer == "pedra":
         print("Vitória!")
    elif player == "tesoura" and computer == "papel":
         print("Vitória!")
    else:
         print("Derrota!")

    #usuário decide se quer jogar novamente
    if input("\nJogar novamente? (s/n): ").lower() == "n":
        play = False


