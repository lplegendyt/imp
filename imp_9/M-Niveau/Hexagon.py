import turtle as tr

def hexagon(seitenlaenge):
    for _ in range(6):
        tr.forward(seitenlaenge)
        tr.left(60)

tr.speed(1)

hexagon(60)

tr.hideturtle()

tr.done()
