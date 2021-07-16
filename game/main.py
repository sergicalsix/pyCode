import turtle
import os
import time
import random


# Score
score_a = 0
score_b = 0
match_point = 3
now_score_a = False
now_score_b = False

# Speed
speed = 2
random_ratio = 0.5
speed_lv = 0

# Window
wn = turtle.Screen()
wn.title("PingPongGame")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0 ".format(score_a, score_b),
          align="center",  font=("Arial",  24, "normal"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("red")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 210)


# paddle A
# turtle is module name and Turtle is a class name . Small 't' denotes a module name and capital 'T' denotes a class name.
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(-1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = speed
ball.dy = -1 * speed


# Function
move_size = 20


def paddle_a_up():
    y = paddle_a.ycor()
    y += move_size
    paddle_a.sety(y)


def paddle_a_down():

    y = paddle_a.ycor()
    y -= move_size
    paddle_a.sety(y)


def paddle_a_2up():
    y = paddle_a.ycor()
    y += 4 * move_size
    paddle_a.sety(y)


def paddle_a_2down():

    y = paddle_a.ycor()
    y -= 4 * move_size
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += move_size
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= move_size
    paddle_b.sety(y)


def paddle_b_2up():
    y = paddle_b.ycor()
    y += 4 * move_size
    paddle_b.sety(y)


def paddle_b_2down():
    y = paddle_b.ycor()
    y -= 4 * move_size
    paddle_b.sety(y)

# Keyboard binding


wn.listen()

"""
def Player_A_key():
    wn.onkeyrelease(None, "o")
    wn.onkeyrelease(None, "l")
    wn.onkeyrelease(None, "z")
    wn.onkeyrelease(None, "x")

    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_a_2up, "q")
    wn.onkeypress(paddle_a_2down, "a")


def Player_B_key():
    wn.onkeyrelease(None, "w")
    wn.onkeyrelease(None, "s")
    wn.onkeyrelease(None, "q")
    wn.onkeyrelease(None, "a")

    wn.onkeypress(paddle_b_up, "o")
    wn.onkeypress(paddle_b_down, "l")
    wn.onkeypress(paddle_b_2up, "z")
    wn.onkeypress(paddle_b_2down, "x")
"""


wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_2up, "q")
wn.onkeypress(paddle_a_2down, "a")
wn.onkeypress(paddle_b_up, "o")
wn.onkeypress(paddle_b_down, "l")
wn.onkeypress(paddle_b_2up, "i")
wn.onkeypress(paddle_b_2down, "k")

# in main game loop
while score_a < match_point and score_b < match_point:
    wn.update()
    # ball sleep and speed reset when point is got
    if now_score_a == True:
        time.sleep(1)
        ball.dx = -1 * speed
        ball.dy = speed
        now_score_a = False
        pen2.clear()
    elif now_score_b == True:
        time.sleep(1)
        ball.dx = speed
        ball.dy = -1 * speed
        now_score_b = False
        pen2.clear()

    # KeyBoard hack
    # if (ball.xcor() + ball.dx) * ball.xcor() <= 0:
    #    if ball.xcor() > 0:
    #        Player_A_key()
    #    elif ball.xcor() <= 0:
    #        Player_B_key()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
        if random.random() > random_ratio:
            ball.dx *= 1.5
            ball.dy *= 1.5
            speed_lv += 1
            pen2.clear()
            pen2.write("Speed Up!! Lv = {}".format(speed_lv), align="center",
                       font=("Arial",  26, "normal"))

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
        if random.random() > random_ratio:
            ball.dx *= 1.5
            ball.dy *= 1.5
            speed_lv += 1
            pen2.clear()
            pen2.write("Speed Up!! Lv = {}".format(speed_lv), align="center",
                       font=("Arial",  26, "normal"))

    # Get Point
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {} ".format(score_a, score_b),
                  align="center",  font=("Arial",  24, "normal"))
        now_score_a = True

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {} ".format(score_a, score_b),
                  align="center", font=("Arial", 24, "normal"))
        now_score_b = True

    # paddle and ball collision

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 55 and ball.ycor() > paddle_b.ycor() - 55):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 55 and ball.ycor() > paddle_a.ycor() - 55):
        ball.setx(-340)
        ball.dx *= -1

# Game Finish!!
pen.clear()
ball.clear()
paddle_a.clear()
paddle_b.clear()
pen.goto(0, 0)

if score_a > score_b:
    pen.write("Player A Win!!", align="center", font=("Arial", 24, "normal"))
elif score_a < score_b:
    pen.write("Player B Win", align="center", font=("Arial", 24, "normal"))
else:
    pen.write("Draw", align="center", font=("Arial", 24, "normal"))

time.sleep(2)
