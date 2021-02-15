# 48 cookies:
# Calculates total number of cookies can be made based on ingredients for 48 cookies.
# 1.5 coups of sugar, 1 cup of butter, 2.75 cups of flour.

amountOfCookies = int(input("How many cookies do you want to make? "))

STANDARD_SUGAR = 1.50
STANDARD_BUTTER = 1.00
STANDARD_FLOUR = 2.75
STANDARD_COOKIES = 48

sugarNeeded = STANDARD_SUGAR * (amountOfCookies / STANDARD_COOKIES)
butterNeeded = STANDARD_BUTTER * (amountOfCookies / STANDARD_COOKIES)
flourNeeded = STANDARD_FLOUR * (amountOfCookies / STANDARD_COOKIES)

print(f"To make {amountOfCookies} cookies, you will need: ")
print(f"\t{sugarNeeded:.2f} cups of sugar")
print(f"\t{butterNeeded:.2f} cups of butter")
print(f"\t{flourNeeded:.2f} cups of flour")
