def main():
    show_headers()
    player_1 = input("Enter player 1's name: ")
    player_2 = input("Enter player 2's name: ")

    play_the_game(player_1, player_2)


def show_headers():
    print("------------------------")
    print(" Rock/Paper/Scissors V1")
    print("------------------------")


def get_the_rolls(player_name):
    rolls = ["rock", "paper", "scissors"]

    roll = input(f"{player_name}, please make your pick: ")
    roll.lower().strip()
    while roll not in rolls:
        print("sorry, that is not a valid play")
        roll = input(f"{player_name}, try again: ")
        roll = roll.lower().strip()
        continue
    return roll


def play_the_game(player1, player2):
    rounds = 3
    win_p1 = 0
    win_p2 = 0
    while win_p1 < rounds and win_p2 < rounds:
        roll1 = get_the_rolls(player1)
        roll2 = get_the_rolls(player2)
        print(f"{player1} picked {roll1} and {player2} picked {roll2}")

        winner = check_for_winner(roll1, roll2, player1, player2)
        if winner is None:
            print("The round was a tie")
        else:
            print(f"{winner} takes the round")
            if winner == player1:
                win_p1 += 1
            else:
                win_p2 += 1
        print(f"The rounds are {player1}:{win_p1} and {player2}:{win_p2}\n")
    overall_winner = None
    if win_p1 == rounds:
        overall_winner = player1.upper()
    else:
        overall_winner = player2.upper()
    print(f"THE GRAND CHAMPION IS ... {overall_winner}")


def check_for_winner(roll1, roll2, player1, player2):
    winner = None
    if roll1 == roll2:
        winner = None
    elif roll1 == "rock":
        if roll2 == "paper":
            winner = player2
        else:
            winner = player1
    elif roll1 == "paper":
        if roll2 == "scissors":
            winner = player2
        else:
            winner = player1
    elif roll1 == "scissors":
        if roll2 == "rock":
            winner = player2
        else:
            winner = player1
    return winner


if __name__ == '__main__':
    main()
