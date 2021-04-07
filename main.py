from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Defining Paddle Coordinates:
LEFT_PADDLE_COR = (-350, 0)
RIGHT_PADDLE_COR = (350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
pad_r = Paddle(RIGHT_PADDLE_COR)
pad_l = Paddle(LEFT_PADDLE_COR)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(pad_r.move_up, "Up")
screen.onkey(pad_r.move_down, "Down")
screen.onkey(pad_l.move_up, "w")
screen.onkey(pad_l.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce_y()

    if ball.xcor()>=350:
        ball.restart_ball()
        score.score_1+=1
        score.update_score()

    if (ball.distance(pad_r)<50 and ball.xcor()>330) or ball.distance(pad_l)<50 and ball.xcor()<-330:
        ball.bounce_x()

    if  ball.ycor()<-350:
        ball.restart_ball()
        score.score_2 += 1
        score.update_score()

    ball.move_ball()
    time.sleep(ball.move_speed)


screen.exitonclick()
