from Button import *
from Displays import *
import random

class loop: 
        def __init__(self):
            self._rbutton = Button(16, "red", buttonhandler=None)
            self._ybutton = Button(17, "yellow", buttonhandler=None)
            self._bbutton = Button(18, "blue", buttonhandler=None)
            self._gbutton = Button(19, "green", buttonhandler=None)
        
            self._rlight = Light(6,"RedLight")
            self._ylight = Light(7,"YellowLight")
            self._blight = Light(8,"BlueLight")
            self._glight = Light(9,"GreenLight")
            self._buzzer = PassiveBuzzer(14) 
            
            self._rdm = 0
            self._display = LCDDisplay(sda = 0, scl=1, i2cid=0)
            self._lightsq=[]


        
        def showpattern (self):
            self._rdm = random.randint(6,9)
            for i in range(4):
                Light(self._rdm).on()
                time.sleep(0.5)
                Light(self._rdm).off()
                self._lightsq.append(self._rdm)



            






    