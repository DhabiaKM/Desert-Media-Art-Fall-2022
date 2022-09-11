
#According to Vin Diesel in the car vroom vroom vroom movies: "There is nothing  stronger than family"
#I hardnessed my internal Vin Diesel for this assignment can i drive cars now please
print("it's too dangerous to go alone, take this")

#Libraries
import neopixel
import board
import digitalio
import time

blinkingLed = neopixel.NeoPixel(board.NEOPIXEL, 1)

#LED brightness
blinkingLed.brightness = 0.3

#Number of my family members
familyMembers=8


#These variables all dictate the amount of time each person's color will blink
ubooya=(20, 20, 255)
umya= (255, 10, 0)
dhabia= (255, 100, 204)
shamma= (153, 0, 255)
mansoor= (255, 102, 0)
saeed= (0, 204, 0)
salama= (204, 0, 102)
mohammed= (255, 255, 0)

#list to hold all the colors :>
everyone= [ubooya,umya,dhabia,shamma,mansoor,saeed,salama,mohammed]

#These variables all dictate the amount of time each person's color will blink
ubooyaN=3
umyaN= 23
dhabiaN= 3
shammaN= 6
mansoorN= 1
saeedN= 3
salamaN= 2
mohammedN= 7

#function to blink everyone's colors together at the start (attendace sorta kinda)
def everyoneHere():
    who=0
    for x in range(familyMembers):
        blinkingLed[0] = everyone[who]
        time.sleep(0.25)
        who=who+1

#function that blinks
def colorNumberBlink(number,color):
    for x in range(number):
        blinkingLed[0] = color
        time.sleep(0.5)
        blinkingLed[0] = (0,0,0)
        time.sleep(0.5)

#function that makes everyone's colors blink in the right order
def blinkTheClan():
    colorNumberBlink(ubooyaN,ubooya)
    colorNumberBlink(umyaN,umya)
    colorNumberBlink(dhabiaN,dhabia)
    colorNumberBlink(shammaN,shamma)
    colorNumberBlink(mansoorN,mansoor)
    colorNumberBlink(saeedN,saeed)
    colorNumberBlink(salamaN, salama)
    colorNumberBlink(mohammedN,mohammed)

#boolean for my while loop
blinkityBlink=True

#While loop
while blinkityBlink:
    everyoneHere()
    blinkTheClan()
    blinkityBlink=False
    #when it's done (signify this by just looping everyone's colors over and over again)
    #show over :> thank u for coming to my color show
    while blinkityBlink==False:
        everyoneHere()







