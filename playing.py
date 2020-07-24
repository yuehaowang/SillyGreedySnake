import random

from pylash.core import stage, init, addChild, KeyCode
from pylash.loaders import LoadManage
from pylash.display import Sprite, BitmapData, Bitmap, FPS, TextField, TextFormatWeight
from pylash.events import MouseEvent, LoopEvent, KeyboardEvent
from pylash.media import Sound, MediaEvent
from pylash.ui import LoadingSample1, Button

score1 = 1
score2 = 0

gameBoard = []
candies = {}

for i in range(50):
    gameBoard.append([])
    for j in range(50):
        gameBoard[i].append(None)

class snake(Sprite):
    def __init__(self, snakeKind, startX, startY, direction):
        super(snake, self).__init__()

        self.snakeKind = snakeKind
        self.direction = direction
        self.startX = startX
        self.startY = startY
        self.speed = 1
        self.foodNumber = 0
        self.head = {
            "Up" : Bitmap(BitmapData(dataList[self.snakeKind+"HeadUp"])),
            "Down" : Bitmap(BitmapData(dataList[self.snakeKind+"HeadDown"])),
            "Left" : Bitmap(BitmapData(dataList[self.snakeKind+"HeadLeft"])),
            "Right" : Bitmap(BitmapData(dataList[self.snakeKind+"HeadRight"]))
        }
        for i in self.head:
            playingLayer.addChild(self.head[i])
            self.head[i].visible = False

        self.items = [self.head[self.direction]]
        self.items[0].x = self.startX
        self.items[0].y = self.startY
        self.items[0].visible = True
        playingLayer.addChild(self.items[0])
        if (startX/10-1 >= 0) and (startY/10-13 >= 0):
            gameBoard[int(startY/10-13)][int(startX/10-1)] = "head"

        if self.direction == "Up":
            for i in range(5):
                self.addBody(self.startY/10+1+i, self.startX/10)
        elif  self.direction == "Down":
            for i in range(5):
                self.addBody(self.startY/10-1-i, self.startX/10)
        elif self.direction == "Left":
            for i in range(5):
                self.addBody(self.startY/10, self.startX/10+1+i)
        elif self.direction == "Right":
            for i in range(5):
                self.addBody(self.startY/10, self.startX/10-1-i)

    def addBody(self, row, col):
        item = Bitmap(BitmapData(dataList[self.snakeKind+"Body"]))
        item.x = col*10
        item.y = row*10
        playingLayer.addChild(item)
        self.items.append({"row":row, "col":col, "item":item})
        row = int(row-13)
        col = int(col-1)
        if (row >= 0) and (col >= 0):
            gameBoard[row][col] = self.snakeKind
    
    def move(self):
        # head style
        lastHead = self.items[0]
        lastHead.visible = False
        self.items[0] = self.head[self.direction]
        self.items[0].x = lastHead.x
        self.items[0].y = lastHead.y
        self.items[0].visible = True
        
        if self.direction == "Up":
            pass
        elif self.direction == "Down":
            pass
        elif self.direction == "Left":
            pass
        elif self.direction == "Right":
            pass
    
    def analyze(self):
        return "normal"

    def loop(self):
        state = self.analyze()
        if state == "normal":
            self.move()
        elif state == "meetCandy":
            pass
        elif (state == "meetHead") or (state == "meetBody") or (state == "meetWall"):
            gameOver(state, self.snakeKind)

        



