# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)

# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()

#     # Detect collision with food.
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         scoreboard.increase_score()

#     # Detect collision with wall.
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_on = False
#         scoreboard.game_over()

#     # Detect collision with tail.
#     for segment in snake.segments:
#         if segment == snake.head:
#             pass
#         elif snake.head.distance(segment) < 10:
#             game_is_on = False
#             scoreboard.game_over()





# screen.exitonclick()

import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def draw_turtle(canvas):
    turtle_screen = turtle.TurtleScreen(canvas)
    turtle_screen.bgcolor("black")
    turtle_screen.title("My Snake Game")
    turtle_screen.tracer(0)

    t = turtle.Turtle()
    t.speed('fastest')

    snake = Snake(t)
    food = Food(t)
    scoreboard = Scoreboard(t)

    turtle_screen.listen()
    turtle_screen.onkey(snake.up, "Up")
    turtle_screen.onkey(snake.down, "Down")
    turtle_screen.onkey(snake.left, "Left")
    turtle_screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        t.clear()
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food.turtle) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail.
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

        food.draw()
        snake.draw()
        scoreboard.draw()

        turtle_screen.update()

    turtle_screen.bye()
