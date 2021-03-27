################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Mar. 27, 2021
# Description: This program collects 10 floating point numbers from user and
# calculates lowest value, highest value, total sum, and average value.
################################################################################

def get_number_list():
    outputList: list = list()
    for index in range(10):
        while True:
            number = input(f"  Enter number {index + 1} of 10: ")
            try:
                number = float(number)
                break
            except ValueError:
                continue
        outputList.append(number)
    return outputList



def main():
    targetList: list = get_number_list()
    targetList.sort()

    lowest = targetList[0]
    highest = targetList[len(targetList) - 1]
    total: float = 0
    average: float

    for element in targetList:
        total = total + element

    average = total / len(targetList)

    print(f"Lowest Number: {lowest:.2f}")
    print(f"Highest Number: {highest:.2f}")
    print(f"Total: {total:.2f}")
    print(f"Average: {average:.2f}")


if __name__ == '__main__':
    main()
