import js
p5 = js.window

angle = 0
x = 150
y = 150


circle_x = 100
circle_xspeed = 1
circle_y = 100
circle_yspeed = 1
circle_radius = 25
left_pedal_y = 150
right_pedal_y = 150
pedal_speed = 2



def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 
        

def draw():
    global angle # use global variable angle
    global x, y #use global variable x an y
    p5.background(255)
    p5.fill(0)
    p5.text("p5.mouseIsPressed: " + str(p5.mouseIsPressed), 10 , 20) 
    p5.text("p5.mouseButton: " + str(p5.mouseButton), 10 , 30)
    p5.text("p5.keyIsPressed: " + str(p5.keyIsPressed), 10 , 40)
    p5.text("p5.key: " + str(p5.key), 10 , 50)
    
        
    #keyboard conditions
    if(p5.keyIsPressed == True):
        if(p5.key == "g"):
            p5.fill(0,255,0)
        if(p5.keyCode == p5.UP_ARROW):
            y = y - 1
        elif(p5.keyCode == p5.DOWN_ARROW):
            y = y + 1 
        elif(p5.keyCode == p5.LEFT_ARROW):
            x = x - 1 
        elif(p5.keyCode == p5.RIGHT_ARROW):
            x = x + 1 




    #mouse conditions
    if(p5.mouseIsPressed == True):
        if(p5.mouseButton == p5.RIGHT):
            p5.fill(255,0,0)
        else:
            p5.fill(0)
    else:
        p5.fill(255)

    p5.rectMode(p5.CENTER)
    p5.push()
    p5.translate(x,y)
    #angle = angle + 1
    angle += 1
    p5.rotate(p5.radians(angle))
    p5.ellipse(0, 0, 100, 100)

    p5.pop()
    
    global circle_x, circle_xspeed
    global circle_y, circle_yspeed

    
    if(circle_x < circle_radius) or (circle_x > p5.width - circle_radius):
        circle_xspeed = -circle_xspeed
        
    if(circle_y < circle_radius) or (circle_y > p5.height - circle_radius):
        circle_yspeed = -circle_yspeed

    circle_x = circle_x + circle_xspeed
    circle_y = circle_y + circle_yspeed
    

    p5.ellipse(circle_x, circle_y, circle_radius*2, circle_radius*2,) 


    global left_pedal_y, right_pedal_y
    global pedal_speed 
    
    p5.rect(10, left_pedal_y, 20, 50) #pedel left
    p5.rect(290, right_pedal_y, 20, 50) #pedel right

    if(p5.keyIsPressed == True):
        if(p5.key == 'w'):
            if(left_pedal_y > 50/2):
                left_pedal_y = left_pedal_y - pedal_speed
        elif(p5.key == 's'):
            if(left_pedal_y < p5.height-50/2):
                left_pedal_y = left_pedal_y + pedal_speed


    if(p5.keyIsPressed == True):
        if(p5.key == 'e'):
            if(right_pedal_y > 50/2):
                right_pedal_y = right_pedal_y - pedal_speed
        if(p5.key == 'd'):
            if(right_pedal_y < p5.height-50/2):
                right_pedal_y = right_pedal_y + pedal_speed
