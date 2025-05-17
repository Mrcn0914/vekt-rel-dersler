import turtle
colors = ["red"]

t=turtle.Turtle()
t.speed(10)

for i in range(40):
    t.color(colors)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(60)
    t.right(10)

turtle.done()