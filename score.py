from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-250,260)
        self.ht()
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=("Courier", 15, 'normal'))

    def up(self):
        self.level += 1
        self.show_level()


