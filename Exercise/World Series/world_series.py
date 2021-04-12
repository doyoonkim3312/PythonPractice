################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu)
# Date: Apr 11, 2021
# Description This program takes World Series data .txt file and return proper
# information that matches with user input year.
################################################################################

def load_winners_data():
    inputFile = open('WorldSeriesWinners.txt', 'r')
    rawList = inputFile.read().split("\n")

    teamWinningYear = {}
    year = 1903
    for team in rawList:
        if year == 1904 or year == 1994:
            teamWinningYear[year] = "not played"
        elif team == "":
            break
        else:
            teamWinningYear[year] = team
        year = year + 1

    rawList.sort()
    rawList.pop(0)
    winningDict = {}
    winningCount = 0
    currentTeam = ""
    for team in rawList:
        if winningCount == 0:
            currentTeam = team
            winningCount = winningCount + 1
        else:
            if currentTeam != team:
                winningDict[currentTeam] = winningCount
                currentTeam = team
                winningCount = 1
            else:
                winningCount = winningCount + 1

    return (teamWinningYear, winningDict)


def main():
    teamWinningByYear, teamWinningCount = load_winners_data()

    userInput = int(input("Enter a year in the range 1903 -- 2020: "))
    if userInput == 1904 or userInput == 1994:
        print(f"The World Series wasn't played in the year {userInput}")
    else:
        print(f"The {teamWinningByYear.get(userInput)} won the World Series in {userInput}")
        print(f"They have won the World Series {teamWinningCount.get(teamWinningByYear.get(userInput))}")


if __name__ == '__main__':
    main()
