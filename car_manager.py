from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'blue', 'purple', 'black']
STARTING_MOVE_DISTANCE = 5

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_chance = random.randint(1,10)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(stretch_wid=3,stretch_len=5)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-240, 280)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def stop_cars(self):
        for car in self.all_cars:
            car.backward(0)

    def increase_speed(self):
        self.speed += 1


