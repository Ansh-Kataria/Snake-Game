# Snake Game
# Made By Ansh Kataria
# Date 6 December 2020


import turtle
import time
import random

# delay
delay = 0.1

# Score
score = 0
high_score = 0

# Segments
segments = []

# Set up the screen
screen = turtle.Screen()
screen.title("Snake By Ansh Kataria")
screen.bgcolor("light blue")
screen.setup(width=600, height=600)
screen.tracer(0)

# Register shape
screen.register_shape("food.gif")
screen.register_shape("body.gif")
screen.register_shape("snake_up.gif")
screen.register_shape("snake_down.gif")
screen.register_shape("snake_left.gif")
screen.register_shape("snake_right.gif")

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("snake_right.gif")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("food.gif")
food.color("red")
food.penup()
food.goto(0, 100)


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions

def go_up():
    if head.direction != "down":
        head.direction = "up"
        head.shape("snake_up.gif")


def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.shape("snake_down.gif")


def go_right():
    if head.direction != "left":
        head.direction = "right"
        head.shape("snake_right.gif")


def go_left():
    if head.direction != "right":
        head.direction = "left"
        head.shape("snake_left.gif")


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    elif head.direction == "down":
        head.sety(head.ycor() - 20)

    elif head.direction == "left":
        head.setx(head.xcor() - 20)

    elif head.direction == "right":
        head.setx(head.xcor() + 20)


# Key Bindings

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

while True:
    screen.update()

    # Check collision between snake and border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 235 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check collision between food and snake head
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 235)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("body.gif")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10
        high_score = max(score, high_score)

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segment first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move the segment 0 in the place of head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)

            # Hide the segments
            for seg in segments:
                seg.goto(1000, 1000)

            # clear the segments
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
