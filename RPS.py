import random

options = ["rock","paper","scissors"]
Users_Choice = input("choose and option between rock paper and scissors: ")

Computers_Choice = random.choice(options)
print(f"you chose {Users_Choice} and the computer chose {Computers_Choice}")

if Users_Choice == Computers_Choice:
    print(f"Both players selected {Users_Choice}. It's a tie!")
elif Users_Choice == "rock":
    if Computers_Choice == "scissors":
        print("Rock beats scissors! You win!")
    else:
        print("Paper beats rock! You lose.")
elif Users_Choice == "paper":
    if Computers_Choice == "rock":
        print("Paper beats rock! You win!")
    else:
        print("Scissors beats paper! You lose.")
elif Users_Choice == "scissors":
    if Computers_Choice == "paper":
        print("Scissors beats paper! You win!")
    else:
        print("Rock betas scissors! You lose.")
elif Users_Choice != "rock, paper, scissors":
    print("invalid")