import pyautogui
import keyboard
import time

img = pyautogui.screenshot(region=(0, 0, 2560, 1440))
num1 = 54, 75, 165
num2 = 47, 147, 82
num3 = 175, 44, 44
num4 = 137, 54, 165
num5 = 110, 58, 58
num6 = 86, 156, 184
num7 = 48, 89, 105
none = 98, 120, 142
field = 112, 128, 144

# mine ist gleich 10
#felder sind 55, 55 pixel groß

rows = 16
cols = 30

def makeBoard():    # 16x30
    board = []
    for _ in range(cols):
        row = [0] * rows
        board.append(row)
    return board

def updateBoard(board):
    _, _ = img.size
    for i in range(len(board)):
        for j in range(len(board[i])):
            x = 460 + 56 * i
            y = 257 + 56 * j
            pixel = img.getpixel((x, y))
            if pixel != (255, 255, 255):
                board[i][j] = 0
            if pixel == num1:
                board[i][j] = 1
            if pixel == num2:
                board[i][j] = 2
            if pixel == num3:
                board[i][j] = 3
            if pixel == num4:
                board[i][j] = 4
            if pixel == num5:
                board[i][j] = 5
            if pixel == num6:
                board[i][j] = 6
            if pixel  == num7:
                board[i][j] = 7
            if pixel == none:
                board[i][j] = 9

    return board


pyautogui.click(500, 500)  # Click to start the game
def findSafe(board):
    for i in range(len(board)):
        for j in range(len(board[i])):


def findMine(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            freeSquares = []
            for num in range(1, 8):
                if board[i][j] == num:
                    if j+1 < len(board[i]) and board[i][j+1] == 0:
                        freeSquares.append((i, j+1))
                    if j-1 >= 0 and board[i][j-1] == 0:
                        freeSquares.append((i, j-1))
                    if i+1 < len(board) and board[i+1][j] == 0:
                        freeSquares.append((i+1, j))
                    if i-1 >= 0 and board[i-1][j] == 0:
                        freeSquares.append((i-1, j))
                    if i+1 < len(board) and j+1 < len(board[i]) and board[i+1][j+1] == 0:
                        freeSquares.append((i+1, j+1))
                    if i-1 >= 0 and j-1 >= 0 and board[i-1][j-1] == 0:
                        freeSquares.append((i-1, j-1))
                    if i+1 < len(board) and j-1 >= 0 and board[i+1][j-1] == 0:
                        freeSquares.append((i+1, j-1))
                    if i-1 >= 0 and j+1 < len(board[i]) and board[i-1][j+1] == 0:
                        freeSquares.append((i-1, j+1))
                    if len(freeSquares) == num:
                        for square in freeSquares:
                            board[square[0]][square[1]] = 10
                            return board
                        break
                    freeSquares.clear()
    return board

def clickSafe(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            # If the field is not a mine, click it
            if board[i][j] != 10:
                pyautogui.click(460 + 56 * i, 257 + 56 * j)
    return board           
                
board = makeBoard()

while True:
    board = updateBoard(board)
    board = findMine(board)
    board = findSafe(board)
    board = clickSafe(board)
    time.sleep(1)  # Wait for initial setup
    if keyboard.is_pressed('q'):
        print("Stopping...")
        break


