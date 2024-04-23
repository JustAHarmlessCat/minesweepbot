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
    img = pyautogui.screenshot(region=(0, 0, 2560, 1440))  # Take a new screenshot each time the function is called
    width, height = img.size  # Get the dimensions of the screenshot
    for i in range(len(board)):
        for j in range(len(board[i])):
            x = startpointx + fieldsize * i
            y = startpointy + fieldsize * j
            # Check if the coordinates are within the dimensions of the screenshot
            if x < width and y < height:
                pixel = img.getpixel((x, y))
                # Use a dictionary to map colors to cell values
                color_to_value = {
                    num1: 1,
                    num2: 2,
                    num3: 3,
                    num4: 4,
                    num5: 5,
                    num6: 6,
                    num7: 7,
                    field: 9,
                    none: 20,
                }
                # Default to 0 if the pixel color is not recognized
                board[i][j] = color_to_value.get(pixel, 0)
    print("Board updated.")
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
                if mine_count == board[i][j] and not potential_mines:
                    for square in safe_squares:
                        board[square[0]][square[1]] = 15
    return board
            
def findMine(board):
    print("Finding mines...")
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
    print("Mines found.")
    return board

def clickSafe(board):
    print("Clicking safe squares...")
    for i in range(len(board)):
        for j in range(len(board[i])):
            # If the field is safe, click it
            if board[i][j] == 15:
                pyautogui.click(startpointx + fieldsize * i, startpointy + fieldsize * j)
    return board

board = makeBoard()

monitor = get_monitors()[0]
resolution = monitor.width, monitor.height

if resolution == (2560, 1440):
    fieldsize = 57
    startpointx = 444
    startpointy = 255
else: 
    fieldsize = 45
    startpointx = 335
    startpointy = 180

print("Starting...")
time.sleep(2)
pyautogui.click(500, 500)
    
while True:
    print("Updating, finding mines, and clicking safe squares...")
    board = updateBoard(board)
    time.sleep(2)
    board = findMine(board)
    board = findSafe(board)
    board = clickSafe(board)
    print("Update, find, and click complete.")
    print(board)
    if keyboard.is_pressed('q'):
        print("Stopping...")
        break