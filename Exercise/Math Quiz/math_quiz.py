###############################################################################
# Author: Doyoon Kim (kim3312@purdue.edu)
# Date: Mar 19, 2021
# Description This program generate simple math question about adding two digit
# number and three digit number.
###############################################################################

import random as random

def main():
    # Write your mainline logic here ------------------------------------------
    twoDigitNumber: int = random.randrange(10, 99)
    threeDigitNumber: int = random.randrange(100, 999)
    correctAnswer = twoDigitNumber + threeDigitNumber

    print(f"   {twoDigitNumber}")
    print(f"+ {threeDigitNumber}")
    print("-----")
    userAnswer = int(input("= "))

    if userAnswer == correctAnswer:
        print(f"Correct -- Good Work!")
    else:
        print(f"Incorrect. The correct answer is {correctAnswer}")



# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
