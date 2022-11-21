mirroredHour = int(input())
mirroredMinute = int(input())

totalTime = mirroredHour * 60 + mirroredMinute
twelveHours = 12 * 60

difference = twelveHours - totalTime

realHour = int(difference / 60)
realMinute = int(difference - realHour * 60)

if realHour == 0:
    realHour = 12

print(f"{realHour}:{realMinute}")