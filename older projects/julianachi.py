series = [1]
num = 0
while num < 5000:
    num = series[len(series) - 1]
    i = 1
    dividants = []
    while i <= series[len(series) - 1]:
        if num % i == 0:
            dividants.append(i)
        i = i + 1

    series.append(num + len(dividants))




n = 1
while n != 0:
    n = int(input())

    if n == 0:
        break

    if series.__contains__(n):
        print("Part of the series")
    else:
        print("Not part of the series")