################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: 02/14/2021
# Title: Exercise06 Roulette Colors
# This program determines color of pocket in Roulette.
################################################################################

targetPocket = int(input("Please enter a pocket number: "))
pocketColor : str

if targetPocket == 0 :
    pocketColor = "green"
elif 1 <= targetPocket <= 10 or 19 <= targetPocket <= 28:
    if targetPocket % 2 == 0 :
        pocketColor = "black"
    else :
        pocketColor = "red"
elif 11 <= targetPocket <= 18 or 29 <= targetPocket <= 36 :
    if targetPocket % 2 == 0:
        pocketColor = "red"
    else:
        pocketColor = "black"
else :
    pocketColor = "Invalid Input!"

print(f"  Pocket {targetPocket} is {pocketColor}.")