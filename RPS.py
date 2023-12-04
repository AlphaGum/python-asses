import random

options = ["rock","paper","scissors"] #arrary to store the options 
Users_Choice = input("choose and option between rock paper and scissors: ")# findind the users choice

Computers_Choice = random.choice(options) #randomising the computers choice
print(f"you chose {Users_Choice} and the computer chose {Computers_Choice}")

def gamelogic():
    if Users_Choice == Computers_Choice:  #if your choice is the same as the computers print a tie 
            print(f"Both players selected {Users_Choice}. It's a tie!")
    elif Users_Choice == "rock": #if this is your choice 
            
            if Computers_Choice == "scissors": #and this is the computers choice
                print("Rock beats scissors! You win!")#print this or
            else:
                print("Paper beats rock! You lose.")#print this
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
    elif Users_Choice != "rock, paper, scissors":#if the users choice is not rock paper or scissors print invlaid and end the program
        print("invalid")
print (gamelogic())