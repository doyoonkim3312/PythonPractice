################################################################################
# Author: Doyoon Kim (kim3312@purude.edu / doyoon3312@kakao.com)
# Date: Apr 13, 2021
# Description This program takes 2008 Weekly Gas price database file, and generates
# corresponding plot graph.
################################################################################

import matplotlib.pyplot as plt

# read_file(): this function read DB file suggested, and returns dictionary, which uses number of week as key
# and corresponding sales value as a value
def read_file():
    dbFile = open('2008_Weekly_Gas_Averages.txt', 'r')
    weeklyGasPrices = dbFile.read()
    dbFile.close()

    outputDict: dict = {}
    weekCounter = 1
    for salesValue in weeklyGasPrices.split("\n"):
        if salesValue != '':
            outputDict[weekCounter] = float(salesValue)
            weekCounter += 1
        else:
            continue
    return outputDict


def main():
    salesData = read_file()
    salesValues:list = salesData.values()
    weeks: list = salesData.keys()

    fig, chart = plt.subplots()
    chart.set_title("2008 Weekly Gas Prices")
    chart.set_xlabel("Weeks (by number)")
    chart.set_ylabel("Average Price (dollars/gallon")

    chart.plot(weeks, salesValues)
    chart.set_xlim(1, 52)
    chart.set_ylim(1.5, 4.3)
    chart.grid()

    plt.savefig("gas_prices.pdf")


if __name__ == '__main__':
    main()
    plt.show()
