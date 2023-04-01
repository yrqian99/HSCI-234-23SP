import js
p5 = js.window

font = p5.loadFont('font/pixel_font.ttf')

class Dialogue:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.dialog_index = 0
        self.current_dialog = self.dialogues[self.dialog_index]
        self.timer = p5.millis()

    def update(self):
        if(p5.millis() > self.timer + self.switch_interval):
            self.dialog_index += 1
            if self.dialog_index > len(self.dialogues) - 1:
                self.dialog_index = 0
            self.current_dialog = self.dialogues[self.dialog_index]
            self.timer = p5.millis()

    def draw(self, x, y):
        p5.strokeWeight(3)
        p5.rect(x, y, 300, 30)

        p5.textFont(font)
        p5.textSize(10)
        p5.text(self.current_dialog, x+10, y+20)

class PrepareDialogue(Dialogue):
    def __init__(self, x=0, y=0):
        self.dialogues = [
            'Can we not do this...',
            "Be gentle, ok?",
            "Is there another way?",
            "I'm scared..."
        ]
        self.switch_interval = 5000
        super().__init__(x, y)

class ApproachingDialogue(Dialogue):
    def __init__(self, x=0, y=0):
        self.dialogues = [
            'Dont hurt me please...',
            'Will I be blind?',
            'nonononono...',
            'Watch out...'
        ]
        self.switch_interval = 1000
        super().__init__(x, y)

class ReadyDialogue(Dialogue):
    def __init__(self, x=0, y=0):
        self.dialogues = [
            'AHHHHHHHHHHHHHHHHHHHHHH'
        ]
        self.switch_interval = 2000
        super().__init__(x, y)

class FinishDialogue(Dialogue):
    def __init__(self, x=0, y=0):
        self.dialogues = [
            'You did it! Finally!',
            'Am I looking good now?',
            'I know I could trust you!'
        ]
        self.switch_interval = 2000
        super().__init__(x, y)

class WrongAreaDialogue(Dialogue):
    def __init__(self, x=0, y=0):
        self.dialogues = [
            'Why are you so far away from me?',
            'You should come closer to me!',
        ]
        self.switch_interval = 2000
        super().__init__(x, y)

class WrongLensDialogue(Dialogue):
    def __init__(self, x=0, y=0):
        self.dialogues = [
            'Did you read the guide?',
            'Can I trust you with this?',
        ]
        self.switch_interval = 2000
        super().__init__(x, y)

class WrongConditionDialogue(Dialogue):
    def __init__(self, x=0, y=0):
        self.dialogues = [
            'I dont think Im ready yet!!',
            'Not yet, not yet, not yet!!',
        ]
        self.switch_interval = 2000
        super().__init__(x, y)

class ReadyDialogue2(Dialogue):
    def __init__(self, x=0, y=0):
        self.dialogues = [
            'NOW!!'
        ]
        self.switch_interval = 1000
        super().__init__(x, y)






