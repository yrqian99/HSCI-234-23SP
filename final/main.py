from righthand import *
from pupil import *
from lefthandAndLens import *
from dialogue import *


import js
p5 = js.window

eye1 = p5.loadImage('images/eyeopen1.png')  
eye2 = p5.loadImage('images/eyeopen2.png')  
eye3 = p5.loadImage('images/eyeopen3.png')
eye4 = p5.loadImage('images/eyeopen4.png')


contact_lens_state = 'right'


lefthand = LeftHand()
righthand = RightHand()
pupil = Pupil()
contact_lens_right = ContactLensRight()
valid_area = False

next_wink = 0
wink_interval = p5.random(1000, 3000)

prepare_dialogue = PrepareDialogue()
approaching_dialogue = ApproachingDialogue()

in_game_state = 'prepare' # prepare, approaching, ready, finish

def setup():
    p5.createCanvas(300, 300)
    p5.imageMode(p5.CORNER)

def draw():
    global next_wink, wink_interval, valid_area, in_game_state
    p5.background(255)

#pupil follows mouse
    pupil.draw()

#update pupil when mousepressed
    if valid_area == True:
        # in_game_state = 'approaching'
        if contact_lens_right.wearing_right_lens == True:
            if righthand.visible == True:
                in_game_state = 'ready'
                if pupil.update_pupil():
                    in_game_state = 'finish'
                    contact_lens_right.visible = False

#right hand disappears after 2 seconds
    if righthand.visible == True and p5.millis() - righthand.space_press_time > 2000:
        p5.image(eye1, 0, 0)

    if righthand.visible == True and p5.millis() - righthand.space_press_time < 2000:
        p5.image(eye4, 0, 0)

#eye wink and speed up when finger touches eye
    if righthand.visible == False:
        if p5.millis() > next_wink:
            switchImage()
            next_wink = p5.millis() + wink_interval
        else:
            p5.image(eye3, 0, 0)

#show hands
    righthand.draw()
    lefthand.draw()

#show contact lens
    if contact_lens_right.visible == True:
        contact_lens_right.draw()

    # lefthand.show_self_pos()
    # pupil.show_self_pos()

#warning when finger get closer to eye
    if -110 < lefthand.x < 40 and -40 < lefthand.y < 130:
        wink_interval = 200
        valid_area = True
        if in_game_state == 'prepare':
            in_game_state = 'approaching'
    else:
        wink_interval = p5.random(1000, 3000)
        valid_area = False
        if in_game_state == 'approaching':
            in_game_state = 'prepare'

# #show dialogue
    if in_game_state == 'prepare':
        prepare_dialogue.update()
        prepare_dialogue.draw(0, 0)
        # print(prepare_dialogue.current_dialog)
    elif in_game_state == 'approaching':
        approaching_dialogue.update()
        approaching_dialogue.draw(0, 0)
        # print(approaching_dialogue.current_dialog)




# #showing mouse position on screen
#     p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 30)
    
# # showing millis() on screen
#     p5.text(str(p5.millis()), 10, 15)




#switch between images eye1, eye2, eye3 every 333 milliseconds
def switchImage():
    global eye1, eye2, eye3, eye4

    if p5.millis() % 1000 < 333:
        p5.image(eye1, 0, 0)
    elif p5.millis() % 1000 < 666:
        p5.image(eye2, 0, 0)
    else:
        p5.image(eye3, 0, 0)


def keyPressed(event):
    global contact_lens_state

    if p5.keyCode == 32:
        righthand.visible = True
        righthand.space_press_time = p5.millis()

    if p5.keyCode == 83:
        contact_lens_right.switch_image()



def keyReleased(event):
    if p5.keyCode == 32:
        righthand.visible = False

def mousePressed(event):
    # if pupil.blue_visible == False:
    #     pupil.switch_pupil()
    #     pupil.blue_visible = True
    print('mousePressed')
    pupil.start_mouse_press_timer()
    print('mouse has been pressed for', pupil.mouse_press_time, 'milliseconds')

    
    

def mouseReleased(event):
    pupil.mouse_press_time = None