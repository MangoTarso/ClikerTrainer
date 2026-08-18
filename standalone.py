from playsound import playsound
import time as tm

class dogClicker:

    def __init__(self, path):
        self.sound = path
        self._times = 1

    def setTimes(self, number):
        self._times = number
    
    def play(self):
        if self.sound != "":
            for i in range(self._times):
                playsound(self.sound, False)
                tm.sleep(0.175)

    def change(self, new_sound):
        self.sound = new_sound
    
if __name__ == "__main__":
    click = dogClicker("")
    times = input("Set times: ")
    click.setTimes(int(times))

    while True:
        click.play()
        tm.sleep(0.5)