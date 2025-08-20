from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

XP = list(range(-300, 300))
YP = list(range(-250, 250))



class CarManager:
    def __init__(self):
        self.cars = []
        self.create_cars()


    def create_cars(self):
        for _ in range(30):
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len= 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_cor = (random.choice(XP), random.choice(YP))
            new_car.goto(random_cor)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(new_x, car.ycor())

    def create_new_cars(self):
        random_chance = random.randint(0,4)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.choice(YP)
            new_car.goto(310, random_y)
            self.cars.append(new_car)

    def new_level(self):
        for car in self.cars:
            car.ht()
        self.cars = []
        self.cars.clear()
        self.create_cars()
        self.create_new_cars()
        self.move_cars()





