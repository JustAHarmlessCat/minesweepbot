import pyautogui
import time

img = pyautogui.screenshot(region=(0, 0, 2560, 1440))
num1 = 54, 75, 165
num2 = 47, 147, 82
num3 = 175, 44, 44
num4 = 137, 54, 165
num5 = 110, 58, 58
num6 = 86, 156, 184

#felder sind 55, 55 pixel groß

def makeBoard():    # 16x30
    board = []
    for i in range(30):
        row = []
        for j in range(16):
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
    return board

#print('\n'.join(map(str, makeBoard(int(rows), int(cols)))))

pyautogui.click(500, 500)	# Clicks on the screen to start the game
board = makeBoard()
time.sleep(1)                   #iwi will das nicht und mann mus das teil zweimal ausführen damit das loppt
board = updateBoard(board)
print('\n'.join(map(str, board)))