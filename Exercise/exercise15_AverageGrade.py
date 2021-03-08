################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Mar 08, 2021
# Title: Exercise15 Average Grade
# This program determine letter grade for each entered scores, and calculates
# average score
################################################################################

def get_valid_score():
    while True:
        score = float(input("Enter a score: "))
        if score < 0 or score > 100:
            print("Invalid Input. Please try again.")
        else:
            return score


def calc_average(scoreList):
    sumOfScore = 0
    counter = 0
    for score in scoreList:
        counter = counter + 1
        sumOfScore = sumOfScore + score

    return sumOfScore / counter


def determine_grade(score: float):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'


def main():
    scoreList: list = []
    for _ in range(0,5):
        score = get_valid_score()
        scoreList.append(score)
        print(f"The letter grade for {score} is {determine_grade(score)}.")

    print(f"The average score is {calc_average(scoreList):.2f}.")


if __name__ == '__main__':
    main()
