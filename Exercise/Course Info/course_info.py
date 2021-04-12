################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu)
# Date: Apr 11, 2021
# Description This program takes course number from user and print proper course
# information.
################################################################################

def get_course_data():
    return {'CS101': {'room': '3004', 'instructor': 'Haynes', 'time': '8:00 a.m.'},
            'CS102': {'room': '4501', 'instructor': 'Alvarado', 'time': '9:00 a.m.'},
            'CS103': {'room': '6755', 'instructor': 'Rich', 'time': '10:00 a.m.'},
            'NT110': {'room': '1244', 'instructor': 'Burke', 'time': '11:00 a.m.'},
            'CM241': {'room': '1411', 'instructor': 'Lee', 'time': '1:00 p.m.'}}


def main():
    courseData = get_course_data()
    userInput = input("Enter a course number: ")
    targetCourse = courseData.get(userInput)

    if targetCourse is not None:
        print(f"The details for course {userInput} are:")
        print(f"{'Instructor':>12}: {courseData.get(userInput).get('instructor')}")
        print(f"{'Room':>12}: {courseData.get(userInput).get('room')}")
        print(f"{'Time':>12}: {courseData.get(userInput).get('time')}")
    else:
        print(f"{userInput} is an invalid course number.")

if __name__ == '__main__':
    main()
