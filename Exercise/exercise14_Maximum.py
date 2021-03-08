################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Mar 08, 2021
# Title: Exercise14 Maximum
# This program determine greater value between given two integers using defined
# function
################################################################################

#

def max_of_two(num1: int, num2: int):
    if num1 > num2:
        return num1
    else:
        return num2

def main():
    # Write your 'mainline logic' here
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    print(f"{max_of_two(num1, num2)} is greater.")

if __name__ == '__main__':
    main()