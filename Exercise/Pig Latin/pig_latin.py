################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 1, 2021
# Description: This program takes string and returns Pig Latin
################################################################################

# pig_latin: This function performs conversion of plaintext and Pig Latin.
def pig(input: str):
    FirstLetter: str = ""
    pigLainConverted: str = ""
    OutputString: list = list()
    for element in input.split():
        for index in range(len(element)):
            if index == 0:
                FirstLetter = element[index].lower()
            else:
                pigLainConverted = pigLainConverted + element[index].lower()
        OutputString.append(pigLainConverted + FirstLetter + "ay")
        pigLainConverted = ""
    OutputString[0] = OutputString[0].capitalize()
    return " ".join(OutputString)



def main():
    inputString = input("Enter a string: ")
    print(pig(inputString))


if __name__ == '__main__':
    main()
