import random

def is_win(player, opponent): # Return True if Player wins

    if (player == "R" and opponent == "S")\
        or (player == 'S' and opponent == 'P')\
        or (player == 'P' and opponent == 'R'):
        return True

def play():
    user = input("'R' for Rock, 'P' for Paper, 'S' for Scissors\n What will you choose: ")
    computer = random.choice(['R','P','S'])

    if user == computer:
        return "Tie"
    elif is_win(user, computer):
        return "You won!"

    return "You Lost!"

Result = play()
print(Result)
