################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Mar 08, 2021
# Title: Exercise16 Prime Numbers
# This program determine whether input value is prime or not.
################################################################################

# 1 is not a prime number. 2, 3 is a prime number. Among the other values, one that is divided by either 2 or 3 is not
# a prime number.
# knownPrimes: list = [1, 2, 3, 5]

def is_prime(num: int):
    if num == 1:
        return False
    for index in range(2, int(num ** 0.5) + 1):
        if num % index == 0:
            return False
    return True


def main():
    while True:
        integer = int(input("Enter a positive integer (-1 to quit): "))
        if integer == -1:
            break
        else:
            if is_prime(integer):
                print(f"{integer} is a prime number.")
            else:
                print(f"{integer} is not a prime number.")



if __name__ == '__main__':
    main()