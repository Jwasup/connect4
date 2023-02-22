import pygame
import os
import math
from math import trunc
import random
from random import random
import time

#define the width and height of the board, create a window and name it connect 4
WIDTH, HEIGHT = 700, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")

#load image files and resize them where neccisary
redPiece = pygame.image.load(os.path.join('Assets', 'redPiece.png'))

yellowPiece = pygame.image.load(os.path.join('Assets', 'yellowPiece.png'))

redX = pygame.image.load(os.path.join('Assets', 'redX.png'))
redX = pygame.transform.scale(redX, (100, 100))

yellowX = pygame.image.load(os.path.join('Assets', 'yellowX.png'))
yellowX = pygame.transform.scale(yellowX, (100, 100))

whiteLine = pygame.image.load(os.path.join('Assets', 'whiteLine.png'))
#load constants
BLACK = (0, 0, 0)

FPS = 60

nodes = 0

#flashing the board for the end of the game to illustrate where the 
def flashBoard(board):
    for i in range(3):
        #iterate through the board and print it onto the screen, using x's for the connect4
        WIN.fill(BLACK)  
        for i in range(6):
            WIN.blit(whiteLine, (100 + 100 * i, 0))
            for j in range(7):
                if board[i][j] == 'R':
                    WIN.blit(redPiece, (100 * j, 100 * i))
                elif board[i][j] == 'Y':
                    WIN.blit(yellowPiece, (100 * j, 100 * i))
                elif board[i][j] == 'r':
                    WIN.blit(redX, (100 * j, 100 * i))
                elif board[i][j] == 'y':
                    WIN.blit(yellowX, (100 * j, 100 * i))
        pygame.display.update()

        pygame.time.wait(600)
        #iterate through the board and print it to the screen, leaving the spaces that are occupied by the connect 4 blank
        WIN.fill(BLACK)  
        for i in range(6):
            WIN.blit(whiteLine, (100 + 100 * i, 0))
            for j in range(7):
                if board[i][j] == 'R':
                    WIN.blit(redPiece, (100 * j, 100 * i))
                elif board[i][j] == 'Y':
                    WIN.blit(yellowPiece, (100 * j, 100 * i))
        pygame.display.update()

        pygame.time.wait(600)


def printBoard(board):
    #print the board to the scrren
    WIN.fill(BLACK)  
    for i in range(6):
        WIN.blit(whiteLine, (100 + 100 * i, 0))
        for j in range(7):
            if board[i][j] == 'R':
                WIN.blit(redPiece, (100 * j, 100 * i))
            elif board[i][j] == 'Y':
                WIN.blit(yellowPiece, (100 * j, 100 * i))
            elif board[i][j] == 'r':
                WIN.blit(redX, (100 * j, 100 * i))
            elif board[i][j] == 'y':
                WIN.blit(yellowX, (100 * j, 100 * i))
    pygame.display.update()

def miniMax(board, currentMove, nextMove, depth, prevMoveX, prevMoveY):
    #increment the node counter by one, this is printed after every ai generated move for now for testing purposes
    global nodes
    nodes += 1

    #check for vertical connect 4 (Trivial due to gravity)
    try:
        if board[prevMoveY + 1][prevMoveX] == board[prevMoveY + 2][prevMoveX] == board[prevMoveY + 3][prevMoveX] == nextMove:
            return -1
    except:
        pass

    #each of these 3 blocks check for a different type of connect 4, -, \, and / respectively.
    #they do this by iterating through the 7 pieces in line with the last moved piece along their 
    #respective lines and counting how many consecutive are equal to the piece to check for a connect 4
    counter = 0
    for i in range(7):
        if 0 <= prevMoveY < 6 and 0 <= prevMoveX - 3 + i < 7:
            if board[prevMoveY][prevMoveX - 3 + i] == nextMove:
                counter += 1
            else:
                counter = 0

            if counter >= 4:
                return -1
    
    counter = 0
    for i in range(7):
        if 0 <= prevMoveY - 3 + i < 6 and 0 <= prevMoveX - 3 + i < 7:
            if board[prevMoveY - 3 + i][prevMoveX - 3 + i] == nextMove:
                counter += 1
            else:
                counter = 0

            if counter >= 4:
                return -1

    counter = 0
    for i in range(7):
        if 0 <= prevMoveY + 3 - i < 6 and 0 <= prevMoveX - 3 + i < 7:
            if board[prevMoveY + 3 - i][prevMoveX - 3 + i] == nextMove:
                counter += 1
            else:
                counter = 0

            if counter >= 4:
                return -1
    
    #base case, prevents excessive recursion.  Every increase to max depth roughly 7x processing speed
    if depth > 5:
        return 0

    #prepares the variables which will store potentially winning moves
    winMoves = ''
    tieMoves = ''
    loseMoves = ''
    #iterating through each possibe move which could be made
    for i in range(7):
        #place said piece
        spaceFound = False
        for j in range(6):
            if board[5 - j][i] == '':
                board[5 - j][i] = currentMove
                prevMoveY = 5 - j
                spaceFound = True
                break
        #if no space to place the piece is found, continue to the next column
        if spaceFound == False:
            continue
        #calculate the value of the new board
        miniResult = -1 * miniMax(board, nextMove, currentMove, depth + 1, i, prevMoveY)

        #update the respective move list
        if miniResult == 1:
            winMoves += str(i)
        elif miniResult == 0:
            tieMoves += str(i)
        elif miniResult == -1:
            loseMoves += str(i)

        #restore the board to how it was before checking the move
        board[prevMoveY][i] = ''
        #if a winning move is found, assume no better moves can be found and stop searching alternative moves from the same board state
        if depth != 0:
            if winMoves != '':
                return 1
    #if depth is not 0, return the value of the board depending on what the best type of move which was found is.  If this point is reached
    #it can be assumed no winning moves were found thanks to previous block
    if depth != 0:
        if tieMoves != '':    
            return 0
        elif loseMoves != '':
            return -1
        else:
            return 0
    else:
        #if it is depth zero we want to return the best move rather than the value of the board,
        #this block slects a random move from the list of the best moves
        if winMoves != '':
            randomInt = trunc(random() * len(winMoves))
            return winMoves[randomInt]
        elif tieMoves != '':
            randomInt = trunc(random() * len(tieMoves))
            return tieMoves[randomInt]
        elif loseMoves != '':
            randomInt = trunc(random() * len(loseMoves))
            return loseMoves[randomInt]
        else:
            #this will trigger if no moves are found(aka the board is full and the game is a tie)
            return 0

