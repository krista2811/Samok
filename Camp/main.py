import pygame, sys, math
import time

from Ai import *

from pygame.locals import *
#
VERTICAL = 0
HORIZONTAL = 1
RIGHTDOWN = 2
RIGHTUP = 3

#Game Setting
TARGET_FPS = 60
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
STONE_SIZE = 31
LEFT = 1
TURN = 1
gameBoard = []#19*19

BLACK = "black"
WHITE = "white"
BLANK = "*"

#Game Init
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Four Go')
fps_clock = pygame.time.Clock()
gameOver = False
winner = ""

#Load Images
bStone = pygame.image.load("./images/black.png")
wStone = pygame.image.load("./images/white.png")
board = pygame.image.load("./images/board.png")

board = pygame.transform.scale(board, (600, 600))
bStone = pygame.transform.scale(bStone, (STONE_SIZE, STONE_SIZE))
wStone = pygame.transform.scale(wStone, (STONE_SIZE, STONE_SIZE))

def checkOneLine(color, x, y, dir): #direction = int
    flag = False
    length = 0
    dx = 0;
    dy = 0;
    _x = 0
    _y = 0

    if dir == RIGHTUP:
        dx = 1
        dy = -1
    elif dir == RIGHTDOWN:
        dx = 1
        dy = 1
    elif dir == HORIZONTAL:
        dx = 1
        dy = 0
    elif dir == VERTICAL:
        dx = 0
        dy = 1

    for i in range(7):
        _y = y + (-3)*dy + i * dy
        _x = x + (-3)*dx + i * dx

        if(_x < 19 and _x >= 0 and _y < 19 and _y >= 0):
            if(flag) :   
                    if(gameBoard[_y][_x] == color) :
                        length += 1
                        if length == 4:
                            return True
                    else:
                        flag = False
                        length = 0
            else:
                if(gameBoard[_y][_x] == color):
                    flag = True
                    length += 1

def isFour(color, x, y):
    flag = False; #flag for panjung
    length = 0;
    if checkOneLine(color, x, y, RIGHTUP):
        return True
    elif checkOneLine(color, x, y, RIGHTDOWN):
        return True
    elif checkOneLine(color, x, y, HORIZONTAL):
        return True
    elif checkOneLine(color, x, y, VERTICAL):
        return True
    else:
        return False

def setGame(gameBoard): 
    for i in range(19):
        oneRow = [];
        for j in range(19):
            oneRow.append(BLANK)
        gameBoard.append(oneRow)


def canDraw(x, y):
    if gameBoard[y][x] == BLANK:
        return True;
    else:
        return False;

def drawStone(color, x, y):

    global gameBoard;
    global TURN;

    #print(str(x) + ", " + str(y))

    px = 20 + STONE_SIZE * x;
    py = 20 + STONE_SIZE * y;

    px -= STONE_SIZE / 2
    py -= STONE_SIZE / 2

    if color == BLACK and canDraw(x, y):
        TURN += 1
        gameBoard[y][x] = BLACK
        screen.blit(bStone, (px, py))
    elif color == WHITE and canDraw(x, y):
        TURN += 1
        gameBoard[y][x] = WHITE
        screen.blit(wStone, (px, py))
    else:
        print(gameBoard[y][x])
        print("Error.")

def roundingOff(n):
    float_n = n - int(n)

    if (float_n >= 0.5):
        n = int(n) + 1
    else:
        n = int(n)

    return n

def pixelToCord(x, y):
    x = (x - 20) / STONE_SIZE
    y = (y - 20) / STONE_SIZE

    x = roundingOff(x)
    y = roundingOff(y)

    return (x, y)

# Draw Board

screen.blit(board, (0, 0))
setGame(gameBoard)
ai = Ai(gameBoard)
oldX = 0
oldY = 0
# Main Loop
while True:
    for event in pygame.event.get():
        if(not gameOver):
            if event.type == MOUSEBUTTONDOWN:
                if event.button == LEFT:
                    x, y = pixelToCord(event.pos[0], event.pos[1])
                    if TURN % 2 == 1 :
                        oldX = x
                        oldY = y
                        drawStone("black", x , y)
                        ai.update(gameBoard)
                        if(isFour(BLACK, x, y)):
                            gameOver = True
                            winner = BLACK    
                    else:
                        aiPosition = []
                        aiPosition = ai.calculateTree(oldX, oldY)
                        drawStone("white", aiPosition[0] , aiPosition[1])
                        ai.update(gameBoard)
                        if isFour(WHITE, x, y):
                            gameOver = True
                            winner = WHITE
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()

    fps_clock.tick(TARGET_FPS)


