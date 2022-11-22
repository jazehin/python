# https://regex101.com/r/CLF3Tj/1 explains what the regex (regular expression) does
import re as regex
pattern = "\?[^\?]+\?"

questions = []

with open('smith.txt', 'r') as fp:
    for line in fp:
        temp = regex.findall(pattern, line)
        for question in temp:
            if (not question in questions and line.startswith("Smith:")):
                questions.append(question)

for question in questions:
    print(question)