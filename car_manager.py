from turtle import Turtle
import random

COLORS = ['red', 'orange','green', 'blue', 'purple']

# Using inheritance
class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.diff_cars = []
        self.create_car()
        self.starting_move_distance = 5
        self.increment = 5


    def create_car(self):
        # This is so we do not create too many cars at ones
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-240, 280)
            new_car.goto(300, random_y)
            self.diff_cars.append(new_car)

    def move_forward(self):
        for cars in self.diff_cars:
            cars.setheading(180)
            cars.forward(self.starting_move_distance)


    def speed_increase(self):
        # Notice that this value below gets stored, meaning it will update and store the overall new value
        self.starting_move_distance += self.increment





