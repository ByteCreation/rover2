#!/usr/bin/python
from sense_hat import SenseHat
import os
import time
import pygame  # See http://www.pygame.org/docs
from pygame.locals import *
import itertools

print("Press Escape to quit")
time.sleep(1)

pygame.init()
pygame.display.set_mode((640, 480))

sense = SenseHat()
sense.clear()  # Blank the LED matrix
sense.set_rotation(270)  # Flight orientation

# 0, 0 = Top left
# 7, 7 = Bottom right
UP_PIXELS = [[3, 0], [4, 0]]
DOWN_PIXELS = [[3, 7], [4, 7]]
LEFT_PIXELS = [[0, 3], [0, 4]]
RIGHT_PIXELS = [[7, 3], [7, 4]]
CENTRE_PIXELS = [[3, 3], [4, 3], [3, 4], [4, 4]]


def set_pixels(pixels, col):
    for p in pixels:
        sense.set_pixel(p[0], p[1], col[0], col[1], col[2])


# Joystick is turned 90 degrees clockwise for flight orientation
def handle_event(event, colour):
    if event.direction == 'down':
        set_pixels(LEFT_PIXELS, colour)
    elif event.direction == 'up':
        set_pixels(RIGHT_PIXELS, colour)
    elif event.direction == 'left':
        set_pixels(UP_PIXELS, colour)
    elif event.direction == 'right':
        set_pixels(DOWN_PIXELS, colour)
    elif event.direction == 'middle':
        set_pixels(CENTRE_PIXELS, colour)


running = True

GREEN = [0, 255, 0]
RED = [255, 0, 0]
BLUE = [0, 0, 255]
WHITE = [255, 255, 255]
toggle = itertools.cycle([GREEN, WHITE, RED, BLUE]).__next__
colour = BLUE
set_pixels(CENTRE_PIXELS, colour)
while running:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            if event.direction == 'middle':
                colour = toggle()
            handle_event(event, colour)