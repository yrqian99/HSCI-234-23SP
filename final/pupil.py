from main import *

import js
p5 = js.window

pupil = p5.loadImage('images/pupil.png')
bluepupil = p5.loadImage('images/bluepupil.png')

class Pupil:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.img = pupil
        self.blue_visible = False
        self.mouse_press_time = None

    def draw(self):
        follow_x = p5.mouseX - 215
        follow_y = p5.mouseY - 215
        self.x = follow_x/50
        self.y = follow_y/50
        p5.image(self.img, self.x, self.y)

    def start_mouse_press_timer(self):
        self.mouse_press_time = p5.millis()

    def update_pupil(self):
        if p5.mouseIsPressed and self.mouse_press_time != None:
            if p5.millis() - self.mouse_press_time > 3000:
                self.switch_pupil()
                self.mouse_press_time = None
                return True
        return False
                

    def switch_pupil(self):
        if self.img == pupil and self.blue_visible == False:
            self.img = bluepupil
            self.blue_visible = True
        else:
            self.img = pupil

    def show_self_pos(self):
        p5.text('pupil position is: '+ str(self.x) + ", " + str(self.y), 10, 60)