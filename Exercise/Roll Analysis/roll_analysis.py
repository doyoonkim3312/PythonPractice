################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Mar. 28, 2021
# Description This program analyzes result of two six sided dice in certain
# numbers of roll
################################################################################
import random as random

# roll_d6(): This function generates return random integer in range from 1 to 6
def roll_d6():
    return random.randint(1,6)


# get_2d6_rolls(rolls: int): This function takes total number of rolls and calculates integer value result of tow six
# sided dice.
def get_2d6_rolls(rolls: int):
    result: list = list()
    for _ in range(rolls):
        result.append(roll_d6() + roll_d6())
    return result



def main():
    ROLLS: int = 900000

    result = get_2d6_rolls(ROLLS)
    result.sort()
    index = 0
    count = 0

    print("Roll" + "  Frequency")
    for number in range(2, 13):
        numberFormatted = "{:>3}".format(number)
        while True:
            try:
                if result[index] == number:
                    count = count + 1
                    index = index + 1
                else:
                    analysisFormatted = "{:>9.2f}".format(count / ROLLS * 100)
                    count = 0
                    break
            except IndexError:
                analysisFormatted = "{:>9.2f}".format(count / ROLLS * 100)
                break
        print(numberFormatted + analysisFormatted + "%")



if __name__ == '__main__':
    main()
