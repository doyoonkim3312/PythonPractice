################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Mar. 27, 2021
# Description: This program takes first list and generate second list which
# contains all the elements from first list that is multiples of 7
################################################################################

def multiples_of(number, numberList: list):
    outputList: list = list()
    for element in numberList:
        if element % number == 0:
            outputList.append(element)
        else:
            continue
    return outputList


def main():

    number_list = [19, 2940, -189, 10, 28, -58, 1, 85, 201, -15, 122, 799, 406]
    print(f"Original list of numbers:\n{number_list}")
    print(f"Numbers in the list that are multiples of 7:\n{multiples_of(7, number_list)}")


if __name__ == '__main__':
    main()
