################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: 02/14/2021
# Title: Exercise04: Software Sales
# This program calculates final price of software after applying appropriate
# discount rate based on order quantity
################################################################################

PRICE = 99.00
orderQuantity = int(input("Please input the number of packages to be purchased: "))
finalPrice : float
discountRate : str

if 0 <= orderQuantity :
    if 10 <= orderQuantity <= 19:
        discountRate = "10%"
        finalPrice = orderQuantity * PRICE * 0.9
    elif 20 <= orderQuantity <= 49:
        discountRate = "25%"
        finalPrice = orderQuantity * PRICE * 0.75
    elif 50 <= orderQuantity <= 99:
        discountRate = "35%"
        finalPrice = orderQuantity * PRICE * 0.65
    elif 100 <= orderQuantity:
        discountRate = "45%"
        finalPrice = orderQuantity * PRICE * 0.55
    elif 0 <= orderQuantity <= 9:
        discountRate = "No"
        finalPrice = orderQuantity * PRICE

    finalPrice = "{:0,.2f}".format(finalPrice)
    print(f"  {discountRate} discount applied")
    print(f"  The final price for purchasing {orderQuantity} packages is ${finalPrice}.")
else :
    print(f"  Invalid Input!")
