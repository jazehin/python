def PerformChange(rubik, change):
    # 1st char: F = row, C = column
    # 2nd char: number of row/column
    # 3rd char: + = right/down, - = left/up
    n = len(rubik)
    i = int(change[1]) - 1

    if (change[0] == 'F'):
        if (change[2] == '+'):
            tmp = rubik[i].pop(n - 1)
            rubik[i].insert(0, tmp)
        elif (change[2] == '-'):
            tmp = rubik[i].pop(0)
            rubik[i].append(tmp)
    else:
        if (change[2] == '+'):
            array = []
            j = 0
            while (j < n):
                array.append(rubik[j][i])
                j = j + 1

            tmp = array.pop(n - 1)
            array.insert(0, tmp)
            
            j = 0
            while (j < n):
                rubik[j][i] = array[j]
                j = j + 1
            
        elif (change[2] == '-'):
            array = []
            j = 0
            while (j < n):
                array.append(rubik[j][i])
                j = j + 1

            tmp = array.pop(0)
            array.append(tmp)
            
            j = 0
            while (j < n):
                rubik[j][i] = array[j]
                j = j + 1

    return rubik

def PrintRubik(rubik):
    for row in rubik:
        string = ""
        for number in row:
            string = string + str(number)
        print(string)
    print()

f = open("rubikcube.txt", "r")

numberOfRubiks = int(f.readline())

i = 0
while (i < numberOfRubiks):
    n = int(f.readline())
    moves = f.readline().split(" ")
    
    rubik = []
    j = 0
    while (j < n):
        rubik.append([])
        k = 0
        while (k < n):
            rubik[j].append(k + 1)
            k = k + 1
        j = j + 1
    
    for move in moves:
        rubik = PerformChange(rubik, move)
    
    PrintRubik(rubik)

    i = i + 1

f.close()