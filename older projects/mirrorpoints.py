N = int(input())

numbers = []

i = 0
while i < N:
    numbers.append(float(input()))
    i = i + 1

mirrorPoints = []

i = 1
while i < N:
    a = 0
    j = 0
    while j < i:
        a = a + numbers[j]
        j = j + 1
    

    b = 0
    k = i
    while k < N:
        b = b + numbers[k]
        k = k + 1

    if a == b:
        mirrorPoints.append(i)

    i = i + 1



print(len(mirrorPoints))