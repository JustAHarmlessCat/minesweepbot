import pyautogui
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
    for i in range(cols):
        row = []
        for j in range(rows):
            row.append(0)
        board.append(row)
    return board

def updateBoard(board):
    width, height = img.size
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
#print('\n'.join(map(str, makeBoard(int(rows), int(cols)))))
board = makeBoard()

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

def clickSafe(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            # Check surrounding fields for a mine
            surrounding_fields = [(i-1, j-1), (i-1, j), (i-1, j+1),
                                  (i, j-1),                 (i, j+1),
                                  (i+1, j-1), (i+1, j), (i+1, j+1)]

            for field in surrounding_fields:
                x, y = field
                # Check if coordinates are within the board
                if 0 <= x < len(board) and 0 <= y < len(board[i]):
                    # If the field is a mine, continue to the next field
                    if board[x][y] == 10:
                        continue
                    # If the field is not a mine, click it
                    else:
                        pyautogui.click(460 + 56 * x, 257 + 56 * y)
    return board            
                


while True:
    board = updateBoard(board)
    board = findMine(board)
    board = clickSafe(board)
    time.sleep(1)  # Wait for initial setup
    if pyautogui.isPressed('q'):
        print("Stopping...")
        break


