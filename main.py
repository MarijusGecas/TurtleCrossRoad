import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(fun=player.move_up, key="Up")

cars = [CarManager() for _ in range(10)]

scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)

    for car in cars:
        car.move(1+player.level/10)
        car.reset_car()
        if car.check_collision(player):
            game_is_on = False
            scoreboard.game_over()


    if player.ycor()>= 280:
        player.level += 1
        scoreboard.level_cleared()
        player.goto(0, -280)

    screen.update()


screen.exitonclick()