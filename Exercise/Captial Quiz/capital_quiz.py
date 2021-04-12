################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 5, 2021
# Description This program generate capital quiz based on data in state)capitals.txt.
# state_capitals.txt will be stored as a key-value pair dictionary.
################################################################################
import random as random
# random module is imported in order to add random factor to the order of question.

# get_state_data() This function open database file and store values in key-value pair dictionary.
def get_state_data():
    outputDict = {}
    # inputFile = open('state_capitals.txt','r')
    inputFile = open('state_capitals.txt', 'r')
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
    numberCorrect, numberQuestion = 0, 0

    while 0 < len(stateList):
        questionKey = random.choice(stateList)
        answer = input(f"What is the capital of {questionKey} (enter 0 to quit)? ")
        if answer == "0":
            break
        else:
            if answer.lower() == str(stateData[questionKey]).lower():
                print("That is correct!")
                stateList.remove(questionKey)
                numberCorrect = numberCorrect + 1
            else:
                print(f"That is incorrect.\nThe capital of {questionKey} is "
                      f"{stateData[questionKey]}.")
            numberQuestion = numberQuestion + 1
    print(f"You answered {numberCorrect} out of {numberQuestion} questions correctly.")




if __name__ == '__main__':
    main()
