import js
p5 = js.window

eye1 = p5.loadImage('images/eyeopen1.png')  
eye2 = p5.loadImage('images/eyeopen2.png')  
eye3 = p5.loadImage('images/eyeopen3.png')  
lefthand = p5.loadImage('images/lefthand.png')  
pupil = p5.loadImage('images/pupil.png')  
contact_lens_right = p5.loadImage('images/contact_lens_right.png')  

class Pupil:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.img = pupil

    def draw(self):
        follow_x = p5.mouseX - 215
        follow_y = p5.mouseY - 215
        self.x = follow_x / 50
        self.y = follow_y/ 50
        p5.image(self.img, self.x, self.y)

    def show_self_pos(self):
        p5.text(str(self.x) + ", " + str(self.y), 10, 45)

class LeftHand:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.img = lefthand

    def draw(self):
        self.x = p5.mouseX - 260
        self.y = p5.mouseY - 130
        if self.x > 0:
            self.x = 0
        else:
            self.x = p5.mouseX - 260
        p5.image(self.img, self.x, self.y, 280, 280)


    def show_self_pos(self):
        p5.text(str(self.x) + ", " + str(self.y), 10, 45)

class ContactLensRight(LeftHand):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.img = contact_lens_right

lefthand = LeftHand()
pupil = Pupil()
contact_lens_right = ContactLensRight()

def setup():
    p5.createCanvas(300, 300)
    p5.imageMode(p5.CORNER)

next_wink = 0
wink_interval = p5.random(1000, 3000)

def draw():
    global next_wink, wink_interval
    p5.background(255)

#pupil follows mouse
    pupil.draw()
    # pupil.show_self_pos()


#eye wink and speed up when finger touches eye
    if p5.millis() > next_wink:
        switchImage()
        next_wink = p5.millis() + wink_interval
    else:
        p5.image(eye3, 0, 0)

    lefthand.draw()
    contact_lens_right.draw()

    lefthand.show_self_pos()

    if -110 < lefthand.x < 40 and -40 < lefthand.y < 130:
        p5.text("You touched my eye!", 10, 60)
        wink_interval = 200
    else:
        wink_interval = p5.random(1000, 3000)


    #showing mouse position on screen
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 30)
    
# showing millis() on screen
    p5.text(str(p5.millis()), 10, 15)


#switch between images eye1, eye2, eye3 every 333 milliseconds
def switchImage():
    global eye1, eye2, eye3

    if p5.millis() % 1000 < 333:
        p5.image(eye1, 0, 0)
    elif p5.millis() % 1000 < 666:
        p5.image(eye2, 0, 0)
    else:
        p5.image(eye3, 0, 0)

def keyPressed(event):
    pass

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass