
from Code.fetchData import *

def loadData():
    print("Select data source:")
    print("1. Record from webcam")
    print("2. Load from CSV-file")
    print("3. Load from MP4-file")

    source = input("Wanted mode (number): ")

    if source == "1":
        data = record()
    if source == "2":
        data = readCSVFile()
    if source == "3":
        data = readVideoFile()

    if source == "1" or source == "3":
        respond = input("Save data as csv-file? (y/n):  ")

        if respond == "y":
            filename = input("Filename:   ")

            if filename[0:4] != "Data.":
                filename = "Data/" + filename

            np.savetxt(filename, data)

    return data

