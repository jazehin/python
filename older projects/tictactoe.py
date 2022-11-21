# To my understanding this is a simple tictactoe type of game, kinda combined with tetris (a very cool idea tbh)
# Rhe output language will be English, as I still don't speak Spanish
# The point formula I decided on: 
# winner: floor(10 * (42 / tokens) + 20 - randomMoves * 2.5)
# loser:  ceiling(-10 - randomMoves * 2.5)

import math
import random as rnd

class Player:
    def __init__(self, name):
        self.name = name
        self.token = None
        self.randomMoves = 0

players = []
game = []
for i in range(0, 7, 1):
    game.append([])
    for j in range (0, 6, 1):
        game[i].append('.')
next = rnd.randint(0, 1)
column = None

numbers = [str(i) for i in range(1, 8)]

winState = {
    "ongoing"      : 0,
    "playerOneWon" : 1,
    "playerTwoWon" : 2,
    "tie"          : 3
}
win = winState['ongoing']

scores = {}

tokens = 0

def start():

    print("*** FOUR IN A ROW ***\n")

    newGame()

    input('Press ENTER to exit...')

def newGame():
    global win
    win = winState['ongoing']
    global scores
    scores = {}
    global players
    players = []
    global game
    game = []
    for i in range(0, 7, 1):
        game.append([])
        for j in range (0, 6, 1):
            game[i].append('.')
    global next
    next = rnd.randint(0, 1)
    global column
    column = None
    global tokens
    tokens = 0

    players.append(Player(input("> Please type the name of the first player: "))) # Input name for player #1

    while players[0].token != 'X' and players[0].token != 'O': # Repeat asking until the input is valid
        players[0].token = input("> {}, please type which token you wish to use [X/O]: ".format(players[0].name)).capitalize()

    players.append(Player(input("> Please type the name of the second player: "))) # Input name for player #2

    if players[0].token == 'X':
        players[1].token = 'O'
    else:
        players[1].token = 'X'

    print("> {}, your token is: {}".format(players[1].name, players[1].token))

    print('\n> Throwing a coin in the air to determine who starts the game...')
    print('> {} starts the game'.format(players[next].name))

    printGame()

    loop(next)

def loop(next):
    global tokens
    tokens += 1

    column = None
    while not numbers.__contains__(column) and column != 'R':
        column = input('> {}, enter a column number [1-7] or [R] to assign randomly: '.format(players[next].name)).capitalize()

    if column == 'R':
        column = rnd.randint(0, 6)
        while game[column][5] != '.':
            column = rnd.randint(0, 6)

        print('> Mmm... column #{} was chosen'.format(column + 1))

        players[next].randomMoves += 1
    else:
        column = int(column) - 1

    result = placeSign(column, next)

    if not result:
        print('> {}, please choose another column!'.format(players[next].name))
        loop(next)

    printGame()

    win = checkGame()

    

    if win is winState['ongoing']:
        if next == 0:
            next = 1
        else:
            next = 0
        loop(next)
    else:
        print(win)
        pointCalc(win)
        return

def printGame():
    print('\n 1234567')
    print('+-------+')
    
    for j in range(4, -1, -1):
        txt = '|'
        for i in range(0, 7, 1):
            txt += game[i][j]
        txt += '|'
        print(txt)

    print('+-------+\n')
    
def placeSign(column, playerNumber):
    if game[column][5] != '.':
        return False
    
    for i in range(0, 5, 1):
        if game[column][i] == '.':
            game[column][i] = players[playerNumber].token
            return True

    game[column][5] = players[playerNumber].token
    return True

def checkGame():
    for x in range(0, 7, 1):
        for y in range(0, 6, 1):
            for xOffset in range(-1, 2, 1):
                for yOffset in range(-1, 2, 1):
                    if (xOffset == 0 and yOffset == 0) or game[x][y] == '.':
                        continue
                    if checkTokens(x, y, xOffset, yOffset):
                        if game[x][y] == players[0].token:
                            return winState['playerOneWon']
                        else:
                            return winState['playerTwoWon']

    i = 0
    while i < 7 and game[i][5] != '.':
        i += 1
    
    if i == 7:
        return winState['tie']
    
    return winState['ongoing']

def checkTokens(x, y, xOffset, yOffset):
    evaluation = False
    try:
        evaluation = game[x][y] == game[x + 1 * xOffset][y + 1 * yOffset] and game[x][y] == game[x + 2 * xOffset][y + 2 * yOffset] and game[x][y] == game[x + 3 * xOffset][y + 3 * yOffset]
    except:
        return False
    else:
        return evaluation

def pointCalc(win):

    readFile()

    if win is winState['playerOneWon']:
        winnerPoints = math.floor(10 * (42 / tokens) + 20 - players[0].randomMoves * 2.5)
        loserPoints  = math.ceil(-10 - players[1].randomMoves * 2.5)

        if scores.keys().__contains__(players[0].name):
            scores[players[0].name] += winnerPoints
        else:
            scores[players[0].name] = winnerPoints

        if scores.keys().__contains__(players[1].name):
            scores[players[1].name] += loserPoints
        else:
            scores[players[1].name] = loserPoints

        print('> {} won {} points, and {} lost {} points.'.format(players[0].name, winnerPoints, players[1].name, -loserPoints))

    elif win is winState['playerTwoWon']:
        winnerPoints = math.floor(10 * (42 / tokens) + 20 - players[1].randomMoves * 2.5)
        loserPoints  = math.ceil(-10 - players[0].randomMoves * 2.5)

        if scores.keys().__contains__(players[1].name):
            scores[players[1].name] += winnerPoints
        else:
            scores[players[1].name] = winnerPoints

        if scores.keys().__contains__(players[0].name):
            scores[players[0].name] += loserPoints
        else:
            scores[players[0].name] = loserPoints

        print('> {} won {} points, and {} lost {} points.'.format(players[0].name, winnerPoints, players[1].name, -loserPoints))

    elif win is winState['tie']:
        print('> It\'s a tie, so no one gets points this round.')

    writeFile()

def readFile():
    global scores
    file = open('scoreboard.txt', 'a')
    file.close()
    file = open('scoreboard.txt', 'r')
    for line in file:
        t = line.split(': ')
        t[1] = int(t[1])
        if scores.keys().__contains__(t[0]):
            scores[t[0]] += t[1]
        else:
            scores[t[0]] = t[1]
    file.close()

def writeFile():
    global scores
    file = open('scoreboard.txt', 'w')
    for name in scores.keys():
        file.write('{}: {}\n'.format(name, scores[name]))
    file.close()

start()