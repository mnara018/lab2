from Buzzer import *
from Button import *
from Displays import *

class CounterGadget: 
    """
    This class can count up and reset and display a count on LCD
    """

    def __init__(self):
        self._number =0
        self._display =LCDDisplay(sda = 0, scl =1, i2cid=0)
        self._buzzer =PassiveBuzzer(15)
        self._buttonup =Button(17, "up" , buttonhandler=self)
        self._buttonup =Button (16, "reset" , buttonhandler=self)
        self.display()

    def increment(self):
        """ add one to the number attribute"""
        self._number = self._number +1

    def reset(self):
        """ reset the number attribute"""
        self._number=0
        self._buzzer.beep()
    
    def display (self):
        """ show the number on the display """
        self._display.showNumber (self._number)
    
    def run (self):
        """Keep this up running"""

        while True:
            time.sleep(0.5)
    
    def buttonPressed (self,name):
        if name == "up": 
            self.increment()
        elif name == "reset":
            self.reset()
        self.display()
    
    
    def buttonReleased (self,name):
        """ handle the button releases"""
        pass
