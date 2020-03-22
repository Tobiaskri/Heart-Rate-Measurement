from Code.userInterface import *
from Code.processData import processing

from matplotlib import pyplot as plt


def main():

    data = loadData()

    red_light = data[:,1]
    green_light = data[:,1]
    blue_light = data[:,2]

    plt.plot(range(len(red_light)),red_light)
    plt.show()

    red_light = processing(red_light)

    plt.plot(range(len(red_light)),red_light)
    plt.show()

main()
