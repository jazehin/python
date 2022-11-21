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
        crimes.append(datetime.date(int(timeArray[0]), int(timeArray[1]), int(timeArray[2])))
        j = j + 1
        
    # I don't know if it's specified, but I'm going to assume that there are at least 2 crimes committed.

    diff = crimes[1].__sub__(crimes[0]).days
    delta = datetime.timedelta(days=diff)
    
    isPeriodical = True
    j = 2
    while (j < numberOfCrimes and isPeriodical):
        if (crimes[j].__sub__(crimes[j - 1]).days != diff):
            isPeriodical = False
        else:
            j = j + 1

    if (isPeriodical):
        print("{} attacks every {} days and will do so again on {}".format(name, diff, crimes[len(crimes) - 1] + delta))
    else:
        print("{} is not a serial killer".format(name))

    i = i + 1

f.close()