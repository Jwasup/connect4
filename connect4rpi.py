import pygame
import os
import math
from math import trunc
import random
from random import random
import time

#define the width and height of the board, create a window and name it connect 4
WIDTH, HEIGHT = 320, 240
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")

#load image files and resize them where neccisary
redPiece = pygame.image.load(os.path.join('Assets', 'redPiece.png'))
redPiece = pygame.transform.scale(redPiece, (40, 40))

yellowPiece = pygame.image.load(os.path.join('Assets', 'yellowPiece.png'))
yellowPiece = pygame.transform.scale(yellowPiece, (40, 40))

redX = pygame.image.load(os.path.join('Assets', 'redX.png'))
redX = pygame.transform.scale(redX, (40, 40))

yellowX = pygame.image.load(os.path.join('Assets', 'yellowX.png'))
yellowX = pygame.transform.scale(yellowX, (40, 40))

whiteLine = pygame.image.load(os.path.join('Assets', 'whiteLine.png'))
whiteLine = pygame.transform.scale(whiteLine, (1,240))
horizontalWhiteLine = pygame.transform.scale(pygame.transform.rotate(whiteLine, 90), (280, 1))
#load constants
BLACK = (0, 0, 0)

FPS = 60

nodes = 0

#flashing the board for the end of the game to illustrate where the 
def flashBoard(board):
    #print the board to the scrren
    WIN.fill(BLACK)  
    for i in range(3):
        #iterate through the board and print it onto the screen, using x's for the connect4
        WIN.fill(BLACK)  
        for i in range(6):
            WIN.blit(whiteLine, (60 + 40 * i, 0))
            WIN.blit(horizontalWhiteLine, (20, 40 + 40 * i))
            for j in range(7):
                if board[i][j] == 'R':
                    WIN.blit(redPiece, (20 + 40 * j, 40 * i))
                elif board[i][j] == 'Y':
                    WIN.blit(yellowPiece, (20 + 40 * j, 40 * i))
                elif board[i][j] == 'r':
                    WIN.blit(redX, (20 + 40 * j, 40 * i))
                elif board[i][j] == 'y':
                    WIN.blit(yellowX, (20 + 40 * j, 40 * i))
        pygame.display.update()

        pygame.time.wait(600)
        #iterate through the board and print it to the screen, leaving the spaces that are occupied by the connect 4 blank
    #print the board to the scrren
    WIN.fill(BLACK)  
    for i in range(3):
        #iterate through the board and print it onto the screen, using x's for the connect4
        WIN.fill(BLACK)  
        for i in range(6):
            WIN.blit(whiteLine, (60 + 40 * i, 0))
            WIN.blit(horizontalWhiteLine, (20, 40 + 40 * i))
            for j in range(7):
                if board[i][j] == 'R':
                    WIN.blit(redPiece, (20 + 40 * j, 40 * i))
                elif board[i][j] == 'Y':
                    WIN.blit(yellowPiece, (20 + 40 * j, 40 * i))
                elif board[i][j] == 'r':
                    WIN.blit(redX, (20 + 40 * j, 40 * i))
                elif board[i][j] == 'y':
                    WIN.blit(yellowX, (20 + 40 * j, 40 * i))
        pygame.display.update()

        pygame.time.wait(600)


def printBoard(board):
    #print the board to the scrren
    WIN.fill(BLACK)  
    for i in range(3):
        #iterate through the board and print it onto the screen, using x's for the connect4
        WIN.fill(BLACK)  
        for i in range(6):
            WIN.blit(whiteLine, (60 + 40 * i, 0))
            WIN.blit(horizontalWhiteLine, (20, 40 + 40 * i))
            for j in range(7):
                if board[i][j] == 'R':
                    WIN.blit(redPiece, (20 + 40 * j, 40 * i))
                elif board[i][j] == 'Y':
                    WIN.blit(yellowPiece, (20 + 40 * j, 40 * i))
                elif board[i][j] == 'r':
                    WIN.blit(redX, (20 + 40 * j, 40 * i))
                elif board[i][j] == 'y':
                    WIN.blit(yellowX, (20 + 40 * j, 40 * i))
        pygame.display.update()
def bestMove(board, depth, maxDepth, isMaximizing, alpha, beta, prevMoveX, prevMoveY, currentMove, nextMove):
    #increment the node counter by one, this is printed after every ai generated move for now for testing purposes
    global nodes
    nodes += 1
    
    if isMaximizing:
        bestVal = -1000
        bestMove = ''
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
                print("X ",end="")
                continue
            #calculate the value of the new board
            value = miniMax(board, depth + 1, maxDepth, False, alpha, beta, i, prevMoveY, nextMove, currentMove)
            print(f"{value} ",end="")
            #restore the board to how it was before checking the move
            board[prevMoveY][i] = ''

            #update bestVal and alpha
            if value > bestVal:
                bestMove = i
            if value == bestVal:
                if i == 3:
                    bestMove = i
                elif i == 2:
                    bestMove = i
                elif i == 4 and bestMove == 2:
                    if random() > .5:
                        bestMove = i
                elif i == 1:
                    bestMove = i
                elif i == 5 and bestMove == 1:
                    if random() > .5:
                        bestMove = i
                elif i == 0:
                    bestMove = i
                elif i == 6 and bestMove == 0:
                    if random() > .5:
                        bestMove = i

            bestVal = max(bestVal, value)
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                break

        return bestMove
    else :
        for i in range(10):
            print("This code actually ran????")
        bestVal = 1000
        bestMove = ''
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
            value = miniMax(board, depth + 1, maxDepth, True, alpha, beta, i, prevMoveY, nextMove, currentMove)

            #restore the board to how it was before checking the move
            board[prevMoveY][i] = ''

            #update bestVal and alpha
            if value < bestVal:
                bestMove = i
            if value == bestVal:
                if i == 3:
                    bestMove = i
            bestVal = min(bestVal, value) 
            beta = min(beta, bestVal)
            if beta <= alpha:
                break

        return bestMove

