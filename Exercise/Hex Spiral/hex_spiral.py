################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com
# Date: Mar 13, 2021
# Description This program draws hexagonal spiral with length increment of 6
# pixels
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width('5')
    # --------------------------------------------------------------------------

    # Write your code here
    pixel = 0
    for _ in range(39):
        pixel = pixel + 6
        forward(pixel)
        right(60)

# Don't change this
if __name__ == '__main__':
    main()
    done()
