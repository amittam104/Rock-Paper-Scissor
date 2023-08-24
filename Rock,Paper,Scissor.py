# A rock paper scissor game. User will compete with program.

import random

def game():
    user = input("Choose wisely - 'r' for rock, 'p' for paper or 's' for scissor\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie."
    
    if rule(user, computer):
        return "You win!"
    
    return "You lost!"    

# r > s, s > p, p > r
def rule(player, opponent):
    if player == 'r' and opponent == 's' or player == 's' and opponent == 'p' or player == 'p' and opponent == 'r':
        return True

print(game())