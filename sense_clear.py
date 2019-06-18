#!/usr/bin/env python
import time
from sense_hat import SenseHat
import random
#allows us to call methods from sensehat as sense

sense = SenseHat()
#clears any LEDS to off state
copypasta = "Did you ever hear the tragedy of Darth Plagueis? The Wise I thought not Its not a story the Jedi would tell you. Its a Sith legend. Darth Plagueis was a Dark Lord of the Sith so powerful and so wise he could use the Force to influence the midichlorians to create life He had such a knowledge of the dark side that he could even keep the ones he cared about from dying The dark side of the Force is a pathway to many abilities some consider to be unnatural He became so powerful the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself" 
'''
print("clearing LEDs")
'''
sense.clear()
#prints message on pi hat
'''
sense.show_message("<o/")
'''
#use RGB values to define colors
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
gray = (155,155,155)
green = (0,255,0)
cyan = (0,255,255)
raspberry = (255,0,125)
yellow = (225,255,0)
blue = (0,0,255)

#text speed
speed = 0.005
#shows a message with the colors
#sense.show_message(copypasta, speed, text_colour = green, back_colour = white)
'''
sense.clear()
displays one letter at a time
sense.show_letter("I", red)
time.sleep(1)
sense.clear()
'''
# assign a random integer between 0 - 255 (inclusive)
'''
r = random.randint(0,255)
sense.show_letter("I",(r,r,r))
sleep(1)
sense.clear()
'''
#turning on an individual pixel
#0,0 is top left and 7,7 is bottom right
'''
sense.set_pixel(2,2,(blue))
sense.set_pixel(4,2,(blue))
sense.set_pixel(3,4,(green))
sense.set_pixel(1,5,(red))
sense.set_pixel(2,6,(red))
sense.set_pixel(3,6,(red))
sense.set_pixel(4,6,(red))
sense.set_pixel(5,5,(raspberry))
time.sleep(1)
sense.clear()
'''
#flashes pixels in random positions of random colors for 1 second for n times
'''
n = 100000
for i in range(n+1):
    sense.set_pixel(random.randint(0,7), random.randint(0,7), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    sense.set_pixel(random.randint(0,7), random.randint(0,7), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    sense.set_pixel(random.randint(0,7), random.randint(0,7), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    sense.set_pixel(random.randint(0,7), random.randint(0,7), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    sense.set_pixel(random.randint(0,7), random.randint(0,7), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    sense.set_pixel(random.randint(0,7), random.randint(0,7), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    sense.set_pixel(random.randint(0,7), random.randint(0,7), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    sense.set_pixel(random.randint(0,7), random.randint(0,7), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    sense.set_pixel(random.randint(0,7), random.randint(0,7), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    sense.set_pixel(random.randint(0,7), random.randint(0,7), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    sense.set_pixel(random.randint(0,7), random.randint(0,7), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    sense.set_pixel(random.randint(0,7), random.randint(0,7), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    time.sleep(0.1)
    sense.clear()
sense.clear()
print("done")
'''
#shows a matrix of colors
'''
r = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
b = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
w = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) 
pixels = [
    b,b,b,b,r,r,r,r,
    b,b,b,b,w,w,w,w,
    b,b,b,b,r,r,r,r,
    b,b,b,b,w,w,w,w,
    r,r,r,r,r,r,r,r,
    w,w,w,w,w,w,w,w,
    r,r,r,r,r,r,r,r,
    w,w,w,w,w,w,w,w]
sense.set_pixels(pixels)
time.sleep(1)
sense.clear()
'''
