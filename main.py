from turtle import Turtle
from turtle import Screen
import random


colors = ["purple", "green", "blue", "red", "pink", "yellow"]
pos = [230, 200, 170, -230, -200, -170]
speeds = ["slow", "slowest", "normal", "fast", "fastest"]


screen = Screen()
screen.setup(400, 500)
screen.title("My Turtle Game")
choice = screen.textinput("Make a bet!", "Choose a color of your liking: ").lower()
w_turtle = ""
all_turtles = []


for c_turtle in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[c_turtle])
    new_turtle.penup()
    new_turtle.goto(-180, pos[c_turtle])
    all_turtles.append(new_turtle)

race_is_on = True

while race_is_on:
    for t in all_turtles:
        t.speed(random.choice(speeds))
        t.forward(random.randint(0, 10))

        if t.xcor() > 165:
            race_is_on = False
            w_turtle = t.pencolor()

            if choice == w_turtle:
                print("You have won! Congratulations.")
            else:
                print(f"The {w_turtle} turtle was the winner. Try again.")







screen.exitonclick()
