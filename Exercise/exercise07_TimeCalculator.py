################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: 02/14/2021
# Title: Exercise07 Time Calculator
# This program convert input seconds into time format.
################################################################################
second : int
minute : int
hour : int
day : int

usrInput = int(input("Please enter a time in seconds. "))

if 60 <= usrInput < 3600 :
    minute = usrInput // 60
    second = usrInput % 60
    if second == 0 :
        print(f"  {usrInput:,} seconds is: {minute} minute(s).")
    else :
        print(f"  {usrInput:,} seconds is: {minute} minute(s) and {second} second(s).")
elif 3600 <= usrInput <86400 :
    hour = usrInput // 3600
    if 60 <= (usrInput % 3600) :
        minute = (usrInput % 3600) // 60
        second = (usrInput % 3600) % 60
        if second == 0 :
            print(f"  {usrInput:,} seconds is: {hour} hour(s) and {minute} minute(s).")
        else :
            print(f"  {usrInput:,} seconds is: {hour} hour(s), {minute} minute(s) and {second} second(s).")
    else :
        second = usrInput % 3600
        if second == 0 :
            print(f"  {usrInput:,} seconds is: {hour} hour(s).")
        else :
            print(f"  {usrInput:,} seconds is: {hour} hour(s) and {second} second(s).")
elif 86400 <= usrInput :
    day = usrInput // 86400
    if 3600 <= (usrInput % 86400) :
        hour = (usrInput % 86400) // 3600
        if 60 <= ((usrInput % 86400) % 3600) :
            minute = ((usrInput % 86400) % 3600) // 60
            second = ((usrInput % 86400) % 3600) % 60
            if second == 0 :
                print(f"  {usrInput:,} seconds is: {day} day(s), {hour} hour(s) and {minute} minute(s).")
            else :
                print(f"  {usrInput:,} seconds is: {day} day(s), {hour} hour(s), {minute} minute(s) and {second} "
                      f"second(s).")
        else :
            second = (usrInput % 86400) % 3600
            if second == 0 :
                print(f"  {usrInput:,} seconds is: {day} day(s) and {hour} hour(s).")
            else :
                print(f"  {usrInput:,} seconds is: {day} day(s), {hour} hour(s) and {second} second(s).")
    elif 0 < (usrInput % 86400) <3600 :
        if 60 <= (usrInput % 86400) :
            minute = (usrInput % 86400) // 60
            second = (usrInput % 86400) % 60
            if second == 0 :
                print(f"  {usrInput:,} seconds is: {day} day(s) and {minute} minute(s).")
            else :
                print(f"  {usrInput:,} seconds is: {day} day(s), {minute} minute(s) and {second} second(s).")
        else :
            second = usrInput % 86400
            print(f"  {usrInput:,} seconds is: {day} day(s) and {second} second(s).")
    else :
        print(f"  {usrInput:,} seconds is: {day} day(s).")
else :
    print(f"  The number of seconds is less than one minute.")

