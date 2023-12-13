import turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
	def __init__(self) -> None:
		self.body = []
		self.createsnake()
		self.head = self.body[0]
	
	def createsnake(self):
		for position in starting_position:
			self.add_segment(position)
	
	def add_segment(self, position):
		snake = turtle.Turtle("square")
		snake.color("white")
		snake.penup()
		snake.goto(position)
		self.body.append(snake)

	def extend(self):
		self.add_segment(self.body[-1].position())
	
	def move(self):
		for part in range(len(self.body) - 1, 0, -1):
			newx = self.body[part - 1].xcor()
			newy = self.body[part - 1].ycor()
			self.body[part].goto(newx, newy)
		self.body[0].forward(MOVE_DISTANCE)

	
	def up(self):
		if self.head.heading() != 270:
			self.head.setheading(90)

	def down(self):
		if self.head.heading() != 90:
			self.head.setheading(270)

	def left(self):
		if self.head.heading() != 0:
			self.head.setheading(180)

	def right(self):
		if self.head.heading() != 180:
			self.head.setheading(0)

