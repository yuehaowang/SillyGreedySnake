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

gameContinue = True

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
        self.eatenCandies = []
        self.heads = {
            "Up" : Bitmap(BitmapData(dataList[self.snakeKind+"HeadUp"])),
            "Down" : Bitmap(BitmapData(dataList[self.snakeKind+"HeadDown"])),
            "Left" : Bitmap(BitmapData(dataList[self.snakeKind+"HeadLeft"])),
            "Right" : Bitmap(BitmapData(dataList[self.snakeKind+"HeadRight"]))
        }
        for i in self.heads:
            playingLayer.addChild(self.heads[i])
            self.heads[i].visible = False
        self.items = [{"row":int(self.startY/10)-13, "col":int(self.startX/10)-1, "item":self.heads[self.direction]}]
        self.items[0]["item"].x = self.startX
        self.items[0]["item"].y = self.startY
        self.items[0]["item"].visible = True
        playingLayer.addChild(self.items[0]["item"])

        if (startX/10-1 >= 0) and (startY/10-13 >= 0):
            gameBoard[int(startY/10-13)][int(startX/10-1)] = "head"

        if self.direction == "Up":
            for i in range(5):
                self.addBody(self.startY+(1+i)*10, self.startX)
        elif  self.direction == "Down":
            for i in range(5):
                self.addBody(self.startY+(-1-i)*10, self.startX)
        elif self.direction == "Left":
            for i in range(5):
                self.addBody(self.startY, self.startX+(1+i)*10)
        elif self.direction == "Right":
            for i in range(5):
                self.addBody(self.startY, self.startX+(-1-i)*10)

    def addBody(self, y, x):
        item = Bitmap(BitmapData(dataList[self.snakeKind+"Body"]))
        item.x = x
        item.y = y
        playingLayer.addChild(item)
        self.items.append({"row":int(y/10)-13, "col":int(x/10)-1, "item":item}) # the row and col is wrt the gameBoard
        if (y/10-13 >= 0) and (x/10-1 >= 0):
            gameBoard[int(y/10-13 >= 0)][int(x/10-1 >= 0)] = self.snakeKind
    
    def move(self):
        # head style
        lastHead = self.items[0]["item"]
        lastHead.visible = False
        self.items[0]["item"] = self.heads[self.direction]
        self.items[0]["item"].x = lastHead.x
        self.items[0]["item"].y = lastHead.y
        self.items[0]["item"].visible = True
        
        for i in range(len(self.items)-1, -1, -1):
            # clear gameBoard
            gameBoard[int(self.items[i]["row"])][int(self.items[i]["col"])] = None
            if (i - self.speed >= 0):
                # update images' position
                self.items[i]["item"].x = self.items[i-self.speed]["item"].x
                self.items[i]["item"].y = self.items[i-self.speed]["item"].y
                # update the dictionary's row and col
                self.items[i]["row"] = self.items[i-self.speed]["row"]
                self.items[i]["col"] = self.items[i-self.speed]["col"]
            else:
                if self.direction == "Up":
                    # update images' position
                    self.items[i]["item"].x = self.items[0]["item"].x
                    self.items[i]["item"].y = self.items[0]["item"].y - (self.speed-i) * 10
                    # update the dictionary's row and col
                    self.items[i]["col"] = self.items[0]["col"]
                    self.items[i]["row"] = self.items[0]["row"] - (self.speed-i)
                elif self.direction == "Down":
                    # update images' position
                    self.items[i]["item"].x = self.items[0]["item"].x
                    self.items[i]["item"].y = self.items[0]["item"].y + (self.speed-i) * 10
                    # update the dictionary's row and col
                    self.items[i]["col"] = self.items[0]["col"]
                    self.items[i]["row"] = self.items[0]["row"] + (self.speed-i)
                elif self.direction == "Left":
                    # update images' position
                    self.items[i]["item"].x = self.items[0]["item"].x - (self.speed-i) * 10
                    self.items[i]["item"].y = self.items[0]["item"].y
                    # update the dictionary's row and col
                    self.items[i]["col"] = self.items[0]["col"] - (self.speed-i)
                    self.items[i]["row"] = self.items[0]["row"]
                elif self.direction == "Right":
                    # update images' position
                    self.items[i]["item"].x = self.items[0]["item"].x + (self.speed-i) * 10
                    self.items[i]["item"].y = self.items[0]["item"].y
                    # update the dictionary's row and col
                    self.items[i]["col"] = self.items[0]["col"] + (self.speed-i)
                    self.items[i]["col"] = self.items[0]["col"]
            # Update the gameBoard
            if (i == 0):
                gameBoard[int(self.items[i]["row"])][int(self.items[i]["col"])] = "head"
                if self.direction == "Up":
                    nextHeadRow = self.items[0]["row"] - 1
                    nextHeadCol = self.items[0]["col"]
                elif self.direction == "Down":
                    nextHeadRow = self.items[0]["row"] + 1
                    nextHeadCol = self.items[0]["col"]
                elif self.direction == "Left":
                    nextHeadRow = self.items[0]["row"]
                    nextHeadCol = self.items[0]["col"] - 1
                elif  self.direction == "Right":
                    nextHeadRow = self.items[0]["row"]
                    nextHeadCol = self.items[0]["col"] + 1
            else:
                gameBoard[int(self.items[i]["row"])][int(self.items[i]["col"])] = self.snakeKind

        return (nextHeadRow, nextHeadCol)
    def growth(self):
        pass



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

    generate(0.05)

