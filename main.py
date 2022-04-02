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

from turtle import Turtle, Screen
from paddle import Paddle
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_running = True

while game_is_running:
    screen.update()

screen.exitonclick()