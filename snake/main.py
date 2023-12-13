import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def clear():
	screen.bye()

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(clear, "q")

turtle_text = Scoreboard()
game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move()
	if snake.head.distance(food) < 15:
		food.refresh()
		turtle_text.increment_score()
		snake.extend()
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		game_is_on = False
		turtle_text.game_over()
	for position in snake.body:
		if position == snake.head:
			pass
		elif snake.head.distance(position) < 10:
			game_is_on = False
			turtle_text.game_over()












screen.exitonclick()