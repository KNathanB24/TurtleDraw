import turtle
import math

screen = turtle.Screen()
screen.setup(450, 450)

t = turtle.Turtle()
t.speed(0)

total_distance = 0
prev_x = None
prev_y = None

filename = input("Enter input file name: ")
file = open(filename, "r")

for line in file:
    line = line.strip()

    if line == "stop":
        t.penup()
        prev_x = None
        prev_y = None
        continue

    components = line.split()
    color = components[0]
    x = int(components[1])
    y = int(components[2])

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

t.penup()
t.goto(100, -200)
t.write("Total Distance: " + str(round(total_distance, 2)))

input("Press Enter to exit...")

try:
    turtle.bye()
except turtle.Terminator:
    pass