from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.seth(90)
        self.goto(0,-270)



    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(),new_y)

    def go_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x,self.ycor())

    def go_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x,self.ycor())

    def refresh(self):
        self.teleport(0,-270)