from operator import truediv


def sortHand(hand):
    i = 0
    while i < len(hand) - 1:
        j = i
        while j < len(hand):
            if hand[i][0] > hand[j][0]:
                tmp = hand[i]
                hand[i] = hand[j]
                hand[j] = tmp
            j = j + 1
        i = i + 1
    return hand

N = int(input())

hands = []

i = 0
while i < N:
    hands.append([])

    j = 0
    while j < 5:
        hands[i].append([])
        hands[i][j].append(int(input()))
        hands[i][j].append(input())
        j = j + 1

    i = i + 1

for hand in hands:
    sortedHand = sortHand(hand)
    
    sameSuit = True
    suit = sortedHand[0][1]
    for i in range(1, 5):
        if sortedHand[i][1] != suit:
            sameSuit = False

    firstCardValue = sortedHand[0][0]

    if sameSuit and sortedHand[0][0] == 10 and sortedHand[1][0] == 11 and sortedHand[2][0] == 12 and sortedHand[3][0] == 13 and sortedHand[4][0] == 14:
        print("Royal flush")
    elif sameSuit and sortedHand[1][0] == firstCardValue + 1 and sortedHand[2][0] == firstCardValue + 2 and sortedHand[3][0] == firstCardValue + 3 and sortedHand[4][0] == firstCardValue + 4:
        print("Straight flush")
    elif sameSuit:
        print("Flush")
    elif sortedHand[1][0] == firstCardValue + 1 and sortedHand[2][0] == firstCardValue + 2 and sortedHand[3][0] == firstCardValue + 3 and sortedHand[4][0] == firstCardValue + 4:
        print("Straight")
    else:
        print("None of the specified")