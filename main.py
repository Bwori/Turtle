import turtle

nyota = turtle.Turtle()
nyota.getscreen().bgcolor("#994444")
nyota.penup()
nyota.goto((-200,100))
nyota.pendown()

def star(turtle, size):
	if size <= 10:
		return
	else:
		turtle.begin_fill()
		for i in range(5):

			turtle.forward(size)
			star(turtle, size/3)
			turtle.left(216)
		turtle.end_fill()

star(nyota, 360)

turtle.done()