# What do I want to do
# 1 - Create a Rock/Paper/Scissors game
# 2 - Create functions to separate the different parts of the game

def main():
    header()
    num_players = int(input("How many players are playing? "))

    while num_players < 0 or num_players > 2:
        print("Try again")
        num_players = int(input("How many players? "))

    if num_players == 1:
        one_player_game()
    elif num_players == 2:
        two_player_game()



def header():
    print("--------------------------------------------------")
    print("Hello and welcome to my Rock, Paper, Scissors game")
    print("--------------------------------------------------")


def test_for_winner(player1, player2, roll1, roll2):
    winner = None
    if roll1 == roll2:
        print("It's a tie")
    elif roll1 == "rock":
        if roll2 == "paper":
            winner = player2
            print(f"{player2} wins the game")
        else:
            winner = player1
            print(f"{player1} wins the game")
    elif roll1 == "paper":
        if roll2 == "scissors":
            winner = player2
            print(f"{player2} wins the game")
        else:
            winner = player1
            print(f"{player1} wins the game")
    elif roll1 == "scissors":
        if roll2 == "rock":
            winner = player2
            print(f"{player2} wins the game")
        else:
            winner = player1
            print(f"{player1} wins the game")
    return winner


def one_player_game():
    p1_name = input("What is your name: ")
    print(f"Hello {p1_name}, since you are by yourself you will be playing against the computer")
    p2_name = "computer"
    return p1_name, p2_name


def two_player_game():
    p1_name = input("Hello player 1. What is your name: ")
    p2_name = input("Hello player 2. What is your name: ")
    return p1_name, p2_name


if __name__ == '__main__':
    main()
