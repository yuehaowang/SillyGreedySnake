from pylash.core import stage, init, addChild, KeyCode
from pylash.loaders import LoadManage
from pylash.display import Sprite, BitmapData, Bitmap, FPS, TextField, TextFormatWeight
from pylash.events import MouseEvent, LoopEvent, KeyboardEvent
from pylash.media import Sound, MediaEvent
from pylash.ui import LoadingSample1, Button

def gameStart(data, bgmPlay, effectsPlay, p1Profile, p2Profile):
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
    playingLayer.addChild(profile1)

    profile2 = Bitmap(BitmapData(dataList["profile%s" % p2Profile]))
    profile2.x = 400
    profile2.y = 20
    playingLayer.addChild(profile2)


