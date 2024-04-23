import pyautogui
import keyboard
import time

from screeninfo import get_monitors

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
                              #20 ist nix also das graue
rows = 16
cols = 30

def makeBoard():    # 16x30              #das board wird gemacht
    print("Making board...")
    board = []
    for _ in range(cols):
        row = [0] * rows
        board.append(row)
    print("Board made.")
    return board

def updateBoard(board):              #wird halt geupdated
    print("Updating board...")
    width, height = img.size
    for i in range(len(board)):
        for j in range(len(board[i])):
            x = startpointx + fieldsize * i
            y = startpointy + fieldsize * j
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
            if pixel == field:
                board[i][j] = 9
            if pixel == none:
                board[i][j] = 20
    print("Board updated.")
    return board

board = makeBoard()

def findSafe(board):
    print("Finding safe squares...")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if 1 <= board[i][j] <= 7:
                mine_count = 0
                safe_squares = []
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(board) and 0 <= ny < len(board[i]) and board[nx][ny] == 10:
                            mine_count += 1
                        if 0 <= nx < len(board) and 0 <= ny < len(board[i]) and board[nx][ny] == 9:
                            safe_squares.append((nx, ny))
                if mine_count == board[i][j]:
                    for square in safe_squares:
                        board[square[0]][square[1]] = 15
    return board
            

def findMine(board):
    print("Finding mines...")
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
    print("Mines found.")
    return board

def clickSafe(board):
    print("Clicking safe squares...")
    for i in range(len(board)):
        for j in range(len(board[i])):
            # If the field is not a mine, click it
            if board[i][j] == 15:
                pyautogui.click(startpointx + fieldsize * i, startpointy + fieldsize * j)
    return board

board = makeBoard()

monitor = get_monitors()[0]
resolution = monitor.width, monitor.height

if resolution == (2560, 1440):
    fieldsize = 56
    startpointx = 460
    startpointy = 257
else: 
    fieldsize = 45
    startpointx = 335
    startpointy = 180

print("Starting...")
time.sleep(2)
pyautogui.click(500, 500)
async def gameloop():
    print("Updating, finding mines, and clicking safe squares...")
    board = await updateBoard(board)
    board = await findMine(board)
    board = await findSafe(board)
    board = await clickSafe(board)
    print("Update, find, and click complete.")
    print(board)
    await time.sleep(1)  # Wait for initial setup
    
while True:
    gameloop()
    break
    if keyboard.is_pressed('q'):
        print("Stopping...")
        break