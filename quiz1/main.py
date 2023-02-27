import js
p5 = js.window

#1. Create a global variable random_size that is a random integer value between 25 - 125. 
random_size = p5.random(25, 125)
random_size2 = p5.random(25, 125)
random_size3 = p5.random(25, 125)
random_size4 = p5.random(25, 125)

alpha = 0
size = 0

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 
    print('finished setup')

def draw():
    global random_size, random_size2, random_size3, random_size4
    global alpha
    global size
    
    p5.background(255)           # white background
    p5.noStroke()
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    p5.strokeWeight(2)
    p5.fill(0)
    p5.text(random_size, 10, 30)
    p5.text("p5.mouseIsPressed: " + str(p5.mouseIsPressed), 10, 45)
    p5.text("is_inside_square(p5.mouseX, p5.mouseY) = " + str(is_inside_rect(p5.mouseX, p5.mouseY)), 10, 60)

    #2. Draw a square of random size using line functions only.
    size = int(random_size)
    size2 = int(random_size2)
    size3 = int(random_size3)
    size4 = int(random_size4)
    
    # p5.push()
    # p5.translate(50, 100)
    # p5.line(0,0,0,size)
    # p5.line(0,0,size,0)
    # p5.line(0,size,size,size)
    # p5.line(size,0,size,size)
    # p5.pop()
    #random_square(size)

    #6. Draw 4 random squares, one in each corner of the canvas.
    p5.stroke(127, 0, 255)
    random_square_at(0, 0, size)

    #9. Make another square change color when the cursor is inside of it.
    p5.stroke(255, 127, 54)
    if(p5.mouseX > 175) and (p5.mouseX < 175 + size) \
    and (p5.mouseY > 0) and (p5.mouseY < size):
        p5.stroke(100, 127, 254)
    else:
        p5.stroke(255, 127, 54)
    random_square_at(175, 0, size)
    
    #8. Animate the transparency of another square.
    p5.stroke(127, 200, 0, alpha)
    alpha = alpha + 1
    if (alpha > 255):
        alpha = 0
    random_square_at(0, 175, size)

    #7. Make one of the squares visible only when the mouse is pressed.
    if(p5.mouseIsPressed):
        p5.stroke(255, 0, 127)
        random_square_at(175, 175, size)

    p5.push()
    p5.translate(0,0)
    for i in range (2):
        p5.stroke(127, 0, 255)
        random_square_at(0, 0, size*(i+1))
    p5.pop()



#3. Write a function definition random_square(size) to draw a random size square.
def random_square(size):
    p5.push()
    p5.translate(0, 0) ###4. Use transformation functions to move the square by x and y coordinates.
    p5.line(0,0,0,size)
    p5.line(0,0,size,0)
    p5.line(0,size,size,size)
    p5.line(size,0,size,size)
    p5.pop()


#5. Write another function definition random_square_at(x, y, size) to draw a square.
def random_square_at(x, y, size):
    p5.push()
    p5.translate(x, y)
    random_square(size)
    p5.pop()


#10. Write a function definition inside_square that returns True if the cursor is inside a square.
def is_inside_rect(x, y):
    
    global size

    size = int(random_size)
    
    if(x > 175) and (x < 175 + size) \
    and (y > 0) and (y < size):
        return True
    else:
        return False

