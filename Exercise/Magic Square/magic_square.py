################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Mar 28, 2021
# Description This program takes 3 by 3 matrix and determine whether it is a
# Lo Shu magic square or not.
################################################################################

# print_square: this function takes 3 by 3 dimensional list and print it in matrix form
def print_square(list: list):
    for row in range(len(list)):
        line: str = ""
        for column in range(len(list[row])):
            if column == len(list[row]) - 1:
                line = line + str(list[row][column])
            else:
                line = line + str(list[row][column]) + " "
        print(line)


# is_magic: this function takes 3 by 3 dimensional list and determine whether it is Lo Shu magic square or not.
# return True, if input list is Lo Shu magic square, False, if input list is not Lo Shu magic square.
def is_magic(inputList: list):
    result: bool = True
    sum: int = 0
    sumEachLine: int = 0
    numberList = list()
    for row in range(len(inputList)):
        for column in range(len(inputList[row])):
            for element in numberList:
                if inputList[row][column] == element:
                    return False
                else:
                    continue
            numberList.append(inputList[row][column])

    for row in range(len(inputList)):
        for column in range(len(inputList[row])):
            if row == 0:
                sum = sum + inputList[row][column]
                sumEachLine = sum
            else:
                sumEachLine = sumEachLine + inputList[row][column]
        if sumEachLine != sum:
            result = False
            return result
        else:
            sumEachLine = 0
            continue

    for column in range(len(inputList)):
        for row in range(len(inputList[column])):
            sumEachLine = sumEachLine + inputList[column][row]
        if sumEachLine != sum:
            result = False
            return result
        else:
            sumEachLine = 0
            continue

    for row in range(len(inputList)):
        sumEachLine = sumEachLine + inputList[row][row]
    if sumEachLine != sum:
        result = False
        return result
    else:
        sumEachLine = 0

    for index in range(3):
        sumEachLine = sumEachLine + inputList[index][2-index]
    if sumEachLine != sum:
        result = False
        return result
    else:
        return result


def main():
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    m3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

    for element in m1, m2, m3:
        print("Your square is:")
        print_square(element)
        if is_magic(element):
            print("It is a Lo Shu magic square!\n")
        else:
            print("It is not a Lo Shu magic square.\n")





if __name__ == '__main__':
    main()
