# Author: JustAHarmlessCat

# Contributors:
# - JustAHarmlessCat
# - 1010Jan1010
#

import pyautogui
import keyboard
import time
import random

from screeninfo import get_monitors
pyautogui.PAUSE = 0.001


flags = []
monitor = get_monitors()[0]

def boardSize():
    img = pyautogui.screenshot(region=(0, 0, monitor.width, monitor.height))
    pixel = img.getpixel((470, 240))
    if img.getpixel((1200, 300)) == (0, 0, 0):
        return 9
    if pixel == (112, 128, 144):
        return 30
    else:
        return 16

colors = {
    (54, 75, 165): 1,
    (47, 147, 82): 2,
    (175, 44, 44): 3,
    (137, 54, 165): 4,
    (110, 58, 58): 5,
    (86, 156, 184): 6, 
    (48, 89, 105): 7,
    (98, 120, 142): 20, # 20 is nothing, so the grey
    (112, 128, 144): 9, # 9 is unclicked
}
                              #20 ist nix also das graue
cols = boardSize()
rows = 16
if cols == 9:
    rows = 9

def makeBoard():    # 30x16              #das board wird gemacht
    print("Making board...")
    board = []
    for _ in range(cols):
        col = [0] * rows
        board.append(col)
    print("Board made.")
    return board

def updateBoard(board):
    img = pyautogui.screenshot(region=(0, 0, monitor.width, monitor.height))  
    for i in range(len(board)):
        for j in range(len(board[i])):
            x, y = startpointx + fieldsize * i, startpointy + fieldsize * j
            # print(str(x) + " " + str(y))
            # drawRectangle(x, y, 2, 2)
            
            pixel = img.getpixel((x, y))
          
            wert = colors.get(pixel)
            if wert is not None:
                board[i][j] = wert
            else:
                board = 0
                return board
    return board
            
            

board = makeBoard()

def findSafe(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if 1 <= board[i][j] <= 7:
                mine_count = 0
                safe_squares = []
                potential_mines = []
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:  # Skip the current cell
                            continue
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(board) and 0 <= ny < len(board[i]):
                            if board[nx][ny] == 10:
                                mine_count += 1
                            elif board[nx][ny] == 9:
                                potential_mines.append((nx, ny))
                            else:
                                safe_squares.append((nx, ny))
                if mine_count == board[i][j]:  # If the number of mines equals the number on the square
                    for square in potential_mines:  # Mark the potential mines as safe
                        board[square[0]][square[1]] = 15
    return board
            
def findMine(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if 1 <= board[i][j] <= 7:
                unclicked_count = 0
                mine_count = 0
                unclicked_positions = []
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:  # Skip the current cell
                            continue
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):  # Ensure ny is within bounds
                            if board[nx][ny] == 9:
                                unclicked_count += 1
                                unclicked_positions.append((nx, ny))
                            elif board[nx][ny] == 10:  # Count the number of revealed mines
                                mine_count += 1
                if unclicked_count == board[i][j] - mine_count:  # Subtract the number of revealed mines from the number in the cell
                    for position in unclicked_positions:
                        board[position[0]][position[1]] = 10
    return board



def clickSafe(board):
    clicks = 0
    safe_positions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 15:
                clicks += 1
                safe_positions.append((i, j))

    if clicks == 0:
        # Check if there are any safeclicks on the board
        if not any(15 in row for row in board):
            # Find the nearest number cell
            nearest_number_cell = None
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell not in {9, 10}:  # Assuming 9 represents an empty cell and 10 represents a mine
                        nearest_number_cell = (i, j)
                        break
                if nearest_number_cell:
                    break

            if nearest_number_cell:
                # Mark a tile that is distant 1 from the nearest number cell
                marked_tile = None
                i, j = nearest_number_cell
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(board) and 0 <= ny < len(board[i]) and board[nx][ny] == 9:
                            marked_tile = (nx, ny)
                            break
                    if marked_tile:
                        break

                if marked_tile:
                    x, y = startpointx + fieldsize * marked_tile[0], startpointy + fieldsize * marked_tile[1]
                    # If the field is safe, click it
                    pyautogui.click(x, y)
                else:
                    # Choose a random empty cell
                    empty_cells = [(i, j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell == 9]
                    random_empty_cell = random.choice(empty_cells) if empty_cells else None
                    if random_empty_cell:
                        x, y = startpointx + fieldsize * random_empty_cell[0], startpointy + fieldsize * random_empty_cell[1]
                        # If the field is safe, click it
                        pyautogui.click(x, y)

    for i, j in safe_positions:
        x, y = startpointx + fieldsize * i, startpointy + fieldsize * j
        # If the field is safe, click it
        pyautogui.click(x, y)

    return board

board = makeBoard()

resolution = monitor.width, monitor.height

if resolution == (2560, 1440):
    fieldsize = 56
    if cols == 30:
        startpointx = 444
        startpointy = 237
    elif cols == 16:
        startpointx = 840
        startpointy = 240
    else:
        startpointx = 1031
        startpointy = 438
else: 
    fieldsize = 42
    startpointx = 333
    startpointy = 177

print("Starting...")
pyautogui.click(1282, 665)
board = updateBoard(board)
while True:
    if keyboard.is_pressed('q'):
        print("Stopping...")
        break
    if keyboard.is_pressed('r') or board == 0:
        print("Restarting...")
        pyautogui.keyDown('ctrl')
        pyautogui.keyUp('ctrl')
        pyautogui.click(1282, 665)
        board = makeBoard()
        flags = []
    if board != 0:
        board = updateBoard(board)
    if board != 0:
        board = findMine(board)
        board = findSafe(board)
        board = clickSafe(board)
