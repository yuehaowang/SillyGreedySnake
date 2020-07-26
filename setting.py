from playing import gameStart

from pylash.core import stage, addChild, KeyCode
from pylash.display import Sprite, BitmapData, Bitmap, TextField
from pylash.events import MouseEvent, KeyboardEvent
from pylash.media import Sound
from pylash.ui import Button


bgmPlay = False
effectsPlay = False
p1Profile = 0
p2Profile = 1

def initSettingPage(data):
    global settingLayer, dataList, profileIndex, p1Arrow, BGM
    dataList = data

    # create BGM
    BGM = Sound(dataList["BGM"])
    BGM.loopCount = Sound.LOOP_FOREVER

    # add the setting layer
    settingLayer = Sprite()
    addChild(settingLayer)

    dataList = data

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
        profiles[i].y = 175
        settingLayer.addChild(profiles[i])

    # add the hintTxt
    hintTxt = TextField()
    hintTxt.text = "<- and -> for switching, and space for determining"
    hintTxt.size = 20
    hintTxt.x = 260-hintTxt.width/2
    hintTxt.y = 147.5
    hintTxt.textColor = "#2a5d95"
    hintTxt.font = "Bradley Hand"
    settingLayer.addChild(hintTxt)

    # p1 choose the profile
    p1 = Sprite()
    settingLayer.addChild(p1)
    profileIndex = [0, 1, 2]
    p1Arrow = Bitmap(BitmapData(dataList["p1Arrow"]))
    p1Arrow.height = p1Arrow.height/p1Arrow.width * 75
    p1Arrow.width = 75
    p1Arrow.x = 95 + (p1Profile%len(profileIndex))*165 - p1Arrow.width/2
    p1Arrow.y = 340
    p1.addChild(p1Arrow)
    
    stage.addEventListener(KeyboardEvent.KEY_DOWN, p1Choosing)

def p1Choosing(e):
    global p1Profile, p2Profile, p2Arrow
    if e.keyCode == KeyCode.KEY_RIGHT:
        p1Profile = (p1Profile+1)%len(profileIndex)
        p1Arrow.x = 95+p1Profile*165-p1Arrow.width/2
    elif e.keyCode == KeyCode.KEY_LEFT:
        p1Profile = (p1Profile-1)%len(profileIndex)
        p1Arrow.x = 95+(p1Profile)*165-p1Arrow.width/2
    elif e.keyCode == KeyCode.KEY_SPACE:
        # store the profile of p1 and remove it from the available list
        del profileIndex[p1Profile]

        stage.removeEventListener(KeyboardEvent.KEY_DOWN, p1Choosing)
        stage.addEventListener(KeyboardEvent.KEY_DOWN, p2Choosing)
        
        # add p2
        p2 = Sprite()
        settingLayer.addChild(p2)
        p2Profile = 0
        p2Arrow = Bitmap(BitmapData(dataList["p2Arrow"]))
        p2Arrow.height = p1Arrow.height/p1Arrow.width * 75
        p2Arrow.width = 75
        p2Arrow.x = 95 + profileIndex[0]*165 - p2Arrow.width/2
        p2Arrow.y = 340
        p2.addChild(p2Arrow)

def p2Choosing(e):
    global p2Profile, bgmOff, effectsOff
    if e.keyCode == KeyCode.KEY_RIGHT:
        p2Profile = (p2Profile+1) % len(profileIndex)
        p2Arrow.x = 95 + profileIndex[p2Profile]*165 - p1Arrow.width/2
    elif e.keyCode == KeyCode.KEY_LEFT:
        p2Profile = (p2Profile-1) % len(profileIndex)
        p2Arrow.x = 95 + profileIndex[p2Profile]*165 - p1Arrow.width/2
    elif e.keyCode == KeyCode.KEY_SPACE:
        p2Profile = profileIndex[p2Profile]
        stage.removeEventListener(KeyboardEvent.KEY_DOWN, p2Choosing)

        # add the BGM button
        bgmStyle = Sprite()
        bgmOn = Bitmap(BitmapData(dataList["bgmOn"]))
        bgmOff = Bitmap(BitmapData(dataList["off"]))
        bgmStyle.addChild(bgmOn)
        bgmStyle.addChild(bgmOff)
        bgmBtn = Button(bgmStyle, None, None, None)
        bgmBtn.x = 260-50-bgmStyle.width
        bgmBtn.y = 500
        settingLayer.addChild(bgmBtn)
        bgmBtn.addEventListener(MouseEvent.MOUSE_UP, bgmSwitch)

        # add the effects button
        effectsStyle = Sprite()
        effectsOn = Bitmap(BitmapData(dataList["effectsOn"]))
        effectsOff = Bitmap(BitmapData(dataList["off"]))
        effectsStyle.addChild(effectsOn)
        effectsStyle.addChild(effectsOff)
        effectsBtn = Button(effectsStyle, None, None, None)
        effectsBtn.x = 260+50
        effectsBtn.y = 500
        settingLayer.addChild(effectsBtn)
        effectsBtn.addEventListener(MouseEvent.MOUSE_UP, effectsSwitch)

        # add button hints
        bgmTxt = TextField()
        bgmTxt.text = "BGM"
        bgmTxt.size = 30
        bgmTxt.x = 260-50-bgmStyle.width/2-bgmTxt.width/2
        bgmTxt.y = 590
        bgmTxt.textColor = "#2a5d95"
        bgmTxt.font = "Bradley Hand"
        settingLayer.addChild(bgmTxt)

        effectsTxt = TextField()
        effectsTxt.text = "Effects"
        effectsTxt.size = 30
        effectsTxt.x = 260+50+effectsStyle.width/2-effectsTxt.width/2
        effectsTxt.y = 590
        effectsTxt.textColor = "#2a5d95"
        effectsTxt.font = "Bradley Hand"
        settingLayer.addChild(effectsTxt)

        # add Go button
        normal = Bitmap(BitmapData(dataList["normalGoBtn"]))
        over = Bitmap(BitmapData(dataList["actionGoBtn"]))
        down = Bitmap(BitmapData(dataList["actionGoBtn"]))

        startBtn = Button(normal, over, down, None)
        startBtn.x = 260-normal.width/2
        startBtn.y = 425
        settingLayer.addChild(startBtn)

        def next(e):
            # remove the contents of cover layer
            settingLayer.remove()

            # init cover layer
            gameStart(dataList, bgmPlay, effectsPlay, p1Profile, p2Profile)

        startBtn.addEventListener(MouseEvent.MOUSE_UP, next)
        
def bgmSwitch(e):
    global bgmPlay, BGM
    if (bgmPlay):
        bgmPlay = False
        bgmOff.visible = True
        BGM.stop()
    else:
        bgmPlay = True
        bgmOff.visible = False
        BGM.play()

def effectsSwitch(e):
    global effectsPlay
    if (effectsPlay):
        effectsPlay = False
        effectsOff.visible = True
    else:
        effectsPlay = True
        effectsOff.visible = False