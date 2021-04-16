################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 15, 2021
# Description This program uses Dice object and simulates test roll using Dice
# object. Result will be printed in certain format using print_result() function
################################################################################

import random

class Dice:
    sides: int

    # Default Constructor
    def __init__(self, sides: int):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

    def n_rolls(self, numberOfRoll: int):
        outputList: list = list()
        for _ in range(numberOfRoll):
            outputList.append(str(self.roll()))
        return outputList


def main():
    # Instantiate Dice object
    sixSideDice: Dice = Dice(6)
    tenSideDice: Dice = Dice(10)
    twentySideDice: Dice = Dice(20)

    print_result(sixSideDice, 10)
    print_result(tenSideDice, 10)
    print_result(twentySideDice, 10)


def print_result(dice: Dice, numberRolled: int):
    print(f"Rolling a {dice.sides} sided die {numberRolled} times: {', '.join(dice.n_rolls(numberRolled))}")


if __name__ == '__main__':
    main()
