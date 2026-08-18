from standalone import dogClicker
import time as tm
import random as rn
from inputimeout import inputimeout, TimeoutOccurred
from BinauralGen import BinauralSine
import Phraser as ph
import copy

clicker = dogClicker('dog-clicker.mp3')

print("THIS IS A DOG CLICKER TRAINER TO GET HORNY AT THE SOUND OF A CLICK\n")
print("IT'S MEANT TO PLAY WHILE YOU WATCH SOMETHING ELSE\n")
w = input("Are we ready?\n")

while True:
    clicks = input("How many times would you like the clicker to play? [int][default=1]: ")

    if clicks == "":
        break

    if clicks.isnumeric():
        clicks = int(clicks)
    else:
        print(f"\n\"{clicks}\" contains invalid characters.")
        continue

    if clicks < 1 or not isinstance(clicks, int):
        print(f"\n\"{clicks}\" is not a valid amount of time.")
        continue
    else:
        clicker.setTimes(clicks)
        break

print()

if w != "":
    print("At the sound of the clicks, you must divert your attention entirely to how your body feels\n")
    tm.sleep(2)
    print("It sounds like this\n")
    tm.sleep(1)
    print("->")
    clicker.play()
    print("When you hear it, clench and focus on how horny you are")
    tm.sleep(2)
    print("\tAt how good your sex tingles")
    tm.sleep(2)
    print("\t\tAt how deep you can go\n")
    tm.sleep(5)

ifSine = input("Do you want to have a binaural beat playing? [y/n][default=y]: ")
sineCheck = False

if ifSine.lower() != "n":
    binaural = BinauralSine()
    sineCheck = True

ifRoll = input("\nDo you want to roll a dice? Theres a 3/10 chance to get denied at the end [y/n][default=n]: ")
badRollCheck = False

if ifRoll.lower() == "y":
    print("\nRolling dice...")
    if rn.randint(1, 10) <= 3: badRollCheck = True
    tm.sleep(2)
    print("Results obtained.")

print("\nREMEMBER: This is meant to sound on the background, while you fill your head with PORN")
tm.sleep(2)

while True:
    x = input("\nHow long will the session be? (minutes[int]): ")

    if x.isnumeric():
        x = int(x)
    else:
        print(f"\n\"{x}\" contains invalid characters.")
        continue

    if x < 1:
        print(f"\n\"{x}\" is not a valid amount of time.")
        continue

    break

OGMOD = (0.75)/((4*x)**2)
begiTime = tm.time()
modifier = copy.deepcopy(OGMOD)
starter = 0.25

print("\n\tREMEMBER: This script is meant to be left playing in the background, while you watch your \"content\"")
tm.sleep(2)
print("\nThe closer the \"chance\" number gets to 1, the closer the session is to finishing")
tm.sleep(3)
print("\tAnd to reaching the grand finale")
tm.sleep(4)

print("\nRemember to press Enter to finish......")

if sineCheck:
    binaural.playSine()

reminder = [
    ".",
    "REMEMBER: Keep watching your porn while listening to this program in the background",
    "THIS IS A DOG CLICKER TRAINER and it's ONLY AUDIO. Keep this on the background"
]

while True:
    randomChanger = rn.uniform(0.5, 1.5)

    if (rn.random() <= starter):
        clicker.play()
        print(ph.PhrasePicker(starter))
        print(f"Chance is now at {round(starter + modifier * randomChanger, 3)}")

    try:
        c = inputimeout(prompt=rn.choices(reminder, weights=[14, 1, 1], k=1)[0], timeout=15)
        break
    except TimeoutOccurred:
        modifier += 2*OGMOD
        starter += modifier * randomChanger
        if sineCheck:
            binaural.randomChange()
    
    if starter >= 1:
        print("\nGet ready to finish with a bang.......")
        for t in range(10):
            tm.sleep(3)
            print(10-t)
        break

if badRollCheck:
    word = "DENIED"
    clicker.change("")
    if sineCheck:
        binaural.stopSine()
        sineCheck = False
else:
    word = "CUM"

while True:
    try:
        c = inputimeout(prompt=word, timeout=0.5)
        if sineCheck:
            binaural.stopSine()
        break
    except TimeoutOccurred:
        clicker.play()

lasted = round(tm.time() - begiTime)
secs = lasted % 60
mins = (lasted // 60) % 60
hors = lasted // 3600

print(f"Time lasted: {lasted} seconds")
print(f"That's {hors} hours, {mins} minutes and {secs} seconds\n")
print(f"\t{hors:02d}:{mins:02d}:{secs:02d}")
tm.sleep(1)
print("\nProgram will close in 10 seconds.....")
tm.sleep(10)
