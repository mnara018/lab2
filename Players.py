import time
from Displays import *


class Players:
    
    def __init__(self):
        self._player = name
        self._points = 0
        self._display = LCDDisplay(sda = 0, scl=1, i2cid=0)
        self._round = 1
    
    def increment(self):
        self._points= self._points +1

    def reset(self):
        self._points=0

    def showturn(self):
        self._display.showText(self._player "is your turn")

    def showscore(self,self._numplayers ):
        self._display.showNumber(self._points)
   
    def nextround (self):
        self._round +=1
    
    def gameover (self):
        self._display.reset()
        self._display.showText("Game Over")
        self._player.reset()


    


