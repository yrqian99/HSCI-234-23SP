import js
p5 = js.window

def setup():
    p5.createCanvas(250, 250)    

def draw():
    p5.fill(255,10,120)
    p5.background(20)
    
    #paw color
    p5.noStroke()
    p5.fill(241,145,155)
    eDistance = 68
    p5.ellipse(100, 183, 22)
    p5.ellipse(100 + eDistance, 183, 22)
    
    #face
    p5.stroke(230)
    p5.strokeWeight(5)
    p5.noFill()
    x = 100
    y = 130
    w = 35
    h = 60
    p5.arc(x, y, w, h, p5.radians(100), p5.radians(260))
    p5.arc(x+70, y, w, h, p5.radians(280), p5.radians(80))
    
    #beard
    x1 = 65
    y1 = 135
    x2 = 75
    y2 = 130
    d1 = 130
    
    for i in range(2):
        p5.line(x1, y1 + i*10, x2, y2 + i*10)
    
    for i in range(2):
        p5.noFill();
        p5.line(x2+d1, y1 + i*10, x1+d1, y2 + i*10)

    #eyes
    x3 = 105
    y3 = 125
    eyeWidth = 20
    eyeHeight = 15
    d3 = 40
    p5.line(x3, y3, x3+eyeWidth/2, y3-eyeHeight)
    p5.line(x3+eyeWidth/2, y3-eyeHeight, x3+eyeWidth, y3)
    p5.line(x3+d3, y3, x3+eyeWidth/2+d3, y3-eyeHeight)
    p5.line(x3+eyeWidth/2+d3, y3-eyeHeight, x3+eyeWidth+d3, y3)

    #ear
    x4 = 105
    y4 = 60
    w4 = 30
    h4 = 80
    p5.arc(x4, y4, w4, h4, p5.radians(110), p5.radians(260))
    p5.arc(x4+60, y4, w4, h4, p5.radians(280), p5.radians(70))
    
    x5 = 110
    y5 = 25
    x6 = 120
    y6 = 88
    p5.line(x5, y5, x6, y6)
    p5.line(x5+50, y5, x6+30, y6)
    p5.line(x6, y6, x6+30, y6)
    
    #mouth
    p5.ellipse(x3-eyeWidth/2+d3, 144, 5)

    #paw
    x7 = 90
    y7 = 190
    w8 = 25
    h8 = 40
    d8 = 20
    for i in range(2):
        p5.arc(x7+ i*68, y7, w8, h8, p5.radians(100), p5.radians(260))
        
    for i in range(2):
        p5.arc(x7+d8+i*68, y7, w8, h8, p5.radians(280), p5.radians(80))
        
    #nail
    x9 = 96
    y9 = 170
    length = 10
    d9 = 8
    
    for i in range(2):
        p5.line(x9+i*68, y9, x9+i*68, y9+length)
        
    for i in range(2):
        p5.line(x9+d9+i*68, y9, x9+d9+i*68, y9+length)

    #blush
        
    p5.noStroke()
    p5.fill(241,145,155)
    eDistance2 = 83
    p5.ellipse(88, 135, 20)
    p5.ellipse(100+eDistance2, 135, 20)

