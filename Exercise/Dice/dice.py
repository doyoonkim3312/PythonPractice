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
        print(f"Rolling a {self.sides} sided die {numberOfRoll} times: {', '.join(outputList)}")


def main():
    # Instantiate Dice object
    sixSideDice: Dice = Dice(6)
    tenSideDice: Dice = Dice(10)
    twentySideDice: Dice = Dice(20)

    sixSideDice.n_rolls(10)
    tenSideDice.n_rolls(10)
    twentySideDice.n_rolls(10)


if __name__ == '__main__':
    main()
