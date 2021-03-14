################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Mar 08, 2021
# Title: Exercise17 Prime List
# This program determine, and return all the prime numbers in specific range.
################################################################################

# This code will reuse is_prime function in exercise16_PrimeNumber.py.

def is_prime(num: int):
    if num == 1:
        return False
    for index in range(2, int(num ** 0.5) + 1):
        if num % index == 0:
            return False
    return True


def main():
    bound = int(input("Enter a positive integer: "))
    outputString: str = ""
    for number in range(2, bound + 1):
        if is_prime(number) and number == 2:
            outputString = outputString + f" {number}"
        elif is_prime(number) and number != 2:
            outputString = outputString + f", {number}"
        else:
            continue

    print(f"The primes up to {bound} are:{outputString}")


if __name__ == '__main__':
    main()