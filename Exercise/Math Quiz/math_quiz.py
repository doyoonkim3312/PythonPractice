###############################################################################
# Author: Doyoon Kim (kim3312@purdue.edu)
# Date: Mar 19, 2021
# Description This program generate simple math question about adding two digit
# number and three digit number.
###############################################################################

import random as random

def main():
    # Write your mainline logic here ------------------------------------------
    twoDigitNumber: int = random_number(2)
    threeDigitNumber: int = random_number(3)
    correctAnswer = twoDigitNumber + threeDigitNumber

    print(f"   {twoDigitNumber}")
    print(f"+ {threeDigitNumber}")
    print("-----")
    userAnswer = int(input("= "))

    if userAnswer == correctAnswer:
        print(f"Correct -- Good Work!")
    else:
        print(f"Incorrect. The correct answer is {correctAnswer}.")


def random_number(digits):
    if digits == 2:
        return random.randrange(10,100)
    elif digits == 3:
        return random.randrange(100,1000)


# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
