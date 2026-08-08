import random as rd
from time import sleep
import pysinewave as psw
import math

class BinauralSine:
    def __init__(self):
        self.freq1 = rd.randint(64, 128)
        self.freq2 = self.freq1 + rd.randint(4, 8)
        self.leftSine = self.createSine("l")
        self.rightSine = self.createSine("r")
        self.initFreq = True
        self.initVol = True
    
    def calculatePitch(self, freq):
        return round((12*math.log(freq/440))/(math.log(2))) + 9

    def createSine(self, side):
        pitch1 = self.calculatePitch(self.freq1)
        pitch2 = self.calculatePitch(self.freq2)
        if side == "l":
            sine = psw.SineWave(pitch=pitch1, decibels=0, channel_side="l", pitch_per_second=1)
            sine.set_frequency(self.freq1)
        elif side == "r":
            sine = psw.SineWave(pitch=pitch2, decibels=0, channel_side="r", pitch_per_second=1)
            sine.set_frequency(self.freq2)
        
        return sine

    def playSine(self):
        self.leftSine.play()
        self.rightSine.play()
        self.leftSine.set_volume(0.1)
        self.rightSine.set_volume(0.1)

    def bigChange(self):
        self.freq1 = rd.randint(64, 128)
        self.freq2 = self.freq1 + rd.randint(4, 8)

    
    def changeFreq(self):
        if self.initFreq:
            self.leftSine.set_frequency(self.freq2)
            self.rightSine.set_frequency(self.freq1)
            self.initFreq = False
        else:
            self.leftSine.set_frequency(self.freq1)
            self.rightSine.set_frequency(self.freq2)
            self.initFreq = True
    
    def changeVol(self):
        if self.initVol:
            self.leftSine.set_volume(0.2)
            self.rightSine.set_volume(0.2)
            self.initVol = False
        else:
            self.leftSine.set_volume(0.1)
            self.rightSine.set_volume(0.1)
            self.initVol = False
    
    def randomChange(self):
        if rd.random() < 0.5:
            self.bigChange()
        sleep(rd.random())
        if rd.random() < 0.5:
            self.changeFreq()
        sleep(rd.random())
        if rd.random() < 0.5:
            self.changeVol()
    
    def stopSine(self):
        self.leftSine.set_volume(0)
        self.rightSine.set_volume(0)
        sleep(5)
        self.leftSine.stop()
        self.rightSine.stop()

if __name__ == "__main__":
    bn = BinauralSine()
    bn.playSine()
    sleep(5)