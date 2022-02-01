import random

rolls = {
    'rock': {
        'defeats': ['scissors'],
        'defeated_by': ['paper']
    },
    'paper': {
        'defeats': ['rock'],
        'defeated_by': ['scissors']
    },
    'scissors': {
        'defeats': ['paper'],
        'defeated_by': ['rock']
    }

}


def main():
    show_header()
    player = "You"
    ai = "Computer"

    play_game(player, ai)


def show_header():
    print("------------------")
    print(" Rock Paper Scissors V2")
    print(" Data Structure Edition")
    print("------------------")


def play_game(player_1, player_2):
    wins = {player_1: 0, player_2: 0}

    roll_names = list(rolls.keys())

    while not find_winner(wins, wins.keys()):
        roll1 = get_roll(player_1, roll_names)
        if not roll1:
            print("Try again")
            continue

        roll2 = random.choice(roll_names)
        print(f"{player_1} rolls {roll1}")
        print(f"{player_2} rolls {roll2}")


        winner = check_for_winning_throw(player_1, player_2, roll1, roll2)

        if winner is None:
            print("This round was a tie")
        else:
            print(f"The winner of this round is {winner}")
            wins[winner] += 1

        print(f"{player_1} has {wins[player_1]} win and {player_2} has {wins[player_2]} win")

    overall_winner = find_winner(wins, wins.keys())
    print(f"{overall_winner} wins the game")




def find_winner(wins, names):
    best_of = 3
    for name in names:
        if wins.get(name, 0) >= best_of:
            return name

    return None


def check_for_winning_throw(player_1, player_2, roll1, roll2):
    # Test for a winner
    winner = None
    if roll1 == roll2:
        print("It's a tie")

    outcome = rolls.get(roll1, {})
    if roll2 in outcome.get('defeats'):
        return player_1
    elif roll2 in outcome.get('defeated_by'):
        return player_2

    return winner


def get_roll(player_name, roll_names):
    for index, r in enumerate(roll_names, start=1):
        print(f"{index} : {r}")

    text = input(f"{player_name}, what is your pick?: ")
    selected_index = int(text) - 1

    if selected_index < 0 or selected_index >= len(rolls):
        print(f"Sorry {player_name}, {text} is not a valid play!")
        return None
    return roll_names[selected_index]


if __name__ == '__main__':
    main()
