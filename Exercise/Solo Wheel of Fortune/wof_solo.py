###############################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: May 9th, 2021 (EST)
# Description: This program provide hangman based phrase-guessing game based on
# the phrase list (phrase.txt)
###############################################################################
import random
import re

class Round:
    currentRound: int
    userEarning: int
    consonants: str = 'BCDFGHJKLMNPQRSTVWXYZ'
    vowels: str = 'AEIOU'
    phrase: str
    phraseConcealed: list

    def __init__(self, currentRound: int):
        self.currentRound = currentRound
        self.userEarning = 0
        with open('phrases.txt', 'r') as file:
            self.phrase = random.choice([line.rstrip('\n') for line in file]).upper()
        self.phraseConcealed = list(re.sub('[A-z]', '_', self.phrase))

    def letter_checking(self, letter: str):
        counter = 0

        for index in range(len(self.phrase)):
            if self.phrase[index] == letter:
                counter += 1
                self.phraseConcealed[index] = letter
            else:
                continue
        return counter

    def char_remaining(self, num: int):
        result: bool = False
        if num == 0:
            for char in self.consonants:
                if char != ' ':
                    result = True
                    break
        else:
            for char in self.vowels:
                if char != ' ':
                    result = True
                    break
        return result


def trial(r: Round):
    while True:
        print(f":::::::::::::::::::::::::::::::::::::::::: ROUND {r.currentRound} of 4 ::")
        print(f"::{''.join(r.phraseConcealed).center(54, ' ')}::")
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print(f"::{r.consonants.center(27, ' ')}::{r.vowels.center(11, ' ')}:"
              f":{('$' + format(r.userEarning, ',')).rjust(11, ' ')} ::")
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

        while True:
            print("What would you like to do?")
            print("  1 - Spin the wheel")
            print("  2 - Buy a vowel")
            print("  3 - Solve the puzzle")
            print("  4 - Quit the game")
            userChoice = input("Enter the number of your choice: ")

            try:
                userChoice = int(userChoice)
                if userChoice == 1:
                    if r.char_remaining(0):
                        result = spin_the_wheel(r)
                        if type(result) == str:
                            r.userEarning = 0
                        else:
                            r.userEarning += result
                    else:
                        print("There is no more consonants to choose.")
                elif userChoice == 2:
                    if r.char_remaining(1) and r.userEarning >= 250:
                        buy_a_vowel(r)
                    elif r.userEarning < 250:
                        print("You need at least $250 to buy a vowel.")
                    else:
                        print("There is no more vowels to choose.")
                elif userChoice == 3:
                    return solve_the_puzzle(r)
                else:
                    return quit_game(r)
                break
            except ValueError:
                print(f"{userChoice} is an invalid choice.")


# spin_the_wheel()
    # This function returns at random a value from a virtual wheel that contains the following 21 spaces.
    # five $500, one $550, four $600, three $650, three $700, one $800, one $900, one $2,500, and two Bankrupt.
    # Cash value should be returned as a number
    # 'bankrupt' should be returned as a string, player's cash earnings for the round are set to zero and the turn ends.
def spin_the_wheel(r: round):
    wheel: list = [500, 500, 500, 500, 500, 550, 600, 600, 600, 600, 650, 650, 650, 700, 700, 700, 800, 900,
                   2500, "Bankrupt", "Bankrupt"]
    wheelValue = random.choice(wheel)
    if wheelValue == 'Bankrupt':
        print(f"The wheel landed on BANKRUPT.")
        print(f"You lost ${format(r.userEarning, ',')}!")
        return 'Bankrupt'
    else:
        print(f"The wheel landed on ${wheelValue}.")
        while True:
            userChoice = input("Pick a consonant: ").upper()
            try:
                float(userChoice)
                int(userChoice)
                print(f"The character {userChoice} is not a letter.")
            except ValueError:
                if len(userChoice) > 1:
                    print("Please enter exactly one character.")
                else:
                    if userChoice in r.vowels:
                        print("Vowels must be purchased.")
                    else:
                        if userChoice in r.consonants:
                            if userChoice in r.phrase:
                                r.consonants = r.consonants.replace(userChoice, ' ')
                                letterCount = r.letter_checking(userChoice)
                                if letterCount > 1:
                                    print(f"There is {letterCount} {userChoice}'s, which earns you "
                                          f"${format((wheelValue * letterCount), ',')}")
                                else:
                                    print(f"There is {letterCount} {userChoice}, which earns you "
                                          f"${format((wheelValue * letterCount), ',')}")
                                return wheelValue * letterCount
                            else:
                                print(f"I'm sorry, there are no {userChoice}'s.")
                                r.consonants = r.consonants.replace(userChoice, ' ')
                                return 0
                        else:
                            print(f"The letter {userChoice} has already been used.")


def buy_a_vowel(r: Round):
    while True:
        userChoice = input("Pick a vowel: ").upper()
        try:
            int(userChoice)
            print(f"The character {userChoice} is not a letter.")
        except ValueError:
            if len(userChoice) > 1:
                print("Please enter exactly one character.")
            else:
                if userChoice in r.consonants:
                    print("Consonants cannot be purchased.")
                else:
                    if userChoice in r.vowels:
                        if userChoice in r.phrase:
                            letterCount = r.letter_checking(userChoice)
                            if letterCount > 1:
                                print(f"There is {letterCount} {userChoice}'s.")
                            else:
                                print(f"There is {letterCount} {userChoice}.")
                        else:
                            print(f"I'm sorry, there are no {userChoice}'s.")

                        r.vowels = r.vowels.replace(userChoice, ' ')
                        r.userEarning -= 250
                        break
                    else:
                        print(f"The letter {userChoice} has already been used.")


def solve_the_puzzle(r: Round):
    print("Solve the puzzle")
    print("Enter your solution")
    print(f"  Clues: {''.join(r.phraseConcealed)}")
    userGuess = input("  Guess: ").upper()
    if userGuess == r.phrase:
        print("Ladies and gentlemen, we have winner!")
        if r.userEarning < 1000:
            r.userEarning = 1000
        print(f"You earned ${format(r.userEarning, ',')} this round.")
    else:
        r.userEarning = 0
        print("I'm sorry. The correct solution was:")
        print(r.phrase)
        print(f"You earned ${format(r.userEarning, ',')} this round.")
    return r.userEarning


def quit_game(r: Round):
    r.userEarning = 0
    print(f"You earned ${format(r.userEarning, ',')} this round.")
    return True



def main():
    totalEarning: int = 0

    for roundNumber in range(1,5):
        round: Round = Round(roundNumber)
        result = trial(round)
        if type(result) == bool:
            break
        else:
            totalEarning += result

    print("Thanks for playing!")
    print(f"You earned a total of ${format(totalEarning, ',')}.")



if __name__ == '__main__':
    main()