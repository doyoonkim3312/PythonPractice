# Collect Input
languageName = input("Enter your favorite language name: ")

# Standard output print
print(f"Oh! your favorite language is: {languageName}!")

# multiple arguments can be passed to print() method.
# sep= keyword can be used to determine how to separate each arguments when they are printed.
# end= keyword can be used to determine how to end print() method.

# Code below has a output of 'a b c' and starts newline
print('a', 'b', 'c', sep=" ", end="\n")

# format() method: format() method takes two arguments, a number, and a format specifier.
# returns a formatted number as a string
# Basic form of a format specifier: [width] pgrouping_option] [.precision] [type]
# width: the minimum total length of string
# grouping_option: a character to use when grouping digits
# .precision: the number of digits after the decimal point
# type use 'd' for integers, 'f' for floats, '%' for percentage

# Code below has a output of '12345.68'
print(format(12345.6789, '.2f'))

# Example codes
price = float(input("Enter the item's price: "))
numOfItems = float(input("How many items: "))
totalPrice = price * numOfItems
print("The total price is $", format(totalPrice, '.2f'), '.', sep="")

# print() code above also can be declared like below:
# {variableName:formatSpecifier)
print(f"The total price is ${totalPrice:.2f}.")

print(f"Format specifier test: {1234567:,d}")
