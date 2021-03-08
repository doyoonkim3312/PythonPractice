################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Mar 08, 2021
# Title: Exercise13 Falling
# This program calculates its travel distance due to gravity.
################################################################################

# d = 1/2gt^2

def falling_distance(time):
    # this function calculates falling distance through 1 second to 10 second.
    return 0.5 * 9.81 * (time ** 2)

def main():
    # Write your 'mainline logic' here
    print("Time (s)  Distance (m)")
    print("----------------------")
    for index in range(0, 10):
        timeFormatted = "{:>8}".format(index + 1)
        valueFormatted = "{:>14.2f}".format(falling_distance(index + 1))
        print(timeFormatted + valueFormatted)


if __name__ == '__main__':
    main()