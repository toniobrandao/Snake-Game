# -*- coding: utf-8 -*-
"""
Created on Wed May 10 08:29:16 2023

@author: antoniobrandao
"""

from turtle import Turtle,  Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from difficulty import Difficulty
from cursor import Cursor

screen = Screen()


level_of_difficulties = [0.3, 0.25, 0.15, 0.1, 0.05, 0.25]
screen.setup(width=600, height = 600)

screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

difficulty = Difficulty()
cursor = Cursor()

# No futuro, tenho que definir essa função em outro lugar
index_of_difficulty = 0
cursor_is_on = True

def screen_control():
    difficulty.clear()
    cursor.hideturtle()
    global index_of_difficulty
    index_of_difficulty = cursor.index
    global cursor_is_on
    cursor_is_on = False

screen.listen()
screen.onkey(cursor.up ,"Up")
screen.onkey(cursor.down ,"Down")
screen.onkey(screen_control , "Return")

while cursor_is_on:
    screen.update()
    time.sleep(0.2)


snake = Snake()
food= Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(level_of_difficulties[index_of_difficulty])
    snake.move()
    
    #Detect collision with food:
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.update_score()
    #Detect collision with food:
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        game_is_on = False
    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
    #if head collides with any segment in the tail:
        #trigger game_over


screen.exitonclick()

