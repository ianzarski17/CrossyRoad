import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from score import Score

TIME = 0.1
screen = Screen()
screen.setup(600,600)
screen.title('My Crossy Road')
screen.tracer(0)
Turtle().hideturtle()
player = Player()
car_manager = CarManager()
score = Score()


screen.listen()
screen.onkey(player.go_up,'Up')
screen.onkey(player.go_down,'Down')
screen.onkey(player.go_left,'Left')
screen.onkey(player.go_right,'Right')

game_on = True

while game_on:
    time.sleep(TIME)
    screen.update()
    car_manager.move_cars()
    car_manager.create_new_cars()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_on = False

    if player.ycor() > 300:
        score.up()
        player.refresh()
        car_manager.new_level()
        TIME *= 0.75
















screen.exitonclick()