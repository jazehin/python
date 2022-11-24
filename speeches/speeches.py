import re as regex
pattern = r"[a-zA-Z]{3}[a-zA-Z]+\w"

def RemoveDuplicates(array):
    tmp = []
    for element in array:
        if (not element in tmp):
            tmp.append(element)
    return tmp

keys = []
values = []

with open('speeches.txt', 'r') as fp:
    for line in fp:
        line = line.lower()
        words = regex.findall(pattern, line)
        words = RemoveDuplicates(words)
        for word in words:
            if (word in keys):
                values[keys.index(word)] = values[keys.index(word)] + 1
            else:
                keys.append(word)
                values.append(1)

i = 0
while (i < len(keys) - 1):
    j = i + 1
    while (j < len(keys)):
        if (keys[i] > keys[j]):
            tmp = keys[i]
            keys[i] = keys[j]
            keys[j] = tmp

            tmp = values[i]
            values[i] = values[j]
            values[j] = tmp
        j = j + 1
    i = i + 1

i = 0
while (i < len(keys)):
    print("{} {}".format(keys[i], values[i]))
    i = i + 1