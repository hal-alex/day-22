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
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

paddle = Turtle()
paddle.penup()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.goto(x=350, y=0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")

screen.listen()
screen.onkey(go_up, "Up")



screen.exitonclick()