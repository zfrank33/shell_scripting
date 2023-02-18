import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    computer = random.choice(options)

    print("Rock, paper, scissors! Shoot!")
    player = input().lower()

    if player == computer:
        print("It's a tie!")
    elif player == 'rock':
        if computer == 'scissors':
            print("You win! Rock beats scissors.")
        else:
            print("You lose! Paper beats rock.")
    elif player == 'paper':
        if computer == 'rock':
            print("You win! Paper beats rock.")
        else:
            print("You lose! Scissors beat paper.")
    elif player == 'scissors':
        if computer == 'paper':
            print("You win! Scissors beat paper.")
        else:
            print("You lose! Rock beats scissors.")
    else:
        print("Invalid input. Please try again.")
        play_game()

if __name__ == '__main__':
    play_game()
