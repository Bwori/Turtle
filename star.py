import turtle

nyota = turtle.Turtle()

nyota.getscreen().bgcolor("cyan")

def star(nyota):
    nyota.forward(200)
    nyota.left(216)
    nyota.forward(200)
    nyota.left(216)
    nyota.forward(200)
    nyota.left(216)
    nyota.forward(200)
    nyota.left(216)
    nyota.forward(200)

star(nyota)
turtle.done()