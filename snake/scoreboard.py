import turtle

class Scoreboard(turtle.Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.color("white")
		self.hideturtle()
		self.penup()
		self.goto(-20, 270)
		self.update_scoreboard()
	
	def update_scoreboard(self):
		self.clear()
		self.write(arg=f"Score: {self.score}", align="center", font= ('Arial', 20, 'normal'))
	
	def game_over(self):
		self.goto(0,0)
		self.write(arg=f"Game Over", align="center", font= ('Arial', 30, 'normal'))


	def increment_score(self):
		self.score += 1
		self.update_scoreboard()
