import pyautogui

img = pyautogui.screenshot(region=(0, 0, 1920, 1080))
num1 = 54, 75, 165
num2 = 47, 147, 82
num3 = 175, 44, 44
num4 = 137, 54, 165
num5 = 110, 58, 58
num6 = 86, 156, 184


def makeBoard(rows, cols):
    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        board.append(row)
    return board

def whatIsThis(x, y):
    for i in range (1, 6):
        if (str(i) + '.png'):                  #hier noch vergleichen pixel mit dem wo das ist
            return i
        else: return 0

def updateBoard(board, img):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if img.getpixel(keine ahnung wie ich hier wat bekomme) !== (255, 255, 255):       #keine ahnung wie ich weiß bei welchem pixel das ist
                board[i][j] = 0

rows = input("Enter the number of rows: ")
cols = input("Enter the number of columns: ")

print('\n'.join(map(str, makeBoard(int(rows), int(cols)))))

board = makeBoard(int(rows), int(cols))
pyautogui.click(500, 500)	# Clicks on the screen to start the game
