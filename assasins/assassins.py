import datetime

f = open("assassins.txt", "r")

numberOfCriminals = int(f.readline())

i = 0
while (i < numberOfCriminals):
    criminalData = f.readline().split(", ")
    name = criminalData[0]
    numberOfCrimes = int(criminalData[1])

    crimes = []

    j = 0
    while (j < numberOfCrimes):
        timeArray = f.readline().split("-")
        crimes.append(datetime.datetime(
            int(timeArray[0])),
            int(timeArray[1])),
            int(timeArray[2]))
        )
    







    i = i + 1







f.close()