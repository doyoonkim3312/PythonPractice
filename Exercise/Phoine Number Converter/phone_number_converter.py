################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 2, 2021
# Description This program takes telephone number with alphabets and reverts
# those alphabets to their original assigned numeric values.
################################################################################

# convert_number: This function takes string type telephone number with alphabets and reverts alphabets to numeric value
def convert_number(number: str):
    numberOutput: list = list()
    convertedValue: str = ""
    for element in number.split("-"):
        try:
            int(element)
            numberOutput.append(element)
        except ValueError:
            for index in range(len(element)):
                try:
                    int(element[index])
                    convertedValue = convertedValue + str(element[index])
                except ValueError:
                    if element[index].upper() == 'A' or element[index].upper() == 'B' or element[index].upper() == 'C':
                        convertedValue = convertedValue + "2"
                    elif element[index].upper() == 'D' or element[index].upper() == 'E' or element[
                        index].upper() == 'F':
                        convertedValue = convertedValue + "3"
                    elif element[index].upper() == 'G' or element[index].upper() == 'H' or element[
                        index].upper() == 'I':
                        convertedValue = convertedValue + "4"
                    elif element[index].upper() == 'J' or element[index].upper() == 'K' or element[
                        index].upper() == 'L':
                        convertedValue = convertedValue + "5"
                    elif element[index].upper() == 'M' or element[index].upper() == 'N' or element[
                        index].upper() == 'O':
                        convertedValue = convertedValue + "6"
                    elif element[index].upper() == 'P' or element[index].upper() == 'Q' or element[
                        index].upper() == 'R' or \
                            element[index].upper() == 'S':
                        convertedValue = convertedValue + "7"
                    elif element[index].upper() == 'T' or element[index].upper() == 'U' or element[
                        index].upper() == 'V':
                        convertedValue = convertedValue + "8"
                    else:
                        convertedValue = convertedValue + "9"
            numberOutput.append(convertedValue)
            convertedValue = ""
    return "-".join(numberOutput)



def main():
    userInput = input("Enter a telephone number: ")
    print(f"The phone number is {convert_number(userInput)}")



if __name__ == '__main__':
    main()