def main():
    #prepare the board along with various variables
    board = [['']*7 for i in range(6)]
    currentMove = 'R'
    nextMove = 'Y'
    run = True
    clock = pygame.time.Clock()
    while run:
        #limit the fps to 60
        clock.tick(FPS)
        #iterate through each event in each frame
        for event in pygame.event.get():
            #quit if the event type is pygame.quit
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            #if the event is mousebuttondown or the current move is Y (AI's move) run this block.
            if event.type == pygame.MOUSEBUTTONDOWN or currentMove == 'Y':
                #if its the player's move get the x coordinate of the mouse and convert into which comumn the player is clicking
                if currentMove == 'R':
                    mouseX, mouseY = pygame.mouse.get_pos()
                    mouseX = trunc(mouseX / 100)
                else:
                    #run the minimax function, print the number of nodes that are explored and the time it took to explore them
                    timeOne = time.time()
                    global nodes
                    nodes = 0
                    mouseX = int(miniMax(board, currentMove, nextMove, 0, 0, 0))
                    print(f"{nodes} Nodes Searched in ",end='')
                    timeTwo = time.time()
                    timeDiff = round(1000 * (timeTwo - timeOne))
                    print(f"{timeDiff} Miliseconds")
                #place the piece in the appropriate location, in the lowest available slot in the correct column
                for i in range(6):
                    if board[5 - i][mouseX] == '':
                        board[5 - i][mouseX] = currentMove
                        mouseY = 5 - i
                        break
                #check for a vertical connect 4
                try:
                    if board[mouseY + 1][mouseX] == board[mouseY + 2][mouseX] == board[mouseY + 3][mouseX] == currentMove:
                        printBoard(board)
                        run = False
                        winner = currentMove
                        board[mouseY][mouseX] = board[mouseY + 1][mouseX] = board[mouseY + 2][mouseX] = board[mouseY + 3][mouseX] = currentMove.lower()
                except:
                    pass
                #each of these 3 blocks check for a different type of connect 4, -, \, and / respectively.
                #they do this by iterating through the 7 pieces in line with the last moved piece along their 
                #respective lines and counting how many consecutive are equal to the piece to check for a connect 4
                counter = 0
                for i in range(7):
                    if 0 <= mouseY < 6 and 0 <= mouseX - 3 + i < 7:
                        if board[mouseY][mouseX - 3 + i] == currentMove:
                            counter += 1
                        else:
                            counter = 0

                        if counter >= 4:
                            board[mouseY][mouseX - 3 + i] = board[mouseY][mouseX - 4 + i] = board[mouseY][mouseX - 5 + i] = board[mouseY][mouseX - 6 + i] = currentMove.lower()
                            printBoard(board)
                            run = False
                            winner = currentMove
                            break
                
                counter = 0
                for i in range(7):
                    if 0 <= mouseY - 3 + i < 6 and 0 <= mouseX - 3 + i < 7:
                        if board[mouseY - 3 + i][mouseX - 3 + i] == currentMove:
                            counter += 1
                        else:
                            counter = 0

                        if counter >= 4:
                            board[mouseY - 3 + i][mouseX - 3 + i] = board[mouseY - 4 + i][mouseX - 4 + i] = board[mouseY - 5 + i][mouseX - 5 + i] = board[mouseY - 6 + i][mouseX - 6 + i] = currentMove.lower()
                            printBoard(board)
                            run = False
                            winner = currentMove
                            break

                counter = 0
                for i in range(7):
                    if 0 <= mouseY + 3 - i < 6 and 0 <= mouseX - 3 + i < 7:
                        if board[mouseY + 3 - i][mouseX - 3 + i] == currentMove:
                            counter += 1
                        else:
                            counter = 0

                        if counter >= 4:
                            board[mouseY + 3 - i][mouseX - 3 + i] = board[mouseY + 4 - i][mouseX - 4 + i] = board[mouseY + 5 - i][mouseX - 5 + i] = board[mouseY + 6 - i][mouseX - 6 + i] = currentMove.lower()
                            printBoard(board)
                            run = False
                            winner = currentMove
                            break
                #swap the turn
                storeMove = currentMove
                currentMove = nextMove
                nextMove = storeMove
            #print the board
            printBoard(board)

    flashBoard(board)
                    

if __name__ == '__main__':
    main()