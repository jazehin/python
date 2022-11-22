def CheckSudoku(sudoku):
    # checking rows
    for row in sudoku:
        temp = []
        for number in row:
            if (number in temp):
                return False
            else:
                temp.append(number)

    # checking columns
    columnIndex = 0
    while (columnIndex < 9):
        temp = []
        rowIndex = 0
        while (rowIndex < 9):
            if (sudoku[rowIndex][columnIndex] in temp):
                return False
            else:
                temp.append(sudoku[rowIndex][columnIndex])
            rowIndex = rowIndex + 1
        columnIndex = columnIndex + 1

    # checking groups
    # there are 9(3*3) 3*3 groups
    i = 0
    while (i < 3):
        j = 0
        while (j < 3):
            temp = []
            k = 0
            while (k < 3):
                l = 0
                while (l < 3):
                    if (sudoku[i * 3 + k][j * 3 + l] in temp):
                        return False
                    else:
                        temp.append(sudoku[i * 3 + k][j * 3 + l])
                    l = l + 1
                k = k + 1
            j = j + 1
        i = i + 1

    return True



f = open("sudoku.txt", "r")

numberOfSudokus = int(f.readline())

i = 0
while (i < numberOfSudokus):
    f.readline()

    sudoku = []

    rowIndex = 0
    while (rowIndex < 9):
        row = f.readline().split(" ")
        sudoku.append([])
        for number in row:
            sudoku[rowIndex].append(int(number))
        rowIndex = rowIndex + 1

    if (CheckSudoku(sudoku)):
        print("Resolved")
    else:
        print("Not resolved")

    i = i + 1

f.close()