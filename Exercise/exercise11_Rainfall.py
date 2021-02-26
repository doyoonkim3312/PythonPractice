################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: 02/14/2021
# Title: Exercise11 Rainfall
# This program takes rainfall value of each month in year and calculate total
# value of rainfall, and calculate average value.
################################################################################

monthInYear = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
year = int(input("Enter the number of years: "))
totalFainFallValue = 0.0

if year <= 0:
    print("Invalid input.")
else:
    for i in range(0,year):
        print(f"  For year No. {i + 1}")
        for element in monthInYear:
            rainfallValue = float(input(f"    Enter the rainfall for {element}.: "))
            while True:
                if rainfallValue < 0:
                    print("    Invalid input, please try again.")
                    rainfallValue = float(input(f"    Enter the rainfall for {element}.: "))
                else:
                    totalFainFallValue += rainfallValue
                    break
    print(f"There are {year * 12} months.")
    print(f"The total rainfall is {totalFainFallValue:.2f}")
    print(f"The monthly average rainfall is {(totalFainFallValue / (year * 12 )):.2f}")