from cover import initCoverPage

from pylash.core import stage, init, addChild, KeyCode
from pylash.loaders import LoadManage
from pylash.display import Sprite, BitmapData, Bitmap, FPS, TextField, TextFormatWeight
from pylash.events import MouseEvent, LoopEvent, KeyboardEvent
from pylash.media import Sound, MediaEvent
from pylash.ui import LoadingSample1, Button

def main():

    # save the file paths which need to be loaded
    loadList = [
        {"name": "coverBg", "path" : "./src/images/coverBg.png"},
        {"name": "normalBtn", "path" : "./src/images/normalBtn.png"},
        {"name": "actionBtn", "path" : "./src/images/actionBtn.png"},
        {"name": "settingBg", "path" : "./src/images/settingBg.png"},
        {"name": "profile0", "path" : "./src/images/profile0.png"},
        {"name": "profile1", "path" : "./src/images/profile1.png"},
        {"name": "profile2", "path" : "./src/images/profile2.png"},
        {"name": "bgmOn", "path" : "./src/images/bgmOn.png"},
        {"name": "effectsOn", "path" : "./src/images/effectsOn.png"},
        {"name": "off", "path" : "./src/images/off.png"},
        {"name": "p1Arrow", "path" : "./src/images/p1Arrow.png"},
        {"name": "p2Arrow", "path" : "./src/images/p2Arrow.png"},
        {"name": "normalGoBtn", "path" : "./src/images/normalGoBtn.png"},
        {"name": "actionGoBtn", "path" : "./src/images/actionGoBtn.png"},
    ]

    loadingLayer = LoadingSample1()
    addChild(loadingLayer)

    def next(result):
        loadingLayer.remove()
        initCoverPage(result)

    
    LoadManage.load(loadList, loadingLayer.setProgress, next)

init(30, "Greedy Snack", 520, 640, main)
