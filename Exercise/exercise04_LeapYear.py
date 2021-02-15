################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: 02/14/2021
# Title: Exercise04: Leap Year
# This program determines whether input year is leap year or not.
################################################################################

inputYear = int(input("Please input a year: "))

if inputYear % 100 == 0 :
    if inputYear % 400 == 0 :
        print(f"In the year {inputYear}, there are 29 days in February.")   #Leap Year
    else :
        print(f"In the year {inputYear}, there are 28 days in February.")
else :
    if inputYear % 4 == 0 :
        print(f"In the year {inputYear}, there are 29 days in February.")   #leap Year
    else :
        print(f"In the year {inputYear}, there are 28 days in February.")

