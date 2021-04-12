################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu)
# Date: Apr 11, 2021
# Description This program takes World Series data .txt file and return proper
# information that matches with user input year.
################################################################################

def load_winners_data():
    inputFile = open('WorldSeriesWinners.txt', 'r')
    rawList = inputFile.read().split("\n")

    outputDict = {}

    sortedList = rawList.copy()
    sortedList.sort()
    sortedList.pop(0)
    # winningDict = {}
    winningCount = 0
    currentTeam = ""
    for team in sortedList:
        if winningCount == 0:
            currentTeam = team
            winningCount = winningCount + 1
        else:
            if currentTeam != team:
                outputDict[currentTeam] = winningCount
                currentTeam = team
                winningCount = 1
            else:
                winningCount = winningCount + 1

    # teamWinningYear = {}
    listIndex = 0
    year = 1903
    while year < 2021:
        if year == 1904 or year == 1994:
            outputDict[year] = "not played"
            year = year + 1
        elif rawList[listIndex] == "":
            break
        else:
            outputDict[year] = rawList[listIndex]
            year = year + 1
            listIndex = listIndex + 1

    return outputDict


def main():
    # teamWinningByYear, teamWinningCount = load_winners_data()
    dataCollected = load_winners_data()
    userInput = int(input("Enter a year in the range 1903 -- 2020: "))
    if 1903 <= userInput <= 2020:
        if userInput == 1904 or userInput == 1994:
            print(f"The World Series wasn't played in the year {userInput}.")
        else:
            print(f"The {dataCollected.get(userInput)} won the World Series in {userInput}.")
            print(f"They have won the World Series {dataCollected.get(dataCollected.get(userInput))} times.")
    else:
        print(f"Data for the year {userInput} is not included in this system.")

if __name__ == '__main__':
    main()
