import turtle as tr

def hexagon(seitenlaenge):
    for _ in range(6):
        tr.forward(seitenlaenge)
        tr.left(60)

def honigwabe(seitenlaenge):
    hexagon(seitenlaenge)
    tr.forward(seitenlaenge)
    hexagon(seitenlaenge)
    tr.backward(seitenlaenge)
    tr.left(60)
    tr.forward(seitenlaenge)
    tr.right(60)
    hexagon(seitenlaenge)
    tr.backward(seitenlaenge)
    tr.left(60)
    tr.forward(seitenlaenge)
    tr.right(60)
    hexagon(seitenlaenge)
    tr.backward(seitenlaenge)

screen = tr.Screen()
screen.bgcolor("white")

tr.speed(5)

honigwabe(50)

tr.hideturtle()

tr.done()