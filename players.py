from turtle import Turtle
import random

COLORS = ["purple", "green", "blue", "red", "pink"]
POS = [-210, -200, -190, -180, -170, -160]


class Players:
    def __init__(self):
        self.pay = 0


    def create_turtles(self):
        for turtle in range(0, 6):
            new_turtle = Turtle("turtle")
            new_turtle.color(random.choice(COLORS))
            new_turtle.penup()
            new_turtle.setheading(270)
            new_turtle.goto(180, POS[turtle])




