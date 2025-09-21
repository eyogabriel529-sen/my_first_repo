import random

options = ("rock", "paper", "scissors")


running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        print("invalid!!")
        player = input("Enter a choice(rock, paper or scissors)>>  ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("it's a tie!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    else:
        print("Computer wins! You lose!")


    while True:
        play_again = input("PLAY AGAIN? (Y/N): ").upper()
        if play_again == "Y":
            running = True
            break
        elif play_again == "N":
            running = False
            print("Thanks for playing!!")
            break
        else:
            print("Invalid input! Enter 'y' or 'n'.")
           



