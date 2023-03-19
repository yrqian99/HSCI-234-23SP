import js
p5 = js.window

# to use images in a program follow 3 steps: 
# 1. copy image files to the same directory as main.py 
# 2. assign images to variables with p5.loadImage function 
eye1 = p5.loadImage('images/eyeopen1.png')  # load image data to img1
eye2 = p5.loadImage('images/eyeopen2.png')  # load image data to img1
eye3 = p5.loadImage('images/eyeopen3.png')  # load image data to img1
pupil = p5.loadImage('images/pupil.png')  # load image data to img1

def setup():
    p5.createCanvas(300, 300)
    p5.imageMode(p5.CORNER)

def draw():
    p5.background(255)
    # 3. use p5.image function to draw images
    # draw img1 at coordinates (25, 25):
    p5.image(pupil, 0, 0) 

    # # draw img1 at (125, 25) and 2x width and height:
    # p5.image(eye1, 125, 25, eye1.width*2, eye1.height*2)
    # draw img2 at coordinates (25, 150):
    p5.noTint()  # disable tint
      # draw images from center
    if(p5.millis() % 1000 < 333):
        p5.image(eye1, 0, 0)  
    elif(333 < p5.millis() % 1000 < 666):
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