###############################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Mar 10, 2021
# Description This program counts total number of alphabet usage in phrases.txt
# file.
###############################################################################
import matplotlib.pyplot as plt
from string import ascii_letters

def read_file():
    alphabetList: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'
                          , 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    result: dict = {}
    counter = 0
    totalLetter = 0
    file = open('phrases.txt', 'r')
    phrases = file.read()
    file.close()

    for letter in alphabetList:
        for line in phrases.split("\n"):
            for char in line:
                if char in ascii_letters:
                    totalLetter += 1
                    if char.upper() == letter:
                        counter += 1
                    else:
                        continue
        result[letter] = counter
        counter = 0

    return result, totalLetter



def main():
    a, totalLetter = read_file()
    keys: list = a.keys()
    values: list = a.values()
    valuesModified: list = list()

    for value in values:
        valuesModified.append(value / totalLetter)

    fig, chart = plt.subplots()
    chart.set_title("Letter Frequency in Puzzle Phrases")
    chart.set_xlabel("Letter")
    chart.set_ylabel("Letter Appearance Frequency")

    chart.bar(keys, valuesModified)
    plt.savefig("wof_analysis.pdf")




if __name__ == '__main__':
    main()
    plt.show()
