import turtle as tr

def kreis(radius):
    tr.pensize(2)
    tr.circle(radius)

tr.speed(1)

for i in range(10):
    kreis(30)
    tr.left(36)

tr.hideturtle()

tr.done()
