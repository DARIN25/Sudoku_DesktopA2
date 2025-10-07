idSize = 50
gridNumSize = 100
selectRow = -1
selectCol = -1
selectNum = 0
grid = [[0 for _ in range(9)] for _ in range(9)]
locked = [[False for _ in range(9)] for _ in range(9)]


def setup():
    size(1000,500)


def draw():
    background(255)
    drawGrid()
    drawNumpadGrid()

def drawGrid():
    stroke(0)
    i=0
    while i<=9:
        if i%3==0:
            strokeWeight(3)
        else:
            strokeWeight(1)
        line(i*gridSize, 0, i*gridSize, 9*gridSize)
        line(0, i*gridSize, 9*gridSize, i*gridSize)
        i+=1
        
        
def drawNumpadGrid():
    stroke(0)
    strokeWeight(3)
    i=0
    while i<4:
        line(i*gridNumSize+600,0,i*gridNumSize+600,4*gridNumSize)
        i+=1
    i=0
    while i<5:
        line(600,i*gridNumSize,3*gridNumSize+600,i*gridNumSize)
        i+=1
    
