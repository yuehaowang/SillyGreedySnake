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
        {"name": "normalStartBtn", "path" : "./src/images/normalStartBtn.png"},
        {"name": "actionStartBtn", "path" : "./src/images/actionStartBtn.png"},
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
        {"name": "playingBg", "path" : "./src/images/playingBg.png"},
        {"name": "snake1HeadUp", "path" : "./src/images/snake1HeadUp.png"},
        {"name": "snake1HeadDown", "path" : "./src/images/snake1HeadDown.png"},
        {"name": "snake1HeadLeft", "path" : "./src/images/snake1HeadLeft.png"},
        {"name": "snake1HeadRight", "path" : "./src/images/snake1HeadRight.png"},
        {"name": "snake1Body", "path" : "./src/images/snake1Body.png"},
        {"name": "snake2HeadUp", "path" : "./src/images/snake2HeadUp.png"},
        {"name": "snake2HeadDown", "path" : "./src/images/snake2HeadDown.png"},
        {"name": "snake2HeadLeft", "path" : "./src/images/snake2HeadLeft.png"},
        {"name": "snake2HeadRight", "path" : "./src/images/snake2HeadRight.png"},
        {"name": "snake2Body", "path" : "./src/images/snake2Body.png"},
    ]

    loadingLayer = LoadingSample1()
    addChild(loadingLayer)

    def next(result):
        loadingLayer.remove()
        initCoverPage(result)

    
    LoadManage.load(loadList, loadingLayer.setProgress, next)

init(30, "Greedy Snake", 520, 640, main)