def keyDown(e):
    if e.keyCode == KeyCode.KEY_W:
        snake1.direction = "Up"
        snake1.speed = 3
    elif e.keyCode == KeyCode.KEY_S:
        snake1.direction = "Down"
        snake1.speed = 3
    elif e.keyCode == KeyCode.KEY_A:
        snake1.direction = "Left"
        snake1.speed = 3
    elif e.keyCode == KeyCode.KEY_D:
        snake1.direction = "Right"
        snake1.speed = 3
    elif e.keyCode == KeyCode.KEY_I:
        snake2.direction = "Up"
        snake2.speed = 3
    elif e.keyCode == KeyCode.KEY_K:
        snake2.direction = "Down"
        snake2.speed = 3
    elif e.keyCode == KeyCode.KEY_J:
        snake2.direction = "Left"
        snake2.speed = 3
    elif e.keyCode == KeyCode.KEY_L:
        snake2.direction = "Right"
        snake2.speed = 3

def keyUp(e):
    if (e.keyCode == KeyCode.KEY_W) or (e.keyCode == KeyCode.KEY_S) or (e.keyCode == KeyCode.KEY_A) or (e.keyCode == KeyCode.KEY_D):
        snake1.speed = 1
    elif (e.keyCode == KeyCode.KEY_I) or (e.keyCode == KeyCode.KEY_K) or (e.keyCode == KeyCode.KEY_J) or (e.keyCode == KeyCode.KEY_L):
        snake2.speed = 1

def loop(e):
    minRatio = 0.02
    while (len(candies)/(2500-len(snake1.items)-len(snake2.items)) < minRatio):
        generate(0.05)

    if gameContinue:
        snakeLoop(snake1, snake2)
    if gameContinue:
        snakeLoop(snake2, snake1)

def snakeLoop(s1, s2):
    normal = True
    # record the position of s2
    s2Position = []
    # compute the next position of s2
    nextS2Position = {}
    for i in range(len(s2.items)-1, -1, -1):
        s2Position.append((s2.items[i]["row"], s2.items[i]["col"]))

        if (i - s2.speed >= 0):
            # update the dictionary's row and col
            row = s2.items[i-s2.speed]["row"]
            col = s2.items[i-s2.speed]["col"]
        else:
            if s2.direction == "Up":
                # update the dictionary's row and col
                col = s2.items[0]["col"]
                row = s2.items[0]["row"] - (s2.speed-i)
            elif s2.direction == "Down":
                # update the dictionary's row and col
                col = s2.items[0]["col"]
                row = s2.items[0]["row"] + (s2.speed-i)
            elif s2.direction == "Left":
                # update the dictionary's row and col
                col = s2.items[0]["col"] - (s2.speed-i)
                row = s2.items[0]["row"]
            elif s2.direction == "Right":
                # update the dictionary's row and col
                col = s2.items[0]["col"] + (s2.speed-i)
                row = s2.items[0]["col"]
        col = int(col)
        row = int(row)
        if (i == 0):
            nextS2Position[str(row)+"_"+str(col)] = "head"
        else:
            nextS2Position[str(row)+"_"+str(col)] = "body"

    # check
    head = False
    body = False
    for i in range(s1.speed):
        if s1.direction == "Up":
            row = s1.items[0]["row"]-1-i
            col = s1.items[0]["col"]
        elif s1.direction == "Down":
            row = s1.items[0]["row"]+1+i
            col = s1.items[0]["col"]
        elif s1.direction == "Left":
            row = s1.items[0]["row"]
            col = s1.items[0]["col"]-1-i
        elif s1.direction == "Right":
            row = s1.items[0]["row"]
            col = s1.items[0]["col"]+1+i

        row = int(row)
        col = int(col)
        if ((row < 0 or row > 49) or (col < 0 or col > 49)):
            gameOver("wall", s1.snakeKind, s2Position)
            normal = False
        elif (str(row)+"_"+str(col) in nextS2Position):
            print("in")
            if nextS2Position[str(row)+"_"+str(col)] == "head":
                head = True
            elif nextS2Position[str(row)+"_"+str(col)] == "body":
                body = True
            normal = False
        elif (gameBoard[row][col] == "candy"):
            pass # eat candy
    if head:
        gameOver("head", s1.snakeKind, s2Position)
    elif body:
        gameOver("body", s1.snakeKind, s2Position)
    elif normal:
        s1.move()


def generate(ratio):
    global candies
    while (len(candies)/(2500-len(snake1.items)-len(snake2.items)) < ratio):
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

def gameOver(overKind, snakeKind, s2Position):
    playingLayer.removeAllEventListeners()
    if overKind == "head":
        if score1 == score2:
            print("both lost")
        elif score1 > score2:
            print("2333p1 won")
        elif score1 < score2:
            print("abc p2 won")
    elif (overKind == "body") or (overKind == "wall"):
        if snakeKind == "snake1":
            snake = snake1
            print("134 p2 won")
        elif snakeKind == "snake2":
            print("189 p1 won")
    if snakeKind == "snake1":
        snake = snake1
    else:
        snake = snake2

    snake.speed = 1
    snake.eatenCandies = []
    while not((snake.items[0]["row"], snake.items[0]["col"]) in s2Position):
        if (snake.items[0]["row"] <= 0 or snake.items[0]["row"] >= 49) or (snake.items[0]["col"] <= 0 or snake.items[0]["col"] >= 49):
            break
        nextHead = snake.move()
        if nextHead in s2Position:
            break
    global gameContinue
    gameContinue = False