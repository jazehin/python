# main diagonal -> going from upper left corner to bottom right corner

def isLowerTriangular(matrix):
    loverTriangular = True
    length = len(matrix)
    i = 2
    j = 1
    while (i < length):
        
    return True




def isUpperTriangular(matrix):
    return True    




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

    loverTriangular = isLowerTriangular(matrix)
    upperTriangular = isUpperTriangular(matrix)
    diagonal = isDiagonal(matrix)

    i = i + 1