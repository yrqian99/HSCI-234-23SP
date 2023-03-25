import js

p5 = js.window

center_x = 1024
center_y = 498

red_x = 734
red_y = 666

green_x = 1314
green_y = 666

blue_x = 1024
blue_y = 162


color_cube = p5.loadImage('images/color_cube.png')

def setup():
    p5.createCanvas(p5.windowWidth, p5.windowHeight) 
    print('finished setup') 
    
def draw():
    global center_x, center_y
    global red_x, red_y
    global green_x, green_y
    global blue_x, blue_y

    p5.background(0)
    p5.image(color_cube, p5.windowWidth/2 - color_cube.width/1.5/2, p5.windowHeight/2 - color_cube.height/1.5/2, color_cube.width/1.5, color_cube.height/1.5)
    p5.strokeWeight(1)
    p5.stroke(0)
    p5.line(red_x, red_y, center_x, center_y)
    p5.line(green_x, green_y, center_x, center_y)
    p5.line(blue_x, blue_y, center_x, center_y)
    p5.fill(255)
    p5.noStroke()
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    p5.ellipse(red_x, red_y, 10)
    p5.ellipse(green_x, green_y, 10)
    p5.ellipse(blue_x, blue_y, 10)

    d = p5.dist(red_x, red_y, center_x, center_y)

    p5.strokeWeight(1)
    p5.stroke(255)
    p5.text(str(d), red_x - 30, red_y + 30)

    p5.noFill()
    p5.ellipse(p5.mouseX, p5.mouseY, 20)
    

def keyPressed(event):
    pass 

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass