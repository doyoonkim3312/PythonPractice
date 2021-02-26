################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: 02/14/2021
# Title: Exercise10 Sum Average
# This program takes series of non-negative number and calculates Sum and Average
################################################################################

# There are two ways to enable this functionality. One is store user input in Array, and another way is
# using while loop. To follow the concept of this week's lecture, I chose to use while loop.

numberOfInputValues = 0
sum : float = 0.0

while True:
    userInput = float(input("Enter a non-negative number (negative to quit): "))
    if userInput < 0:
        break
    else:
        numberOfInputValues += 1
        sum += userInput

if numberOfInputValues == 0:
    print("No input.")
else:
    print(f"Sum = {sum:.2f}")
    print(f"Average = {(sum / numberOfInputValues):.2f}")