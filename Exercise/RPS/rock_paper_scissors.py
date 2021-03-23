###############################################################################
# Author: Doyoon Kim (kim3312@purdue.edu)
# Date: Mar 19, 2021
# Description This program offers Rock Paper Scissor game with computer
###############################################################################

import random as random

def main():
    # Write your mainline logic here ------------------------------------------
    while True:
        computerChoice: str = get_computer_choice()

        userChoice: str = get_player_choice()

        print(f"  The computer chose {computerChoice}, and you chose {userChoice}.")
        gameResult: str = get_winner(computerChoice, userChoice)

        if gameResult == "tie":
            print(f"  Its a {gameResult}. Starting over.\n")
            continue
        else:
            if gameResult == "computer":
                print(f"  {computerChoice} beats {userChoice}")
                print(f"  You lost.  Better luck next time.")
            else:
                print(f"  {userChoice} beats {computerChoice}")
                print(f"  You won the game!")
            print("Thanks for playing.")
            break


def get_winner(computerChoice: str, userChoice: str):
    if computerChoice == "rock":
        if userChoice == "paper":
            return "player"
        elif userChoice == "scissors":
            return "computer"
        else:
            return "tie"
    elif computerChoice == "scissors":
        if userChoice == "rock":
            return "player"
        elif userChoice == "paper":
            return "computer"
        else:
            return "tie"
    else:
        if userChoice == "rock":
            return "computer"
        elif userChoice == "scissors":
            return "player"
        else:
            return "tie"


def get_computer_choice():
    choices = ["rock", "scissors", "paper"]
    return random.choice(choices)


def get_player_choice():
    while True:
        userChoice: str = input("Choose rock, paper, or scissors: ")

        if (userChoice == "rock" or userChoice == "paper" or userChoice == "scissors"):
            return userChoice
        else:
            print("You made an invalid choice. Please try again.")
            continue


# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
