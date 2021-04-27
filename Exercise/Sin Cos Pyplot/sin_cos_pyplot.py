################################################################################
# Author: Doyoon Kim (kim3312@purdue.edu / doyoon3312@kakao.com)
# Date: Apr 13, 2021
# Description This program draws sin and cos graph between interval [0, 360] in
# degree
################################################################################
import math
import matplotlib.pyplot as plt

# get_sin_values(): This function returns dictionary, which uses x values as a key,
# sin(x) value as a value, between interval [0,360]
def get_sin_values():
    outputDict: dict = {}
    for point in range(0,360,1):
        outputDict[point] = math.sin(point * (math.pi / 180))
    return outputDict

# get_sin_values(): This function returns dictionary, which uses x values as a key,
# cos(x) value as a value, between interval [0,360]
def get_cos_values():
    outputDict: dict = {}
    for point in range(0, 360, 1):
        outputDict[point] = math.cos(point * (math.pi / 180))
    return outputDict


def main():
    sinPlotData = get_sin_values()
    sinPoint = sinPlotData.keys()
    sinValue = sinPlotData.values()

    cosPlotData = get_cos_values()
    cosPoint = cosPlotData.keys()
    cosValue = cosPlotData.values()

    fig, chart = plt.subplots()
    chart.plot(sinPoint, sinValue, color='r')
    chart.plot(cosPoint, cosValue, color='b')
    chart.set_ylim(-1.2,1.2)
    chart.set_xlim(-10, 380)
    chart.set_xticks([90,180,270,360])
    chart.set_yticks([-1, 1])
    chart.set_xticklabels(['$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$'])
    chart.spines['bottom'].set_position(('data', 0))
    chart.spines['left'].set_position(('data', 0))
    chart.spines['top'].set_visible(False)
    chart.spines['right'].set_visible(False)

    plt.savefig("sin_cos_pyplot.pdf")


if __name__ == '__main__':
    main()
    plt.show()
