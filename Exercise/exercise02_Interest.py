# Exercise 02 Interest
# Calculate a grand value that contains original deposit and its interest.
# Formula used: FV = P(1+r/n)^nt
# FV: Future Value means amount of money in the account after the specified number of years.
# P: Principal amount that was originally deposited into account.
# r: annual interest rate
# n: number of times per year that the interest is compounded.
# t: specified number of years.

print("Please enter the following quantities.")
initialDeposit = float(input("\tHow much is the initial deposit? "))
interestRate = float(input("\tWhat is the annual interest rate in percent ? ")) * 0.01
compoundedYears = int(input("\tHow many times per year is the interest compounded? "))
yearLeft = float(input("\tHow many years will the account be left to earn interest? "))

futureValue = initialDeposit * (1 + interestRate/compoundedYears)**(compoundedYears * yearLeft)
formattedValue = "{:,.2f}".format(futureValue)

print(f"At the end of {yearLeft}, the account will be worth ${formattedValue}.")
