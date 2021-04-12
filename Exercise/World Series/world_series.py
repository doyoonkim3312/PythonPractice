################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu)
# Date: Apr 11, 2021
# Description This program takes World Series data .txt file and return proper
# information that matches with user input year.
################################################################################

def load_winners_data():
    inputFile = open('WorldSeriesWinners.txt', 'r')
    rawList = inputFile.read().split("\n")
    inputFile.close()

    teamList = list()
    for team in rawList:
        if team not in teamList:
            teamList.append(team)
    teamList.pop(len(teamList) - 1)

    winningNumber = {}
    for team in teamList:
        winningNumber[team] = rawList.count(team)

    yearDirct = {}
    listIndex = 0
    year = 1903
    while year < 2021:
        if year == 1904 or year == 1994:
            year = year + 1
        elif rawList[listIndex] == "":
            break
        else:
            yearDirct[year] = rawList[listIndex]
            year = year + 1
            listIndex = listIndex + 1

    return winningNumber, yearDirct


def main():
    winning, teamByYear = load_winners_data()
    userInput = int(input("Enter a year in the range 1903 -- 2020: "))
    if 1903 <= userInput <= 2020:
        if userInput == 1904 or userInput == 1994:
            print(f"The World Series wasn't played in the year {userInput}.")
        else:
            print(f"The {teamByYear.get(userInput)} won the World Series in {userInput}.")
            print(f"They have won the World Series {winning.get(teamByYear.get(userInput))} times.")
    else:
        print(f"Data for the year {userInput} is not included in this system.")


if __name__ == '__main__':
    main()
