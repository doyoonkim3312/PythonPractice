################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 3, 2021
# Description This program read random numbers from random_numbers.txt created
# in Exercise 33, and analyze the numbers in file.
################################################################################

def main():
    try:
        inputFile = open('../Number Writer/random_numbers.txt', 'r')
        numbers = inputFile.read()
    except OSError:
        print("Error: Unable to read file. Program cannot locate the file.")
        exit()

    maxNumber, minNumber, totalNumbers, sum = 0, 0, 0, 0
    for number in numbers.split("\n"):
        totalNumbers = totalNumbers + 1
        sum = sum + int(number)

        if totalNumbers == 1:
            maxNumber, minNumber = int(number), int(number)
        else:
            if int(number) > maxNumber:
                maxNumber = int(number)
            if int(number) < minNumber:
                minNumber = int(number)

    print(f"{totalNumbers:0,} numbers were read from the file.")
    print(f"Max: {maxNumber}")
    print(f"Min: {minNumber}")
    print(f"Sum: {sum:0,}")
    print(f"Avg: {sum / totalNumbers:.1f}")


if __name__ == '__main__':
    main()
