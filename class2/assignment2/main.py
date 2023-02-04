import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.fill(255,10,120)
    p5.background(255)           # white background
    p5.strokeWeight(4)
    p5.stroke(230,250,0)
    p5.strokeWeight(12)
    x = 100
    y = 220
    d = 10
    for n in range(3): p5.ellipse(100+n*30,y,d,d) 
    for n in range(0, 80, 20):p5.ellipse(80+n,y+40,d,d) 
    #start from 0 go to 80 by step 40
    p5.line(10,10,200,200)       # p5.line(x1,y1,x2,y2)
    p5.strokeWeight(8)
    #p5.noStoke() #no stoke
    p5.triangle(90,15,70,180,190,150) #p5.triangle(x1,y1,x2,y2,x3,y3)
    p5.strokeWeight(2)
    p5.fill(20,200,20) #fill with gray
    #p5.stroke(0) #no stroke
    p5.quad(30,210,50,200,40,240,20,250) #p5.quad(x1,y1,x2,y2,x3,y3)
    p5.strokeWeight(1)
    p5.rect(200,50,50,50) #rect(x,y,width,height)
    p5.noFill()
    p5.strokeWeight(12)
    p5.ellipse(210,210,30,30) #p5.ellipse(x,y,width,height)
    p5.strokeWeight(8)
    p5.fill(220,20,100) #fill with gray
    p5.strokeCap(p5.ROUND)
    p5.stroke(10,250,55)
    p5.arc(250, 250, 50, 50, 0, p5.QUARTER_PI) #p5.arc(x, y, width, height, start, stop) radius vs degrees
    p5.arc(150, 150, 60, 60, p5.radians(90), p5.radians(200)) #convert degree to radians
    p5.strokeCap(p5.SQUARE)
    p5.line(200, 120, 280, 180)
    p5.fill(220,10,120,90)
    p5.strokeWeight(12)
    p5.noStroke()
    p5.ellipse(220,220,50,50)
    p5.fill(20,10,220,90)
    p5.rectMode(p5.CENTER)
    p5.rect(210,260,60,60)



