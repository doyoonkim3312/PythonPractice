################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Mar 28, 2021
# Description This program takes numbes and
################################################################################

def print_square(list: list):
    print("Your square is:")
    for row in range(len(list)):
        line: str = ""
        for column in range(len(list[row])):
            if column == len(list[row]) - 1:
                line = line + str(list[row][column])
            else:
                line = line + str(list[row][column]) + " "
        print(line)


def is_magic(list: list):
    result: bool = True
    sum: int = 0
    sumEachLine: int = 0
    for row in range(len(list)):
        for column in range(len(list[row])):
            if row == 0:
                sum = sum + list[row][column]
                sumEachLine = sum
            else:
                sumEachLine = sumEachLine + list[row][column]
        if sumEachLine != sum:
            print(f"1: False: {sumEachLine} is not equal to {sum}")
            result = False
            return result
        else:
            sumEachLine = 0
            continue

    for column in range(len(list)):
        for row in range(len(list(column))):
            sumEachLine = sumEachLine + list[column][row]
        if sumEachLine != sum:
            print(f"2: False: {sumEachLine} is not equal to {sum}")
            result = False
            return result
        else:
            sumEachLine = 0
            continue

    for row in range(len(list)):
        sumEachLine = sumEachLine + list[row][row]
    if sumEachLine !=sumEachLine:
        print(f"3: False: {sumEachLine} is not equal to {sum}")
        result = False
        return result
    else:
        return result

def main():

    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    m3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

    print_square(m3)
    print(f"result: {is_magic(m1)}")

    
if __name__ == '__main__':
    main()
