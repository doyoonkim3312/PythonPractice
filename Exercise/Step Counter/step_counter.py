################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 3, 2021
# Description This program reads file that stores all steps information in daily
# bases, and analyzes those information in month bases
################################################################################
    
def main():
    try:
        stepDatabase = open('steps.txt', 'r')
        dailySteps = stepDatabase.read()
    except OSError:
        print("Error: Unable to read the file. Program cannot locate the file")
        exit()

    monthCounter, dayCounter, monthlySum, monthlyAverage = 1, 0, 0, 0
    monthlySteps: list = list()
    names: list = ["January", "February", "March", "April", "May", "June", "July", "August",
                       "September", "October", "November", "December"]

    for steps in dailySteps.split("\n"):
        dayCounter = dayCounter + 1
        monthlySum = monthlySum + int(steps)

        if monthCounter < 8:
            if dayCounter == 31 and (monthCounter % 2) == 1:
                monthlySteps.append(monthlySum / 31)
                dayCounter = 0
                monthlySum = 0
                monthCounter = monthCounter + 1
            elif dayCounter == 30 and (monthCounter % 2) == 0:
                monthlySteps.append(monthlySum / 30)
                dayCounter = 0
                monthlySum = 0
                monthCounter = monthCounter + 1
            elif dayCounter == 28 and monthCounter == 2:
                monthlySteps.append(monthlySum / 28)
                dayCounter = 0
                monthlySum = 0
                monthCounter = monthCounter + 1
        else:
            if dayCounter == 31 and (monthCounter % 2) == 0:
                monthlySteps.append(monthlySum / 31)
                dayCounter = 0
                monthlySum = 0
                monthCounter = monthCounter + 1
            elif dayCounter == 30 and (monthCounter % 2) == 1:
                monthlySteps.append(monthlySum / 30)
                dayCounter = 0
                monthlySum = 0
                monthCounter = monthCounter + 1

    print("The average steps taken each month were:")
    for index in range(len(monthlySteps)):
        print(f"{names[index]:>10} : {monthlySteps[index]:.1f}")




if __name__ == '__main__':
    main()
