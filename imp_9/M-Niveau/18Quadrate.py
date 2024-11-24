import turtle as tr

def quadrat(seitenlaenge):
    for _ in range(4):
        tr.forward(seitenlaenge)
        tr.right(90)

screen = tr.Screen()
screen.bgcolor("white")

tr.speed(1)

for i in range(18):
    quadrat(60)
    tr.right(20)

tr.hideturtle()

tr.done()
