
import time
from sense_hat import SenseHat

sense = SenseHat()

# sense.clear()
r = [200, 16, 46]
b = [1, 33, 105]
w = [255, 255, 255]
g = [185, 185, 185]
O = [0,0,0]
X = [0,0,0]

flag1 = [
    r, w, b, r, r, b, w, r,
    b, r, b, r, r, b, r, b,
    w, w, w, r, r, w, w, w,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    w, w, w, r, r, w, w, w,
    b, r, b, r, r, b, r, b,
    r, w, b, r, r, b, w, r
]

flag2 = [
    r, b, w, r, r, w, b, r,
    w, r, w, r, r, w, r, w,
    b, b, w, r, r, w, b, b,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    b, b, w, r, r, w, b, b,
    w, r, w, r, r, w, r, w,
    r, b, w, r, r, w, b, r
]

thing = [
    [
        b, b, b, r, r, b, b, b,
        b, b, b, r, r, b, b, b,
        b, b, b, r, r, b, b, b,
        b, r, b, g, g, b, r, b,
        b, r, b, g, g, b, r, b,
        b, b, b, r, r, b, b, b,
        b, b, b, r, r, b, b, b,
        b, b, b, r, r, b, b, b
    ],
    [
        b, r, r, b, b, b, b, b,
        b, b, r, r, b, b, b, b,
        b, b, b, r, r, b, b, b,
        b, r, b, g, g, b, r, b,
        b, r, b, g, g, b, r, b,
        b, b, b, r, r, b, b, b,
        b, b, b, b, r, r, b, b,
        b, b, b, b, b, r, r, b
    ],
    [
        r, r, b, b, b, b, b, b,
        b, r, r, b, b, b, b, b,
        b, b, r, r, b, b, r, b,
        b, b, b, g, g, b, r, b,
        b, r, b, g, g, b, b, b,
        b, r, b, b, r, r, b, b,
        b, b, b, b, b, r, r, b,
        b, b, b, b, b, b, r, r,
    ],
    [
        b, b, b, b, b, b, b, b,
        r, r, r, b, b, r, b, b,
        r, r, r, r, b, b, r, b,
        b, b, b, g, g, b, b, b,
        b, b, b, g, g, b, b, b,
        b, r, b, b, r, r, r, r,
        b, b, r, b, b, r, r, r,
        b, b, b, b, b, b, b, b,
    ],
    [
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, r, b, b,
        r, r, r, r, b, b, r, b,
        r, r, r, g, g, b, b, b,
        b, b, b, g, g, r, r, r,
        b, r, b, b, r, r, r, r,
        b, b, r, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
    ],
    [
        b, b, b, b, b, b, b, b,
        b, b, b, b, r, r, b, b,
        r, b, b, b, b, b, b, b,
        r, r, r, g, g, r, r, b,
        b, r, r, g, g, r, r, r,
        b, b, b, b, b, b, b, r,
        b, b, r, r, b, b, b, b,
        b, b, b, b, b, b, b, b,
    ],
    [
        b, b, b, b, b, b, b, b,
        b, b, b, r, r, b, b, b,
        b, b, b, b, b, b, b, b,
        r, r, r, g, g, r, r, r,
        r, r, r, g, g, r, r, r,
        b, b, b, b, b, b, b, b,
        b, b, b, r, r, b, b, b,
        b, b, b, b, b, b, b, b,
    ],
    [
        b, b, b, b, b, b, b, b,
        b, b, b, r, r, b, b, r,
        b, b, b, b, b, b, r, r,
        b, b, r, g, g, r, r, b,
        b, r, r, g, g, r, b, b,
        r, r, b, b, b, b, b, b,
        r, b, b, r, r, b, b, b,
        b, b, b, b, b, b, b, b,
    ],
    [
        b, b, b, b, b, b, b, r,
        b, b, r, r, b, b, r, r,
        b, b, b, b, b, r, r, b,
        b, b, b, g, g, r, b, b,
        b, b, r, g, g, b, b, b,
        b, r, r, b, b, b, b, b,
        r, r, b, b, r, r, b, b,
        r, b, b, b, b, b, b, b,
    ],
    [
        b, b, b, b, b, r, r, b,
        b, b, r, b, b, r, r, b,
        b, r, b, b, b, r, r, b,
        b, b, b, g, g, r, b, b,
        b, b, r, g, g, b, b, b,
        b, r, r, b, b, b, r, b,
        b, r, r, b, b, r, b, b,
        b, r, r, b, b, b, b, b,
    ],
    [
        b, b, b, b, r, r, b, b,
        b, b, b, r, r, b, b, b,
        b, r, b, r, r, b, b, b,
        b, r, b, g, g, b, b, b,
        b, b, b, g, g, b, r, b,
        b, b, b, r, r, b, r, b,
        b, b, b, r, r, b, b, b,
        b, b, r, r, b, b, b, b,
    ],
    [
        b, b, b, r, r, b, b, b,
        b, b, b, r, r, b, b, b,
        b, b, b, r, r, b, b, b,
        b, r, b, g, g, b, r, b,
        b, r, b, g, g, b, r, b,
        b, b, b, r, r, b, b, b,
        b, b, b, r, r, b, b, b,
        b, b, b, r, r, b, b, b,
    ]
]

def turnClockwise():
    loopnum = 0
    while loopnum <= 5:
        loopthing = 0
        while loopthing <= 11:
            time.sleep(0.04)
            sense.set_pixels(thing[loopthing])
            loopthing += 1
        loopnum += 1

def turnAnticlockwise():
    loopnum = 0
    while loopnum <= 5:
        loopthing = 11
        while loopthing >= 0:
            time.sleep(0.04)
            sense.set_pixels(thing[loopthing])
            loopthing -= 1
        loopnum += 1

def flagOne():
    sense.set_pixels(flag1)

def flagTwo():
    sense.set_pixels(flag2)

def clear():
    sense.clear()

while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
        if event.direction == 'left' and event.action == 'released':
            turnClockwise()
        elif event.direction == 'right' and event.action == 'released':
            turnAnticlockwise()
        elif event.direction == 'down' and event.action == 'released':
            flagOne()
        elif event.direction == 'up' and event.action == 'released':
            flagTwo()
        elif event.direction == 'middle' and event.action == 'released':
            clear()
