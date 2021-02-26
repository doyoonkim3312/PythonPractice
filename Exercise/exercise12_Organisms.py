################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: 02/14/2021
# Title: Exercise12 Organisms
# This program predicts the approximate size of a population of organisms.
################################################################################
startNumber = int(input("Starting number, in million: "))
rate = int(input("Average daily increase, in percent: "))
days = int(input("Number of days to multiply: "))
value = 0.0

print("Day" + "   Approx. Pop")
for index in range(0, days):
    dayFormatted = "{:>3}".format(index + 1)
    if index == 0:
        value = startNumber
        valueFormatted = "{:>14.4f}".format(value)
        print(dayFormatted + valueFormatted)
    else:
        value = value * (1 + (rate / 100))
        valueFormatted = "{:>14.4f}".format(value)
        print(dayFormatted + valueFormatted)
