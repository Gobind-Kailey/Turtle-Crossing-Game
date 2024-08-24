from turtle import Turtle

# Constants
FONT = ('Courier', 20, 'normal')
ALIGNMENT = "left"

# Using inheritance
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-280, 260)
        self.writing()

    # This will write the scoreboard
    def writing(self):
        self.write(arg= f"Level: {self.level}  ", align= ALIGNMENT, font= FONT)

    # This will update the scoreboard
    def update_score(self):
        self.level += 1
        self.clear()
        self.writing()

    # Game over message will pop up once your turtle runs into a car.
    def game_over(self):
        self.goto(-90,0)
        self.write(arg=" GAME OVER!  ", align=ALIGNMENT, font=FONT)

