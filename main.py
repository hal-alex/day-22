# Pong game using Turtle with Python

# Steps:
# Create the screen
# Create and move a paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with the wall and bounce
# Detect collision with the paddle
# Detect when paddle misses
# Keep score

import turtle
from paddle import Paddle
screen = turtle.Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")



Paddle()



screen.exitonclick()