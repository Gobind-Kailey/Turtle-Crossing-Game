# Importing all files
from turtle import Screen
from player_crossing import Player
from car_manager import CarManager
from scoreboard_crossing import Scoreboard
import time

# Setting up the screen
screen = Screen()
screen.setup(600, 600)
screen.title("Snake Game- Gobind Kailey")

# So we can update the screen later.
screen.tracer(0)
# Creating classes
player = Player()
car = CarManager()
score_board = Scoreboard()

# Application can listen to our clicks
screen.listen()
screen.onkey(player.move_forward, 'Up')


# in the while loop

game_continue = True
while game_continue:
    time.sleep(0.1)
    screen.update()
    # This will keep creating a new car.
    car.create_car()

    # This is when it has reached the end and is taken to the next level.
    if player.ycor() > 280:
        player.reset()
        car.speed_increase()
        score_board.update_score()

    # This checks if the turtle is in reach of the car, and if it is: (GAME OVER)
    for car_distance in car.diff_cars:
        if player.distance(car_distance) < 20:
            score_board.game_over()
            game_continue = False
    # The cars will keep moving forward until we have made a hit.
    if game_continue:
        car.move_forward()

# This is so the screen exits when we click on the screen, not on its own. 
screen.exitonclick()