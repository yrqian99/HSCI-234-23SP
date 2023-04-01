import js
p5 = js.window

lefthand = p5.loadImage('images/lefthand.png')
contact_lens_right = p5.loadImage('images/contact_lens_right.png')
contact_lens_wrong = p5.loadImage('images/contact_lens_wrong.png')

class LeftHand:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.img = lefthand

    def draw(self):
        self.x = p5.mouseX - 260

        if p5.mouseIsPressed:
            self.y -= 0.1  
            if self.y < -130:
                self.y = -130
        else:
            self.y = p5.mouseY - 130

        if self.x > 0:
            self.x = 0
        else:
            self.x = p5.mouseX - 260
        p5.image(self.img, self.x, self.y, 280, 280)


    def show_self_pos(self):
        p5.text('left hand position is: '+ str(self.x) + ", " + str(self.y), 10, 45)


class ContactLensRight(LeftHand):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.img_right = contact_lens_right
        self.img_wrong = contact_lens_wrong
        self.img = self.img_wrong
        self.visible = True
        self.wearing_right_lens = False

    def switch_image(self):
        if self.img == self.img_wrong:
            self.img = self.img_right
            self.wearing_right_lens = True
        elif self.img == self.img_right:
            self.img = self.img_wrong
            self.wearing_right_lens = False