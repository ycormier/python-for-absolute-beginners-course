import random


def main():
    show_header()
    player = input("What is your name? ")
    ai = "Computer"

    play_game(player, ai)


def show_header():
    print("------------------")
    print(" Rock Paper Scissors V1")
    print("------------------")


def play_game(player_1, player_2):
    rounds = 3
    wins_p1 = 0
    wins_p2 = 0

    while wins_p1 < rounds and wins_p2 < rounds:

        rolls = ["rock", "paper", "scissors"]

        roll1 = get_roll(player_1, rolls)
        if not roll1:
            print("Try again")
            continue

        roll2 = random.choice(rolls)
        print(f"{player_1} rolls {roll1}")
        print(f"{player_2} rolls {roll2}")

        winner = check_for_winning_throw(player_1, player_2, roll1, roll2)

        if winner is None:
            print("This round was a tie")
        else:
            print(f"The winner of this round is {winner}")
            if winner == player_1:
                wins_p1 += 1
            else:
                wins_p2 += 1
        print(f"{player_1} as {wins_p1} win and {player_2} has {wins_p2} win\n")

    overall_winner = None
    if wins_p1 == rounds:
        overall_winner = player_1
    else:
        overall_winner = player_2
    print(f"{overall_winner} wins the game")


def check_for_winning_throw(player_1, player_2, roll1, roll2):
    # Test for a winner
    winner = None
    if roll1 == roll2:
        print("It's a tie")
    elif roll1 == "rock":
        if roll2 == "paper":
            winner = player_2
        else:
            winner = player_1
    elif roll1 == "paper":
        if roll2 == "scissors":
            winner = player_2
        else:
            winner = player_1
    elif roll1 == "scissors":
        if roll2 == "rock":
            winner = player_2
        else:
            winner = player_1
    return winner


def get_roll(player_name, rolls):
    for index, r in enumerate(rolls, start=1):
        print(f"{index} : {r}")
        index += 1

    text = input(f"{player_name}, what is your pick? [rock,paper,scissors]: ")
    selected_index = int(text) - 1

    if selected_index <= 0 or selected_index >= len(rolls):
        print(f"Sorry {player_name}, {text} is not a valid play!")
        return None
    return rolls[selected_index]


if __name__ == '__main__':
    main()
