grid = [[0]*9 for _ in range(9)]
locked = [[False]*9 for _ in range(9)]
gridSize = 50
gridNumSize = 100
selectRow = -1
selectCol = -1
selectNum = 0
answer = True
stage = False
dificulty = 0
menuY = 0

def setup():
    global stage, menuY
    size(1000, 500)
    stage = False
    menuY = height

def draw():
    global menuY
    if not stage:
        if menuY < height:
            menuY += 20
        else:
            background(0)
        openMenu()
    if stage:
        background(255)
        drawGameUI()
        drawGrid()
        drawNum()
        drawNumpadGrid()
        drawNumpadNum()
        drawSaveButton()
        drawMenuButton()
        openMenu()
        if menuY > 0:
            openMenu()
            menuY -= 20

def drawGrid():
    stroke(0)
    i = 0
    while i <= 9:
        if i % 3 == 0:
            strokeWeight(3)
        else:
            strokeWeight(1)
        line(i*gridSize, 0, i*gridSize, 9*gridSize)
        line(0, i*gridSize, 9*gridSize, i*gridSize)
        i += 1

def drawNum():
    textAlign(CENTER, CENTER)
    textSize(24)
    fill(0)
    row = 0
    while row < 9:
        col = 0
        while col < 9:
            if grid[row][col] != 0:
                text(str(grid[row][col]), col*gridSize + gridSize//2, row*gridSize + gridSize//2)
            col += 1
        row += 1

def drawNumpadGrid():
    stroke(0)
    strokeWeight(3)
    i = 0
    while i < 4:
        line(i*gridNumSize + 600, 0, i*gridNumSize + 600, 4*gridNumSize)
        i += 1
    i = 0
    while i < 5:
        line(600, i*gridNumSize, 3*gridNumSize + 600, i*gridNumSize)
        i += 1

def drawNumpadNum():
    textAlign(CENTER, CENTER)
    textSize(30)
    fill(0)
    numpadNum = 1
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            text(str(numpadNum), j*gridNumSize + 600 + (gridNumSize//2), i*gridNumSize + (gridNumSize//2))
            numpadNum += 1
            j += 1
        i += 1
    text("-", 600 + gridNumSize + gridNumSize//2, 3*gridNumSize + gridNumSize//2)

def mousePressed():
    global stage, selectRow, selectCol, selectNum, answer
    if not stage:
        if mouseX >= width/2 - 100 and mouseY >= menuY - 270 and mouseX <= width/2 + 100 and mouseY <= menuY - 230:
            stage = True
            newGame()
        if mouseX >= width/2 - 100 and mouseY >= menuY - 220 and mouseX <= width/2 + 100 and mouseY <= menuY - 180:
            stage = True
            selectInput("Select game file: ", "fileSelected")
    if stage:
        if mouseY < 9*gridSize and mouseX < 9*gridSize:
            r = int(mouseY // gridSize)
            c = int(mouseX // gridSize)
            if not locked[r][c]:
                selectCol = c
                selectRow = r
                answer = True
            else:
                print("Can't change this number")
        if mouseY < 400 and mouseX > 600 and mouseX < 900:
            if mouseY < 100:
                if mouseX < 700:
                    selectNum = 1
                elif mouseX < 800:
                    selectNum = 2
                else:
                    selectNum = 3
            elif mouseY < 200:
                if mouseX < 700:
                    selectNum = 4
                elif mouseX < 800:
                    selectNum = 5
                else:
                    selectNum = 6
            elif mouseY < 300:
                if mouseX < 700:
                    selectNum = 7
                elif mouseX < 800:
                    selectNum = 8
                else:
                    selectNum = 9
            else:
                if 700 < mouseX < 800:
                    selectNum = 0
        if selectRow != -1 and selectCol != -1:
            if selectNum == 0 or checkValid(grid, selectNum, selectRow, selectCol):
                grid[selectRow][selectCol] = selectNum
                selectNum = 0
                answer = True
            else:
                selectNum = 0
                print("Invalid number")
                answer = False
        if mouseX >= width/2 + gridNumSize and mouseY >= height - 70 and mouseX <= width/2 + gridNumSize*2 and mouseY <= height - 30:
            saveGame()
        if mouseX >= width/2 + gridNumSize*3 and mouseY >= height - 70 and mouseX <= width/2 + gridNumSize*4 and mouseY <= height - 30:
            global stage
            stage = False

def checkValid(arr, num, row, col):
    i = (row // 3) * 3
    while i < (row // 3) * 3 + 3:
        j = (col // 3) * 3
        while j < (col // 3) * 3 + 3:
            if arr[i][j] == num and not (i == row and j == col):
                return False
            j += 1
        i += 1
    j = 0
    while j < 9:
        if j != col and arr[row][j] == num:
            return False
        j += 1
    i = 0
    while i < 9:
        if i != row and arr[i][col] == num:
            return False
        i += 1
    return True

def shuffleArray(arr):
    import random
    i = len(arr) - 1
    while i > 0:
        j = int(random.random() * (i + 1))
        arr[i], arr[j] = arr[j], arr[i]
        i -= 1

def generateFullBoard(board):
    row = 0
    while row < 9:
        col = 0
        while col < 9:
            if board[row][col] == 0:
                numbers = [1,2,3,4,5,6,7,8,9]
                shuffleArray(numbers)
                i = 0
                while i < len(numbers):
                    n = numbers[i]
                    if checkValid(board, n, row, col):
                        board[row][col] = n
                        if generateFullBoard(board):
                            return True
                        board[row][col] = 0
                    i += 1
                return False
            col += 1
        row += 1
    return True

def newGame():
    global grid, locked
    full = [[0]*9 for _ in range(9)]
    generateFullBoard(full)
    r = 0
    while r < 9:
        c = 0
        while c < 9:
            grid[r][c] = full[r][c]
            locked[r][c] = True
            c += 1
        r += 1
    holes = 50
    import random
    k = 0
    while k < holes:
        r = int(random.random() * 9)
        c = int(random.random() * 9)
        grid[r][c] = 0
        locked[r][c] = False
        k += 1

def drawGameUI():
    if selectRow != -1 and selectCol != -1:
        if answer:
            fill(200, 200, 255, 100)
        else:
            fill(225, 0, 0, 100)
        noStroke()
        rect(selectCol*gridSize, selectRow*gridSize, gridSize, gridSize)
    row = 0
    while row < 9:
        col = 0
        while col < 9:
            if locked[row][col]:
                fill(225)
                noStroke()
                rect(col*gridSize, row*gridSize, gridSize, gridSize)
            col += 1
        row += 1

def openMenu():
    fill(0)
    rect(0, 0, width, menuY)
    textAlign(CENTER, CENTER)
    textSize(50)
    fill(255)
    text("A2 Sudoku the Game", width//2, menuY - 400)
    textSize(25)
    rect(width//2 - 100, menuY - 270, 200, 40)
    rect(width//2 - 100, menuY - 220, 200, 40)
    fill(0)
    text("New Game", width//2, menuY - 250)
    text("Load Game", width//2, menuY - 200)

def fileSelected(selection):
    if selection is not None:
        print("Loading: " + selection.getAbsolutePath())
        loadGame(selection.getAbsolutePath())

def loadGame(filename):
    lines = loadStrings(filename)
    for r in range(9):
        parts = lines[r].split("|")
        nums = parts[0].strip().split(" ")
        locks = parts[1].strip().split(" ")

        for c in range(9):
            grid[r][c] = int(nums[c])
            locked[r][c] = (int(locks[c]) == 1)
    global stage
    stage = True
    print("Game loaded successfully")

def saveGame():
    selectOutput("Save your Sudoku game:", "fileSaveSelected")

def fileSaveSelected(selection):
    if selection is None:
        print("Save canceled.")
        return

    lines = [None]*9
    for r in range(9):
        row = ""
        for c in range(9):
            row += str(grid[r][c])
            if c < 8:
                row += " "
        row += " | "
        for c in range(9):
            row += "1" if locked[r][c] else "0"
            if c < 8:
                row += " "
        lines[r] = row
    saveStrings(selection.getAbsolutePath(), lines)
    print("Game saved to " + selection.getAbsolutePath())

def drawSaveButton():
    fill(255)
    rect(width//2 + gridNumSize, height - 70, gridNumSize, 40)
    fill(0)
    textSize(20)
    text("Save Game", width//2 + gridNumSize + gridNumSize//2, height - 50)

def drawMenuButton():
    fill(255)
    rect(width//2 + gridNumSize*3, height - 70, gridNumSize, 40)
    fill(0)
    textSize(20)
    text("Menu", width//2 + gridNumSize*3 + gridNumSize//2, height - 50)
