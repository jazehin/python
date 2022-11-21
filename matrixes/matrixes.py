# main diagonal -> going from upper left corner to bottom right corner

def isUpperTriangular(matrix):
    upperTriangular = True
    length = len(matrix)
    i = 1
    j = 0
    while (i < length and upperTriangular):
        while (j < i and upperTriangular):
            if (matrix[i][j] != 0):
                upperTriangular = False
            j = j + 1
        i = i + 1
        j = 0
    return upperTriangular




def isLowerTriangular(matrix):
    lowerTriangular = True
    length = len(matrix)
    i = 0
    j = 1
    while (i < length - 1 and lowerTriangular):
        j = i + 1
        while (j < length and lowerTriangular):
            if (matrix[i][j] != 0):
                lowerTriangular = False
            j = j + 1
        i = i + 1
    return lowerTriangular 




def isDiagonal(matrix):
    return isLowerTriangular(matrix) and isUpperTriangular(matrix)




f = open("matrixes.txt", "r")

numberOfMatrixes = int(f.readline())

i = 0
while (i < numberOfMatrixes):
    length = int(f.readline())

    matrix = []
    
    j = 0
    while (j < length):
        array = f.readline().split(" ")
        k = 0
        while (k < len(array)):
            array[k] = int(float(array[k]))
            k = k + 1

        matrix.append(array)
        j = j + 1
    
    if (isDiagonal(matrix)):
        print("Diagonal")
    elif (isLowerTriangular(matrix)):
        print("Lower triangular")
    elif (isUpperTriangular(matrix)):
        print("Upper triangular")
    else:
        print("Neither diagonal nor triangular")

    i = i + 1

f.close()