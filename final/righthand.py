import js
p5 = js.window

righthand = p5.loadImage('images/righthand.png')

class RightHand:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.img = righthand
        self.visible = False
        self.space_press_time = None

    def draw(self):
        if self.visible:
            p5.image(self.img, self.x, self.y)