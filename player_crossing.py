from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# We are using inheritance to inherit from the Turtle class
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_turtle()

    # This will create the turtle at the starting position
    def create_turtle(self):
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)



