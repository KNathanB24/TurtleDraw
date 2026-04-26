import turtle
import math

screen = turtle.Screen()
screen.setup(450, 450)

t = turtle.Turtle()
t.speed(0)

total_distance = 0
prev_x = None
prev_y = None

filename = "turtle-draw-data.txt"
file = open(filename, "r")

for line in file:
    line = line.strip()

    if line == "stop":
        t.penup()
        prev_x = None
        prev_y = None
        continue

    parts = line.split()
    color = parts[0]
    x = int(parts[1])
    y = int(parts[2])

    t.color(color)

    if prev_x is None:
        t.penup()
        t.goto(x, y)
        t.pendown()
    else:
        dx = x - prev_x
        dy = y - prev_y
        total_distance += math.sqrt(dx*dx + dy*dy)

        t.goto(x, y)

    prev_x = x
    prev_y = y

file.close()

# display total distance
t.penup()
t.goto(100, -200)
t.write("Total Distance: " + str(round(total_distance, 2)))

# REQUIRED: wait for user input BEFORE closing
input("Press Enter to exit...")

# safely close turtle AFTER enter
try:
    turtle.bye()
except turtle.Terminator:
    pass