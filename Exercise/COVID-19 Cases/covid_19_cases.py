################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 13, 2021
# Description This program takes Indiana's Positive COVID-19 cases from external
# database and generates corresponding bar chart.
################################################################################

import datetime
import matplotlib.pyplot as plt

# read_file(): This function takes external COVID-19 cases value and returns dictionary, which uses date as a key
# cumulative positive case number as a value.
def read_file():
    dbFile = open('indiana_covid_19_data.txt', 'r')
    casesData = dbFile.read()
    dbFile.close()

    outputDict: dict = {}
    positiveCasesCumulative = 0
    for dayData in casesData.split("\n"):
        if dayData != '':
            try:
                dataByDay = dayData.split(" ")
                year, month, day = dataByDay[0].split('-')
                date = datetime.date(int(year), int(month), int(day))
                positiveCasesCumulative += int(dataByDay[2])
                outputDict[date] = positiveCasesCumulative / 1000
            except IndexError:
                print(f"Index Error Occurred: {dataByDay}")
        else:
            continue
    return outputDict


def main():
    data = read_file()
    dates: list = data.keys()
    casesCumulative: list = data.values()

    fig, chart = plt.subplots()
    chart.set_title("Positive COVID-19 Cases in Indiana")
    chart.set_xlabel("Date")
    chart.set_ylabel("Number of Cases (In thousands)")

    chart.bar(dates, casesCumulative)
    fig.autofmt_xdate()
    chart.set_ylim(0, 730)

    plt.savefig("covid_19_cases.pdf")


if __name__ == '__main__':
    main()
    plt.show()
