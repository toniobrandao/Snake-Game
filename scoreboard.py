# -*- coding: utf-8 -*-
"""
Created on Fri May 12 12:19:30 2023

@author: antoniobrandao
"""
from turtle import Turtle, Screen
import time 

class ScoreBoard(Turtle):
        def __init__(self):
            super().__init__()
            self.hideturtle()
            self.score = 0
            self.speed("fastest")
            self.penup()
            self.color("green")
            self.goto(0,270)
            self.write_score()
        
        def write_score(self):
            self.goto(0,270)
            self.write(f"SCORE: {self.score} ", move=True, align="center", font=('Courier', 15, 'bold'))
        def game_over(self):
            self.goto(0, 0)
            self.write('GAME OVER', move=True, align="center", font=('Courier', 30, 'bold') )


        def update_score(self):
            self.score +=1
            self.clear()
            self.write_score()
            
                       
