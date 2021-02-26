################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: 02/14/2021
# Title: Exercise09 Hash Pattern
# This program takes number of line and print two # with increasing spaces between them
################################################################################

numberOfLines : int = int(input("Enter the number of lines: "))
index = 0
lineOutput : str = ""

while index < numberOfLines :
    lineOutput = "#"
    for n in range(0, index) :
        lineOutput += " "
        n += 1
    lineOutput += "#"
    print(lineOutput)
    index += 1
