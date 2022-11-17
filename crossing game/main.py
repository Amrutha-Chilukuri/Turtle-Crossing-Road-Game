from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
timmy = Player()
screen.listen()
screen.onkeypress(timmy.move_up, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    for i in range(20):
        time.sleep(0.1)
        screen.update()
        car_manager.create_car()
        car_manager.move_cars()
        for car in car_manager.all_cars:
            if car.distance(timmy) < 20:
                game_is_on = False
                scoreboard.game_over()
        if timmy.is_at_finish_line():
            scoreboard.level_up()
            timmy.reset_position()
            car_manager.level_up()


screen.exitonclick()