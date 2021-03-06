################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 3, 2021
# Description This program takes .txt file and count total words and lines in
# input file.
################################################################################
    
def main():
    inputFile = open('rumpelstiltskin.txt', 'r')
    contents = inputFile.read()
    inputFile.close()
    lineCount, wordCount = 0, 0

    for line in contents.split("\n"):
        lineCount = lineCount + 1
        if len(line) != 0:
            wordCount = wordCount + len(line.split())
    # The line below deletes empty line added by editor.
    lineCount = lineCount - 1

    print(f"Total number of words: {wordCount}")
    print(f"Total number of lines: {lineCount}")
    print(f"Average number of words per line: {wordCount / lineCount:.1f}")


if __name__ == '__main__':
    main()
