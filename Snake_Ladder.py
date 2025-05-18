import random

# Snake and Ladder configuration
Snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
Ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Player positions
player_positions = {"Player 1": 0, "Player 2": 0}


# Function to roll the die
def roll_dice():
    return random.randint(1, 6)


# Function to update player position
def update_position(player, position):
    print(f"{player} rolled the die...")
    roll = roll_dice()
    print(f"{player} got {roll}")
    position += roll

    if position > 100:
        print(f"{player} cannot move beyond 100. Staying at {position - roll}")
        return position - roll

    if position in Snakes:
        print(f"Oh no! {player} landed on a snake at {position}. Going down to {Snakes[position]}")
        position = Snakes[position]
    elif position in Ladders:
        print(f"Yay! {player} climbed a ladder at {position}. Going up to {Ladders[position]}")
        position = Ladders[position]
    else:
        print(f"{player} moved to {position}")

    return position


# Main game loop
def play_game():
    print("Welcome to The Snake and Ladder Game!")
    while True:
        for player in player_positions:
            input(f"\n{player}'s turn. Press Enter to roll the die...")
            player_positions[player] = update_position(player, player_positions[player])

            if player_positions[player] == 100:
                print(f"\nCongratulations {player} wins the game! ")
                return


# Run the game
if __name__ == "__main__":
    play_game()