def miniMax(board, depth, maxDepth, isMaximizing, alpha, beta, prevMoveX, prevMoveY, currentMove, nextMove):
    #increment the node counter by one, this is printed after every ai generated move for now for testing purposes
    global nodes
    nodes += 1

    global cutBranches

    try:
        if board[prevMoveY + 1][prevMoveX] == board[prevMoveY + 2][prevMoveX] == board[prevMoveY + 3][prevMoveX] == nextMove:
            if isMaximizing:
                return -(maxDepth - depth + 1)
            else:
                return depth
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
                if isMaximizing:
                    return -(maxDepth - depth + 1)
                else:
                    return depth
    
    counter = 0
    for i in range(7):
        if 0 <= prevMoveY - 3 + i < 6 and 0 <= prevMoveX - 3 + i < 7:
            if board[prevMoveY - 3 + i][prevMoveX - 3 + i] == nextMove:
                counter += 1
            else:
                counter = 0

            if counter >= 4:
                if isMaximizing:
                    return -(maxDepth - depth + 1)
                else:
                    return depth

    counter = 0
    for i in range(7):
        if 0 <= prevMoveY + 3 - i < 6 and 0 <= prevMoveX - 3 + i < 7:
            if board[prevMoveY + 3 - i][prevMoveX - 3 + i] == nextMove:
                counter += 1
            else:
                counter = 0

            if counter >= 4:
                if isMaximizing:
                    return -(maxDepth - depth + 1)
                else:
                    return depth
    
    #base case, prevents excessive recursion.  Every increase to max depth roughly 7x processing required
    if depth >= maxDepth:
        return 0
    
    if isMaximizing:
        value = -1000
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
            value = max(value, miniMax(board, depth + 1, maxDepth, False, alpha, beta, i, prevMoveY, nextMove, currentMove))

            #restore the board to how it was before checking the move
            board[prevMoveY][i] = ''

            #update bestVal and alpha
            if value > beta:
                cutBranches += 1
                break
            alpha = max(alpha, value)

        if value > -1000:
            return value
        else:
            return 0
    else :
        value = 1000
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
            value = min(value, miniMax(board, depth + 1, maxDepth, True, alpha, beta, i, prevMoveY, nextMove, currentMove))

            #restore the board to how it was before checking the move
            board[prevMoveY][i] = ''

            #update bestVal and alpha
            if value < alpha:
                cutBranches += 1
                break
            beta = min(beta, value)

        if value < 1000:
            return value
        else:
            return 0
        

def main():
    #prepare the board along with various variables
    board = [['']*7 for i in range(6)]
    currentMove = 'R'
    nextMove = 'Y'
    if random() > .5:
        randInt = trunc(random() * 7)
        board[5][randInt] = 'Y'
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
                    validMove = False
                    mouseX, mouseY = pygame.mouse.get_pos()
                    mouseX = trunc((mouseX - 20) / 40)
                    if board[0][mouseX] != '':
                        continue
                else:
                    #run the minimax function, print the number of nodes that are explored and the time it took to explore them
                    timeOne = time.time()
                    global nodes
                    nodes = 0
                    global cutBranches
                    cutBranches = 0
                    depthAdditive = 0
                    for i in range(7):
                        if board[0][i] != '':
                            depthAdditive += 1
                    if depthAdditive == 0:
                        maxDepth = 6
                    elif depthAdditive == 1:
                        maxDepth = 7
                    elif depthAdditive == 2:
                        maxDepth = 8
                    elif depthAdditive == 3:
                        maxDepth = 11
                    elif depthAdditive == 4:
                        maxDepth = 18
                    mouseX = bestMove(board, 0, maxDepth, True, -1000, 1000, 0, 0, currentMove, nextMove)
                    print(f"\n{nodes} Nodes ({cutBranches} Branches Cut) Searched in ",end='')
                    timeTwo = time.time()
                    timeDiff = round(1000 * (timeTwo - timeOne))
                    print(f"{timeDiff} Miliseconds At A Depth Of {maxDepth}")
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
                        break
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
                
                #check to see if the board is empty, if not the game is a tie
                boardFull = True
                for i in range(7):
                    if board[0][i] == '':
                        boardFull = False
                        break
                if boardFull == True:
                    run = False

                #swap the turn
                storeMove = currentMove
                currentMove = nextMove
                nextMove = storeMove

                if run == False:
                    break
            #print the board
            printBoard(board)

    flashBoard(board)
    if winner == 'Y':
        print("\033[93mAI Wins")
    elif winner == 'R':
        print("\033[91mPlayer Wins")
    else:
        print("It's A Tie!")

if __name__ == '__main__':
    main()
