################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 5, 2021
# Description This program generate capital quiz based on data in state)capitals.txt
################################################################################
import random as random

def get_state_data():
    outputDict = {}
    inputFile = open('state_capitals.txt','r')
    stateData = inputFile.read()
    inputFile.close()

    for line in stateData.split('\n'):
        try:
            keyValue: list = line.split(", ")
            outputDict[keyValue[1]] = keyValue[0]
        except IndexError:
            continue
    return outputDict


def main():
    stateData = get_state_data()
    stateList = list(stateData.keys())
    random.shuffle(stateList)

    numberTotal = len(stateList)
    numberCorrect, numberQuestion = 0, 0
    while numberQuestion < numberTotal:
        answer = input(f"What is the capital of {stateList[numberQuestion]} (enter 0 to quit)? ")
        if answer == str(0):
            break
        else:
            if answer.lower() == str(stateData[stateList[numberQuestion]]).lower():
                print("This is correct!")
                numberCorrect = numberCorrect + 1
            else:
                print(f"This is incorrect.\nThe capital of {stateList[numberQuestion]} is "
                      f"{stateData[stateList[numberQuestion]]}")
            numberQuestion = numberQuestion + 1
    print(f"You answered {numberCorrect} out of {numberQuestion} questions")



if __name__ == '__main__':
    main()
