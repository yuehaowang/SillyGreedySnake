from setting import initSettingPage

from pylash.core import stage, init, addChild, KeyCode
from pylash.loaders import LoadManage
from pylash.display import Sprite, BitmapData, Bitmap, FPS, TextField, TextFormatWeight
from pylash.events import MouseEvent, LoopEvent, KeyboardEvent
from pylash.media import Sound, MediaEvent
from pylash.ui import LoadingSample1, Button

def initCoverPage(result):
    # receive the loaded data
    dataList = result

    # add the cover layer
    coverLayer = Sprite()
    addChild(coverLayer)

    # set the bg image
    coverBg = Bitmap(BitmapData(dataList["coverBg"], 0, 0, 520, 640))
    coverLayer.addChild(coverBg)

    # define the state of buttons
    normal = Bitmap(BitmapData(dataList["normalStartBtn"]))
    over = Bitmap(BitmapData(dataList["actionStartBtn"]))
    down = Bitmap(BitmapData(dataList["actionStartBtn"]))

    startBtn = Button(normal, over, down, None)
    startBtn.x = 135
    startBtn.y = 385
    coverLayer.addChild(startBtn)

    def next(e):
        # remove the contents of cover layer
        coverLayer.remove()

        # init cover layer
        initSettingPage(dataList)

    startBtn.addEventListener(MouseEvent.MOUSE_UP, next)
