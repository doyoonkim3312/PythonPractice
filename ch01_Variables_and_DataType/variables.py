# Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)

# String
message = "Hello World!"
print(message)

# String concatenation
message += ", Hello Python!"
personalGreeting = "hello Doyoon."
newMessage = "welcome to Python!"

print(message)
print(personalGreeting + newMessage)

# f-string ('f' stands for 'format')
# One way of concatenate strings by formatting them
fullGreeting = f"{personalGreeting} {newMessage.title()}"
print(fullGreeting)

firstName = "Doyoon"
lastName = "Kim"
fullName = f"{firstName} {lastName}"

# Another way of using f-string
fullName2 = "{} {}".format(firstName, lastName)

print(f"Hello, {fullName}. Welcome Back")
print(fullName2)

# Changin Case in a String with Methods

# title() method changes each word to title case.
# output will be "Welcome to Python"
print(newMessage.title())

# upper/lower cases
print(message.upper())
print(message.lower())

testString : str = message.upper()
isUpper : bool = testString.isupper()
print(isUpper)

# Adding Whitespace (Tap, newlines, etc.)
print("Languages:\nPython\n\tJava\nKotlin\Swift")

# Stripping Witespace: method called '.rstrip()' removes whitespaces.
language = "Python "

print(f"'{language}'")
print(f"'{language.rstrip()}'")

# Numeric
# Integer, Float, Underscored Numbers

int1 : int = 2
int2 : int = 5
underscored : int = 14_000_000_000

float1 : float = 7.0
float2 : float = 3.0

addition = int1 + int2
subtract =  int2 - int1
multiply = int1 * float2
division = float1 / float2

# Double forward slash: Result will be rounded down to closet integer.
division2 = float1 // float2
squared = float1 ** int1

# Multiple Assignment
x, y, z = 1, 2, 3

print(addition, subtract, multiply, division, squared)
print(x, y, z)

# CONSTANT (same as final in Java, Val in Kotlin/Swift)
# There's no keyword for constant value in Python, but all programmers use all captial letters to indicate a variable
# should be treated as a constant and never be changed.

SAMPLE_CONSTANT = 400000
