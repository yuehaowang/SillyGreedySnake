from pylash.core import stage, init, addChild, KeyCode
from pylash.loaders import LoadManage
from pylash.display import Sprite, BitmapData, Bitmap, FPS, TextField, TextFormatWeight
from pylash.events import MouseEvent, LoopEvent, KeyboardEvent
from pylash.media import Sound, MediaEvent
from pylash.ui import LoadingSample1, Button

def initSettingPage(dataList):
    # add the setting layer
    settingLayer = Sprite()
    addChild(settingLayer)

    # add the bg image
    settingBg = Bitmap(BitmapData(dataList["settingBg"]))
    settingLayer.addChild(settingBg)

    # add the profile choices
    profiles = [
        Bitmap(BitmapData(dataList["profile0"])),
        Bitmap(BitmapData(dataList["profile1"])),
        Bitmap(BitmapData(dataList["profile2"]))
    ]
    for i in range(len(profiles)):
        profiles[i].x = 20 + i*165
        profiles[i].y = 165
        settingLayer.addChild(profiles[i])

    # add the hintTxt
    hintTxt = TextField()
    hintTxt.text = "<- and -> for switching the profile, and space for determining"
    hintTxt.size = 18
    hintTxt.x = 260-hintTxt.width/2
    hintTxt.y = 140
    hintTxt.textColor = "#2a5d95"
    hintTxt.font = "Bradley Hand"
    settingLayer.addChild(hintTxt)

    global profileTarget, profileIndex, p1Arrow, choosing, p1
    choosing = True
    # p1 choose the profile
    p1 = Sprite()
    settingLayer.addChild(p1)
    profileIndex = [0, 1, 2]
    profileTarget = 0
    p1Arrow = Bitmap(BitmapData(dataList["p1Arrow"]))
    p1Arrow.height = p1Arrow.height/p1Arrow.width * 75
    p1Arrow.width = 75
    p1Arrow.x = 95+(profileTarget%len(profileIndex))*165-p1Arrow.width/2
    p1Arrow.y = 340
    p1.addChild(p1Arrow)
    
    stage.addEventListener(KeyboardEvent.KEY_DOWN, keyDown)
    # p1.addEventListener(LoopEvent.ENTER_FRAME, loop)
    # p1.addEventListener(KeyboardEvent.KEY_UP, keyUp)
    
    # p1.removeAllEventListeners()
    del profileIndex[profileTarget%len(profileIndex)]

    # add p2
    # p2 = Sprite()
    # settingLayer.addChild(p2)
    # profileTarget = profileIndex[profileIndex[0]]
    # p2Arrow = Bitmap(BitmapData(dataList["p2Arrow"]))
    # p2Arrow.height = p1Arrow.height/p1Arrow.width * 75
    # p2Arrow.width = 75
    # p2Arrow.x = 95+(profileTarget%len(profileIndex))*165-p2Arrow.width/2
    # p2Arrow.y = 340
    # p2.addChild(p2Arrow)

def keyDown(e):
    if e.keyCode == KeyCode.KEY_RIGHT:
        profileTarget += 1
        print("right")
        p1Arrow.x = 95+(profileTarget%len(profileIndex))*165-p1Arrow.width/2
    elif e.keyCode == KeyCode.KEY_LEFT:
        profileTarget -= 1
        print("left")
        p1Arrow.x = 95+(profileTarget%len(profileIndex))*165-p1Arrow.width/2
    elif e.keyCode == KeyCode.KEY_SPACE:
        choosing = False
        print("quit")
        p1.addEventListener(LoopEvent.EXIT_FRAME, test)
    else:
        print("bad condition")


def loop(e):
    p1Arrow.x = 95+(profileTarget%len(profileIndex))*165-p1Arrow.width/2
    if choosing == False:
        p1.addEventListener(LoopEvent.EXIT_FRAME, test)
    print("loop")

def test(e):
    pass