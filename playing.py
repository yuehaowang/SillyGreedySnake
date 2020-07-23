from pylash.core import stage, init, addChild, KeyCode
from pylash.loaders import LoadManage
from pylash.display import Sprite, BitmapData, Bitmap, FPS, TextField, TextFormatWeight
from pylash.events import MouseEvent, LoopEvent, KeyboardEvent
from pylash.media import Sound, MediaEvent
from pylash.ui import LoadingSample1, Button

score1 = 100
score2 = 0

class snake(Sprite):
    def __init__(self, snakeKind, startX, startY, direction):
        super(snake, self).__init__()

        self.snakeKind = snakeKind
        self.items = []
        self.direction = direction
        self.startX = startX
        self.startY = startY
        self.speed = 1

        self.item = [Bitmap(BitmapData(dataList[self.snakeKind+"Head"+self.direction]))]
        self.item[0].x = self.startX
        self.item[0].y = self.startY
        playingLayer.addChild(self.item[0])

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

        # if (snakeKind == "snake1"):
        #     head = Bitmap(BitmapData(dataList["snake1Head"+self.direction]))
        #     head.x = startX + 14*10
        #     head.y = startY + 44*10
        #     playingLayer.addChild(head)
        #     self.addBody(45, 14)
        #     self.addBody(46, 14)
        #     self.addBody(47, 14)
        #     self.addBody(48, 14)
        #     self.addBody(49, 14)
        # else:
        #     self.direction = "Down"
        #     head = Bitmap(BitmapData(dataList["snake2Head"+self.direction]))
        #     head.x = 10 + 35*10
        #     head.y = 130 + 5*10
        #     playingLayer.addChild(head)
        #     self.addBody(4, 35)
        #     self.addBody(3, 35)
        #     self.addBody(2, 35)
        #     self.addBody(1, 35)
        #     self.addBody(0, 35)

    def addBody(self, row, col):
        item = Bitmap(BitmapData(dataList[self.snakeKind+"Body"]))
        item.x = col*10
        item.y = row*10
        playingLayer.addChild(item)
        self.items.append({"row":row, "col":col, "item":item})
        


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
    playingLayer.addChild(profile2)# display the scores
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

    # create game snakes
    snake1 = snake("snake1", 60, 180, "Right")
    snake2 = snake("snake2", 450, 590, "Left")



