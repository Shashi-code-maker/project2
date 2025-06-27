import turtle as t
import random

d = 0.1 # delay
s = 0 # score
hs = 0 # high_score

# screen
sc = t.Screen()
sc.title("Snake Game")
sc.bgcolor("blue")
sc.setup(width=600, height=600)
sc.tracer(0)

# snake head
h = t.Turtle()
h.shape("square")
h.color("white")
h.penup()
h.goto(0, 0)
h.direction = "Stop"

# food
f = t.Turtle()
f.speed(0)
f.shape(random.choice(['square', 'triangle', 'circle']))
f.color(random.choice(['red', 'green', 'black']))
f.penup()
f.goto(0, 100)

# score display
p = t.Turtle()
p.speed(0)
p.shape("square")
p.color("white")
p.penup()
p.hideturtle()
p.goto(0, 250)
p.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))