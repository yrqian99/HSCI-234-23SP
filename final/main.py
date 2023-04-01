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
eye5 = p5.loadImage('images/eyeopen5.png')

instruction1 = p5.loadImage('images/instruction1.png')
instruction2 = p5.loadImage('images/instruction2.png')

font = p5.loadFont('font/pixel_font.ttf')

game_state = 'intro' #intro, in_game
in_game_state = 'prepare' # prepare, approaching, ready, finish
contact_lens_state = 'right' # right, wrong


lefthand = LeftHand()
righthand = RightHand()
pupil = Pupil()
contact_lens_right = ContactLensRight()
valid_area = False

next_wink = 0
wink_interval = p5.random(1000, 3000)




class Instructions():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.img = instruction1
    
    def draw(self, x, y):
        p5.image(self.img, x, y)

    def update(self):
        if self.img == instruction1:
            if p5.mouseIsPressed and 135 < p5.mouseX < 190 and 270 < p5.mouseY < 300:
                self.img = instruction2
        elif self.img == instruction2:
            if p5.mouseIsPressed and 140 < p5.mouseX < 190 and 177 < p5.mouseY < 200:
                self.img = instruction1
            if p5.mouseIsPressed and 140 < p5.mouseX < 300 and 226 < p5.mouseY < 263:
                global game_state
                game_state = 'in_game'
                # print('game_state is: ' + game_state)
        


class Eye():
    def __init__(self, x=0, y=0):
        self.img = eye1

    def switch_image(self):
        if p5.millis() % 1000 < 333:
            p5.image(self.img, 0, 0)
        elif p5.millis() % 1000 < 666:
            self.img = eye2
            p5.image(self.img, 0, 0)
        else:
            self.img = eye3
            p5.image(self.img, 0, 0)

    def react_to_right_hand(self):
        if righthand.visible == True and p5.millis() - righthand.space_press_time > 1500:
            self.img = eye1
            p5.image(self.img, 0, 0)
        elif righthand.visible == True and 1000 < p5.millis() - righthand.space_press_time < 1500:
            self.img = eye5
            p5.image(self.img, 0, 0)
        elif righthand.visible == True and 0 < p5.millis() - righthand.space_press_time < 1000:
            self.img = eye4
            p5.image(self.img, 0, 0)


prepare_dialogue = PrepareDialogue()
approaching_dialogue = ApproachingDialogue()
ready_dialogue = ReadyDialogue()
ready_dialogue2 = ReadyDialogue2()
finish_dialogue = FinishDialogue()
wrong_area_dialogue = WrongAreaDialogue()
wrong_lens_dialogue = WrongLensDialogue()
wrong_condition_dialogue = WrongConditionDialogue()
eye = Eye()
instruction = Instructions()



def setup():
    p5.createCanvas(300, 300)
    p5.imageMode(p5.CORNER)

def draw():
    global next_wink, wink_interval, valid_area, in_game_state, game_state
    p5.background(255, 194,72)
    p5.textSize(15)
    p5.textFont(font)
    for i in range (0, 20):
        p5.text('READ!READ!READ!READ!READ!', 0, i*20)

    if game_state == 'intro':
        
        instruction.draw(0, 0)
        instruction.update()

    if game_state == 'in_game':
        p5.background(255)

    #pupil follows mouse
        pupil.draw()

    #update pupil when mousepressed
        if valid_area == True:
            # in_game_state = 'approaching'
            if contact_lens_right.wearing_right_lens == True:
                if righthand.visible == True:
                    if eye.img == eye4:
                        if pupil.update_pupil():
                            contact_lens_right.visible = False

    # #right hand disappears after 2 seconds
        eye.react_to_right_hand()
    #     if righthand.visible == True and p5.millis() - righthand.space_press_time > 2000:
    #         p5.image(eye1, 0, 0)

    #     if righthand.visible == True and p5.millis() - righthand.space_press_time < 2000:
    #         p5.image(eye4, 0, 0)

    #eye wink and speed up when finger touches eye
        if righthand.visible == False:
            if p5.millis() > next_wink:
                eye.switch_image()
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

        # transition to 'ready' state when right hand is visible
        if righthand.visible and in_game_state == 'approaching' or 'prepare':
            in_game_state = 'ready'
            if eye.img == eye4 and contact_lens_right.wearing_right_lens == True and valid_area == True:
                in_game_state = 'now'


            # transition back to 'prepare' or 'approaching' state when right hand is not visible
        if not righthand.visible and in_game_state == 'ready':
            in_game_state = 'approaching' if valid_area else 'prepare'

        # transition to 'finish' state when blue pupil is visible
        if pupil.blue_visible and in_game_state != 'finish':

            in_game_state = 'finish'


        #show dialogue
        if in_game_state == 'prepare':
            prepare_dialogue.update()
            prepare_dialogue.draw(0, 0)
            # print(prepare_dialogue.current_dialog)
        elif in_game_state == 'approaching':
            approaching_dialogue.update()
            approaching_dialogue.draw(0, 0)
            # print(approaching_dialogue.current_dialog)
        elif in_game_state == 'ready':
            ready_dialogue.update()
            ready_dialogue.draw(0, 0)
        elif in_game_state == 'now':
            ready_dialogue2.update()
            ready_dialogue2.draw(0, 0)
        elif in_game_state == 'finish':
            finish_dialogue.update()
            finish_dialogue.draw(0, 0)

        
        # wrong conditions dialogue

        if p5.mouseIsPressed:
            if righthand.visible == False or eye.img != eye4:
                wrong_condition_dialogue.update()
                wrong_condition_dialogue.draw(0,0)    
            if valid_area == False:
                wrong_area_dialogue.update()
                wrong_area_dialogue.draw(0,0)
            if contact_lens_right.wearing_right_lens == False:
                wrong_lens_dialogue.update()
                wrong_lens_dialogue.draw(0,0)
        
        if p5.keyIsPressed:
            if p5.keyCode == 71:
                game_state = 'intro' 




# #showing mouse position on screen
#     p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 30)
    
# # showing millis() on screen
#     p5.text(str(p5.millis()), 10, 15)


#switch between images eye1, eye2, eye3 every 333 milliseconds
# def switchImage():
#     global eye1, eye2, eye3, eye4

#     if p5.millis() % 1000 < 333:
#         p5.image(eye1, 0, 0)
#     elif p5.millis() % 1000 < 666:
#         p5.image(eye2, 0, 0)
#     else:
#         p5.image(eye3, 0, 0)


def keyPressed(event):
    global contact_lens_state

    if p5.keyCode == 32:
        righthand.visible = True
        righthand.space_press_time = p5.millis()

    if p5.keyCode == 83:
        # print('key "S" Pressed')
        contact_lens_right.switch_image()


def keyReleased(event):
    if p5.keyCode == 32:
        righthand.visible = False


def mousePressed(event):
    # if pupil.blue_visible == False:
    #     pupil.switch_pupil()
    #     pupil.blue_visible = True
    # print('mousePressed')
    pupil.start_mouse_press_timer()
    # print('mouse has been pressed for', pupil.mouse_press_time, 'milliseconds')


def mouseReleased(event):
    pupil.mouse_press_time = None