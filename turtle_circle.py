from turtle import Turtle, Screen
import random

color = ["IndianRed", "DeepSkyBlue", "DarkOrchid", "DarkGoldenRod", "blue", "green", "yellow", "purple" , "orange", "pink"]
timmy = Turtle()

timmy.shape("arrow")
timmy.speed("fastest")
steps = 5
timmy.pensize(2)

for _ in range(int(360/steps)):
    timmy.color(random.choice(color))
    timmy.circle(100)
    timmy.setheading(timmy.heading() + steps)

screen = Screen()
screen.exitonclick()
