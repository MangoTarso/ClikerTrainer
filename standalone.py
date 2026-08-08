from playsound import playsound
import time as tm

class dogClicker:

    def __init__(self, path):
        self.sound = path
    
    def play(self):
        playsound(self.sound)

    def change(self, new_sound):
        self.sound = new_sound
    
if __name__ == "__main__":
    click = dogClicker("dog-clicker.mp3")

    while True:
        click.play()
        tm.sleep(0.5)