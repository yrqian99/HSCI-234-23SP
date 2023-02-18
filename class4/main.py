#press w and s to move forwad and backward

import js
p5 = js.window

angle = 0.0
angle2 = 0.0
scale = 1.0
x = 150
y = 150


circle_x = 100
circle_xspeed = 1
circle_y = 100
circle_yspeed = 1
circle_radius = 25
left_pedal_y = 150
right_pedal_y = 150
pedal_speed = 2


def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas


def label():
    p5.fill(0)
    p5.textSize(9)
    p5.text("W A L L • ", 130, 208)
    p5.fill(255)
    p5.text("E", 180, 208)


def galaxy():
    global angle
    global scale

    if(p5.keyIsPressed == True):
        if(p5.key == 'w'):
            scale = scale + 0.001

    if(p5.keyIsPressed == True):
        if(p5.key == 's'):
            scale = scale - 0.001


    p5.push()
    p5.translate(150, 150)
    p5.rotate(angle)
    p5.scale(scale)
    p5.noStroke()
    # planet1
    p5.fill(66, 107, 143)
    p5.ellipse(50, 50, 30, 30)
    # planet2
    p5.fill(244, 220, 181)
    p5.ellipse(80, 120, 50, 50)
    angle = angle + 0.02
    p5.pop()


def galaxy2():
    global angle2
    global scale

    if(p5.keyIsPressed == True):
        if(p5.key == 'w'):
            scale = scale + 0.001

    if(p5.keyIsPressed == True):
        if(p5.key == 's'):
            scale = scale - 0.001
    
    p5.push()
    p5.translate(150, 150)
    p5.scale(scale)
    p5.rotate(angle2)
    p5.noStroke()
    # planet3
    p5.fill(241, 93, 34)
    p5.ellipse(100, 80, 20, 20)
    # planet4
    p5.fill(244, 236, 240)
    p5.ellipse(30, 150, 80, 80)
    angle2 = angle2 + 0.015
    p5.pop()


def galaxy_trace():
    
    global scale

    if(p5.keyIsPressed == True):
        if(p5.key == 'w'):
            scale = scale + 0.001

    if(p5.keyIsPressed == True):
        if(p5.key == 's'):
            scale = scale - 0.001


    p5.push()
    p5.translate(150, 150)
    p5.scale(scale)
    p5.noStroke()
    # p5.stroke(240)
    # p5.strokeWeight(3)

    p5.fill(140, 208, 211)
    p5.ellipse(0, 0, 290, 290)
    p5.fill(151, 218, 221)
    p5.ellipse(0, 0, 250, 250)
    p5.fill(167, 231, 234)
    p5.ellipse(0, 0, 140, 140)
    p5.pop()


def eyes_frame_left():
    p5.push()
    p5.translate(120, 80)
    p5.rectMode(p5.CENTER)
    p5.fill(80)
    p5.noStroke()
    p5.arc(0, 0, 50, 50, 0, p5.PI)
    p5.arc(-25, 0, 100, 80, p5.TWO_PI - p5.QUARTER_PI, p5.TWO_PI, p5.PIE)
    p5.pop()


def eyes_frame_left_inner():
    p5.push()
    p5.translate(120, 80)
    p5.rectMode(p5.CENTER)
    p5.fill(230)
    p5.noStroke()
    p5.arc(0, 0, 40, 40, 0, p5.PI)
    p5.arc(-20, 0, 80, 60, p5.TWO_PI - p5.QUARTER_PI, p5.TWO_PI, p5.PIE)
    p5.pop()


def eyes_frame_right():
    p5.push()
    p5.translate(180, 80)
    p5.rectMode(p5.CENTER)
    p5.fill(80)
    p5.noStroke()
    p5.arc(0, 0, 50, 50, 0, p5.PI)
    p5.arc(25, 0, 100, 80, p5.PI, p5.PI + p5.QUARTER_PI, p5.PIE)
    p5.pop()


def eyes_frame_right_inner():
    p5.push()
    p5.translate(180, 80)
    p5.rectMode(p5.CENTER)
    p5.fill(230)
    p5.noStroke()
    p5.arc(0, 0, 40, 40, 0, p5.PI)
    p5.arc(20, 0, 80, 60, p5.PI, p5.PI + p5.QUARTER_PI, p5.PIE)
    p5.pop()


def eye(x, y, s, c):

    d = p5.map(p5.mouseX, 0, 300, -1, 1)

    p5.push()
    p5.translate(x, y)
    p5.noStroke()
    p5.fill(c)
    p5.ellipse(d, 0, s, s)
    p5.pop()


def nose():
    p5.rectMode(p5.CENTER)
    p5.push()
    p5.translate(150, 70)
    # rect1
    p5.fill(255, 150, 40)
    p5.noStroke()
    p5.rect(0, 25, 20, 50)
    # rect2
    p5.fill(50)
    p5.rect(0, 0, 20, 10)
    # rect3
    # p5.fill(255,150,40)
    # p5.rect(0,48,30,10)
    p5.pop()


def body():

    p5.rectMode(p5.CENTER)
    p5.push()
    p5.translate(150, 130)
    # bottom part
    p5.fill(255, 150, 40)
    p5.noStroke()
    p5.rect(0, 48, 110, 70)
    # upper part
    p5.fill(150)
    p5.noStroke()
    p5.rect(0, 0, 110, 30)

    if (94 < p5.mouseX < 204 and 144 < p5.mouseY < 211):
            # inner part
            p5.fill(99, 79, 68)
            p5.noStroke()
            p5.rect(0, 48, 50, 45)
    
    p5.pop()



def hand(x):

    d = p5.map(p5.mouseX, 0, 300, -2, 2)

    p5.rectMode(p5.CENTER)
    p5.push()
    p5.fill(215, 202, 184)
    p5.noStroke()
    p5.translate(x+d, 150)
    p5.rect(0, 0, 30, 30)
    p5.pop()


def arm(x, r):
    p5.push()
    p5.fill(178, 171, 154)
    p5.noStroke()
    p5.translate(x, 138)
    p5.rotate(r)
    p5.ellipse(0, 0, 20, 30)
    p5.pop()


def tire(x):

    d = p5.map(p5.mouseX, 0, 300, -3, 3)

    p5.rectMode(p5.CENTER)
    p5.push()
    p5.fill(50)
    p5.noStroke()
    p5.translate(x+d, 200)
    p5.rect(0, 0, 40, 60)
    p5.pop()


def draw():
    global angle  # use global variable angle
    global x, y  # use global variable x an y
    p5.background(129, 192, 198)

    galaxy_trace()
    galaxy()
    galaxy2()

    # p5.fill(0)
    # p5.text("p5.mouseIsPressed: " + str(p5.mouseIsPressed), 10, 20)
    # p5.text("p5.mouseButton: " + str(p5.mouseButton), 10, 30)
    # p5.text("p5.keyIsPressed: " + str(p5.keyIsPressed), 10, 40)
    # p5.text("p5.key: " + str(p5.key), 10, 50)
    # p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 10)

    nose()
    arm(90, -15)
    arm(210, 15)
    body()

    eyes_frame_left()
    eyes_frame_right()
    eyes_frame_left_inner()
    eyes_frame_right_inner()

    # left eye black
    eye(125, 80, 30, 50)
    # right eye black
    eye(175, 80, 30, 50)

    # right eye white
    eye(130, 80, 10, 220)
    # right eye white
    eye(180, 80, 10, 220)

    tire(90)
    tire(210)

    hand(100)
    hand(200)

    label()