def gameStart(data, bgmPlay, effectsPlay, p1Profile, p2Profile):
    global dataList, playingLayer

    # receive the loaded data
    dataList = data

    # create the playing layer
    playingLayer = Sprite()
    addChild(playingLayer)

    # set the bg image
    playingBg = Bitmap(BitmapData(dataList["playingBg"], 0, 0, 520, 640))
    playingLayer.addChild(playingBg)

    # add profiles
    profile1 = Bitmap(BitmapData(dataList["profile%s" % p1Profile]))
    profile1.x = 20
    profile1.y = 20
    profile1.width = 100
    profile1.height = 100
    playingLayer.addChild(profile1)

    profile2 = Bitmap(BitmapData(dataList["profile%s" % p2Profile]))
    profile2.x = 400
    profile2.y = 20
    profile2.width = 100
    profile2.height = 100
    playingLayer.addChild(profile2) # display the scores
    colon = TextField()
    colon.text = ":"
    colon.size = 50
    colon.x = 260 - colon.width/2
    colon.y = 70 - colon.height/2
    colon.textColor = "#225590"
    colon.font = "Bradley Hand"
    playingLayer.addChild(colon)

    score1Txt = TextField()
    score1Txt.text = "%s" % score1
    score1Txt.size = 50
    score1Txt.x = 260 - 20 - score1Txt.width
    score1Txt.y = 70 - score1Txt.height/2
    score1Txt.textColor = "#225590"
    score1Txt.font = "Bradley Hand"
    playingLayer.addChild(score1Txt)

    score2Txt = TextField()
    score2Txt.text = "%s" % score2
    score2Txt.size = 50
    score2Txt.x = 260 + 20
    score2Txt.y = 70 - score2Txt.height/2
    score2Txt.textColor = "#225590"
    score2Txt.font = "Bradley Hand"
    playingLayer.addChild(score2Txt)

    # add sample snakes
    sampleSnake1 = snake("snake1", 130, 40, "Up")
    sampleSnake2 = snake("snake2", 380, 40, "Up")

    global snake1, snake2
    # create game snakes
    snake1 = snake("snake1", 60, 180, "Right")
    snake2 = snake("snake2", 450, 570, "Left")

    stage.addEventListener(KeyboardEvent.KEY_DOWN, keyDown)
    stage.addEventListener(KeyboardEvent.KEY_UP, keyUp)
    playingLayer.addEventListener(LoopEvent.ENTER_FRAME, loop)

def keyDown(e):
    print("KeyDown")
    if e.keyCode == KeyCode.KEY_W:
        if snake1.direction != "Down":
            snake1.direction = "Up"
            snake1.speed = 2 
    elif e.keyCode == KeyCode.KEY_S:
        if snake1.direction != "Up":
            snake1.direction = "Down"
            print("Down")
            snake1.speed = 2
    elif e.keyCode == KeyCode.KEY_A:
        if snake1.direction != "Right":
            snake1.direction = "Left"
            snake1.speed = 2
    elif e.keyCode == KeyCode.KEY_D:
        if snake1.direction != "Left":
            snake1.direction = "Right"
            snake1.speed = 2
    elif e.keyCode == KeyCode.KEY_I:
        if snake2.direction != "Down":
            snake2.direction = "Up"
            snake2.speed = 2
    elif e.keyCode == KeyCode.KEY_K:
        if snake2.direction != "Up":
            snake2.direction = "Down"
            print("Down")
            snake2.speed = 2
    elif e.keyCode == KeyCode.KEY_J:
        if snake2.direction != "Right":
            snake2.direction = "Left"
            snake2.speed = 2
    elif e.keyCode == KeyCode.KEY_L:
        if snake2.direction != "Left":
            snake2.direction = "Right"
            snake2.speed = 2

def keyUp(e):
    print("KeyUp")
    if (e.keyCode == KeyCode.KEY_W) or (e.keyCode == KeyCode.KEY_S) or (e.keyCode == KeyCode.KEY_A) or (e.keyCode == KeyCode.KEY_D):
        snake1.speed = 1
    elif (e.keyCode == KeyCode.KEY_I) or (e.keyCode == KeyCode.KEY_K) or (e.keyCode == KeyCode.KEY_J) or (e.keyCode == KeyCode.KEY_L):
        snake2.speed = 1

def loop(e):
    generate()
    snake1.loop()
    snake2.loop()

def generate():
    global candies
    while (len(candies)/(2500-len(snake1.items)-len(snake2.items)) < 0.05):
        row = random.randint(0, 49)
        col = random.randint(0, 49)

        if (gameBoard[row][col] == None):
            gameBoard[row][col] = "candy"
            candyKind = random.randint(0,3)
            newCandy = Bitmap(BitmapData(dataList["candy%s" % candyKind]))
            newCandy.x = 10 + col*10
            newCandy.y = 130 + row*10
            playingLayer.addChild(newCandy)
            candies[str(row)+"_"+str(col)] = newCandy

def gameOver(overKind, snakeKind):
    if overKind == "meetHead":
        if score1 == score2:
            pass # both lost
        elif score1 > score2:
            pass # p1 won
        elif score1 < score2:
            pass # p2 won
    elif (overKind == "meetBody") or (overKind == "meetWall"):
        if snakeKind == "snake1":
            pass # p1 lost
        elif snakeKind == "snake2":
            pass # p2 lost
