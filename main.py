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
from ball import Ball
import time
from score_keeping import Score_Keeping

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_keeping = Score_Keeping()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_running = True

while game_is_running:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.ball_reset()
        score_keeping.l_score_point()

    if ball.xcor() < -380:
        ball.ball_reset()
        score_keeping.r_score_point()



screen.exitonclick()