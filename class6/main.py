import js
p5 = js.window

program_timer = 0
program_state = 'state1'
window_state = 'window'


def setup():
    p5.createCanvas(300, 300)
    print('finished setup..')


def draw():
    global program_timer
    global program_state
    global window_state

    sun_y = 230

    p5.background(0)
    p5.fill(255)
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    p5.text('program_state = ' + program_state, 10, 25)

    program_timer = int(p5.millis()/1000)
    p5.text('seconds: ' + str(program_timer), 10, 35)

    sunrise(220, 250, 100, 25, 8, 17, 77, 0, 0, 0)

    if program_timer > 2: 
        program_state = 'state2'

    if program_state == 'state2':
        sunrise(200, 250, 0, 0, 80, 28, 120, 85, 85, 85)
 
    if program_timer > 5:
        program_state = 'state3'

    if program_state == 'state3':
        sunrise(170, 250, 0, 0, 214, 96, 139, 170, 170, 170)

    if program_timer > 8:
        program_state = 'state4'

    if program_state == 'state4':
        sunrise(140, 250, 0, 0, 252, 187, 200, 255, 255, 255)
        
    if window_state == 'window':
        window()
        
    if window_state == 'nowindow':
        nowindow()

    p5.fill(255)
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    p5.text('program_state = ' + program_state, 10, 25)

    program_timer = int(p5.millis()/1000)
    p5.text('seconds: ' + str(program_timer), 10, 35)


def sunrise(y, r1, g1, b1, r2, g2, b2, r3, g3, b3):
    p5.rectMode(p5.CORNER)
    p5.background(r3, g3, b3)
    p5.noStroke()

    # draw sun
    p5.fill(r1, g1, b1)
    p5.ellipse(150, y, 75, 75)

    # draw horizon
    p5.fill(r2, g2, b2)
    p5.rect(0, 180, 300, 150)

def window():
    p5.fill(0)
    p5.rectMode(p5.CORNER)
    p5.rect(0,0,300,50)
    p5.rect(0,0,50,300)
    p5.rect(0,250,300,50)
    p5.rect(250,0,50,300)
    p5.rectMode(p5.CENTER)
    p5.rect(150,150,30,300)
    p5.rect(150,150,300,30)

def nowindow():
    p5.fill(0)
    p5.rectMode(p5.CORNER)
    p5.rect(0,0,300,50)
    p5.rect(0,0,50,300)
    p5.rect(0,250,300,50)
    p5.rect(250,0,50,300)

def mousePressed(event):
    global window_state
    
    if window_state == 'window':
        window_state = 'nowindow'
    elif window_state == 'nowindow':
        window_state = 'window'

def keyReleased(event):
    pass

def keyPressed(event):
    pass

def mouseReleased(event):
    pass
