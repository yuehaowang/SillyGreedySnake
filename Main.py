from cover import initCoverPage

from pylash.core import stage, init, addChild, KeyCode
from pylash.loaders import LoadManage
from pylash.display import Sprite, BitmapData, Bitmap, FPS, TextField, TextFormatWeight
from pylash.events import MouseEvent, LoopEvent, KeyboardEvent
from pylash.media import Sound, MediaEvent
from pylash.ui import LoadingSample1, Button

import os

def main():
    loadList = []
    for root, dirs, files in os.walk("./src/images/"):
        for filename in files:
            if filename.split(".")[1] == "png":
                loadList.append({"name":filename.split(".")[0], "path": root+filename})

    for root, dirs, files in os.walk("./src/"):
        for filename in files:
            if filename.split(".")[1] == "wav":
                loadList.append({"name":filename.split(".")[0], "path": root+filename})

    loadingLayer = LoadingSample1()
    addChild(loadingLayer)

    def next(result):
        loadingLayer.remove()
        initCoverPage(result)

    
    LoadManage.load(loadList, loadingLayer.setProgress, next)

init(30, "Greedy Snake", 520, 640, main)
