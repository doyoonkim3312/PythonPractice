################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 13, 2021
# Description This program takes each month's sales value from user and generate
# corresponding pie chart.
################################################################################
import matplotlib.pyplot as plt

# get_user_input: this function takes each month's sales value from user and returns dictionary which uses
# name of month as a key and corresponding sales value as a value.
def get_user_input():
    months: list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                    'October', 'November', 'December']
    outputDict: dict = {}
    for month in months:
        salesValue = int(input(f"Enter the sales for {month}: "))
        while salesValue < 0:
            salesValue = input(f"Invalid sales value detected.\n"
                               f"Enter the sales for {month}: ")
        outputDict[month] = salesValue
    return outputDict


def main():
    salesData: dict = get_user_input()
    salesKey: list = salesData.keys()
    salesValue: list = salesData.values()
    indexColor: list = ['#4D4038', '#BAA892', '#5B6870', '#6E99B4', '#A3D6D7', '#085C11', '#849E2A', '#C3BE0B',
                        '#E9E45B', '#6B4536', '#B46012', '#FF9B1A']
    fig, chart = plt.subplots()
    chart.set_title('Monthly Sales Values')
    chart.pie(salesValue, colors=indexColor, labels=salesKey)
    plt.savefig('MonthlySalesValues.pdf')   # Save plot as a .pdf file.


if __name__ == '__main__':
    main()
    plt.show()
