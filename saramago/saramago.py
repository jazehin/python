string = "saramago"

with open('saramago.txt', 'r') as fp:
    for line in fp:
    
        line = line.lower()
        counter = 0
        i = 0

        for letter in line:
            if (letter == string[i]):
                if (i == len(string) - 1):
                    i = 0
                    counter = counter + 1
                else:
                    i = i + 1

        print(counter)