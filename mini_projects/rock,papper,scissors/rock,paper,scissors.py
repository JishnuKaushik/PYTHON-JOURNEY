import random

options = ("rock", "paper", "scissors")
running = True

while running: # this here to keep this game on loop until we type something else except of y 

    player = None
    computer = random.choice(options)

    while player not in options: # why we add this line is because if what player chosse is not in the option then this loop keep on continuing.
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a tie!")
    elif player == "rock" and computer == "scissors":
        print("you win!")
    elif player == "scissors" and computer == "paper":
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("you win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")        