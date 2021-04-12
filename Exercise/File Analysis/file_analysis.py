################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu)
# Date: Apr 11, 2021
# Description This program takes two files and perform 3 types of analysis,
# including frequency check, common word check and eitherButNotBoth word check.
# All frequency check, common word check and eitherButNotBoth check uses modified
# word list that removes repeated element using set() type value.
# All Result will be store in specific file that corresponding to each test case.
################################################################################
import string

# load_files(filename: str) this function takes filename and return list of all words in certain file.
def load_files(filename: str):
    openedFile = open(filename, 'r')
    file = openedFile.read()
    openedFile.close()
    outputList: list = list()

    for row in file.split("\n"):
        if row == "":
            continue
        else:
            for word in row.split(" "):
                # print(f"Test_{word}_test")
                if word != "":
                    outputList.append(word.strip(string.punctuation).lower())
    return outputList

# frequency_check: this function takes word from unique set and perform frequency check
def frequency_check(targetWords: list, totalWords: list):
    outputDict = {}
    wordCount = 0

    for targetWord in targetWords:
        for word in totalWords:
            if targetWord == word:
                wordCount = wordCount + 1
        outputDict[targetWord] = wordCount
        wordCount = 0

    return outputDict


def main():
    file1 = load_files('xian_1.txt')
    file2 = load_files('xian_2.txt')

    file1Unique = list(set(file1))
    file1Unique.sort()
    file1FrequencyResult = open('xian_1_word_frequency.txt', 'w')
    for item in frequency_check(file1Unique, file1).items():
        file1FrequencyResult.write(f"{item[0]}: {item[1]}\n")
    file1FrequencyResult.close()

    file2Unique = list(set(file2))
    file2Unique.sort()
    file2FrequencyResult = open('xian_2_word_frequency.txt', 'w')
    for item in frequency_check(file2Unique, file2).items():
        file2FrequencyResult.write(f"{item[0]}: {item[1]}\n")
    file2FrequencyResult.close()

    commonWords = list(set(file1).intersection(set(file2)))
    commonWords.sort()
    fileCommonWord = open('common_words.txt', 'w')
    for word in commonWords:
        fileCommonWord.write(f"{word}\n")
    fileCommonWord.close()

    eitherButNotBoth = list(set(file1).symmetric_difference(set(file2)))
    eitherButNotBoth.sort()
    fileEitherButNotBoth = open('eitherbutnotboth.txt', 'w')
    for word in eitherButNotBoth:
        fileEitherButNotBoth.write(f"{word}\n")
    fileEitherButNotBoth.close()



if __name__ == '__main__':
    main()
