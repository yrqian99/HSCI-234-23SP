import js
p5 = js.window


class Player:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x  # initialize attribute x
        self.y = y  # initialize attribute y

    def set_point(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def move_point(self, distance_x, distance_y):
        self.x += distance_x
        self.y += distance_y

        # if (self.x > 20) or (self.x < 0):
        #     distance_x = -distance_x

        # if (self.y > 20) or (self.y < 0):
        #     distance_y = -distance_y

    def keymove_point(self, distance_x, distance_y):
        if(p5.keyIsPressed == True):
            if(p5.key == 'd'):
                self.x += distance_x
            elif(p5.key == 's'):
                self.y += distance_y
            elif(p5.key == 'a'):
                self.x -= distance_x
            elif(p5.key == 'w'):
                self.y -= distance_y



    def draw(self):

        p5.noStroke()
        p5.push()
        p5.translate(self.x, self.y)
        p5.scale(0.5)
        # red square
        p5.fill(250, 8, 64)
        p5.rect(150, 30, 20, 20)

        # black squares
        p5.fill(115, 26, 66)
        p5.rect(130, 50, 20, 20)
        p5.rect(20, 120, 20, 30)
        p5.rect(40, 130, 20, 40)
        p5.rect(60, 150, 20, 40)
        p5.rect(80, 170, 30, 20)

        # dark pink
        p5.fill(201, 30, 107)
        p5.rect(60, 50, 20, 20)
        p5.rect(40, 70, 20, 20)
        p5.rect(20, 90, 40, 20)
        p5.rect(20, 110, 60, 10)
        p5.rect(40, 120, 40, 10)
        p5.rect(60, 130, 90, 20)
        p5.rect(80, 150, 50, 20)

        # pipnk
        p5.fill(255, 38, 136)
        p5.rect(80, 50, 30, 20)
        p5.rect(110, 70, 20, 20)
        p5.rect(130, 90, 20, 40)
        p5.rect(80, 120, 50, 10)
        p5.rect(80, 110, 30, 10)
        p5.rect(60, 90, 40, 20)
        p5.rect(60, 70, 30, 20)

        # light pink
        p5.fill(255, 153, 199)
        p5.rect(90, 70, 20, 20)
        p5.rect(100, 90, 30, 20)
        p5.rect(110, 110, 20, 10)

        p5.pop()


player_1 = Player(100, 100)
player_2 = Player()
player_3 = Player(150, 150)

bomb_scale = 0.5
bomb_scalespeed = 0.0005

bomb_moveSpeed = 1

def setup():
    p5.createCanvas(300, 300)
    print('finished setup')


def draw():
    p5.background(255)

    global bomb_scale
    global bomb_scalespeed

    bomb_scale = bomb_scale + bomb_scalespeed
    if (bomb_scale > 0.51) or (bomb_scale < 0.49):
        bomb_scalespeed = -bomb_scalespeed

    p5.push()
    p5.translate(0,0)
    p5.scale(bomb_scale)
    player_1.move_point(1, 1)
    player_3.keymove_point(1, 1)
    player_1.draw()
    player_2.draw()
    player_3.draw()
    p5.stroke(0)
    p5.strokeWeight(1)
    p5.line(player_2.x+ 50, player_2.y+ 50 , player_3.x+ 50, player_3.y+ 50)
    d = p5.dist(player_2.x+ 50, player_2.y+ 50 , player_3.x+ 50, player_3.y+ 50)
    p5.textSize(42)
    if d < 60:
        p5.text('boom', player_2.x, player_2.y)
    p5.scale(2)
    p5.textSize(12)
    p5.text('(' + str(d) + ')', 10, 10)
    p5.pop()




def keyPressed(event):
    # print(int(player_3.x))
    pass


def keyReleased(event):
    pass


def mousePressed(event):
    player_2.set_point(new_x=p5.mouseX, new_y=p5.mouseY)
    # print(int(player_2.x))
    # d= p5.dist(player_2.x - player_3.x , player_2.y - player_3.y)
    # print(int(d))


def mouseReleased(event):
    pass
