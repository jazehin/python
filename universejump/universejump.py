f = open("universejump.txt", "r")

numberOfCases = int(f.readline())

def GetHopNumber(hops, possibleHops):
    i = 0
    while (i < len(possibleHops) and possibleHops[i][0] != hops[len(hops) - 1]):
        i = i + 1
    if (i < len(possibleHops)):
        if (possibleHops[i][1] == hops[0]):
            
            return len(hops)
        else:
            hops.append(possibleHops[i][1])
            return GetHopNumber(hops, possibleHops)
    else:
        return 0

i = 0
while (i < numberOfCases):
    numberOfHops = int(f.readline())
    possibleHops = []

    j = 0
    while (j < numberOfHops):
        possibleHops.append(f.readline().replace("\n", "").split(" "))
        j = j + 1

    hops = []
    hops.append(possibleHops[0][0])
    hops.append(possibleHops[0][1])
    
    numberOfHops = GetHopNumber(hops, possibleHops)
    if (numberOfHops == 0):
        print("They wander the multiverse")
    else:
        print("They can return to {} in {} jumps".format(hops[0], numberOfHops)) 
    
    
    i = i + 1
