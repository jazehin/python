import datetime

monthLength = { 
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def DrawCalendar(year, month):
    if (((year % 400 == 0) and (year % 100 == 0)) or (year % 4 == 0) and (year % 100 != 0)): # https://www.programiz.com/python-programming/examples/leap-year
        # leap year, so feb is 29
        monthLength[2] = 29

    print(str.expandtabs("mon\ttue\twed\tthu\tfri\tsat\tsun", 5))

    date = datetime.date(year, month, 1)
    start = date.isoweekday()
    
    
    i = 1
    dayCounter = 1
    string = ""
    end = start + monthLength[date.month]
    while (i < end):
        if (i < start or i > start + monthLength[date.month]):
            string = string + "\t"
        else:
            string = string + "{}\t".format(dayCounter)
            dayCounter = dayCounter + 1

        if (i % 7 == 0 or i == end - 1):
            print(str.expandtabs(string, 5))
            string = ""

        i = i + 1

    monthLength[2] = 28
    

f = open("calendar.txt", "r")

numberOfDates = int(f.readline())

i = 0
while (i < numberOfDates):

    date = f.readline().split("/")
    # we don't really need the day imo
    month = int(date[1])
    year = int(date[2])

    # play around here with print() to separate them
    DrawCalendar(year, month)

    i = i + 1

f.close()