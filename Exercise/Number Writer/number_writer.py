################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 3, 2021
# Description This program takes total number of random number to be generated,
# and write generated random number to result.txt file
################################################################################

import random as random

def main():
    userInput = int(input("Enter the number of random numbers to be written to the file: "))

    try:
        outputFile = open("random_numbers.txt", 'w')
    except OSError:
        print("Failed to create files")
        exit()

    for index in range(userInput):
        if index == userInput - 1:
            outputFile.write(str(random.randint(1, 500)))
        else:
            outputFile.write(str(random.randint(1, 500)) + "\n")

    outputFile.close()



if __name__ == '__main__':
    main()
