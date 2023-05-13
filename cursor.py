from turtle import Turtle, Screen
import time
cursor_locations = [ (-100, 120), (-80, 70), (-80, 20) , (-80, -30), (-120, -80)]
class Cursor(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.penup()
        self.color("green")
        self.shapesize(2,2)
        self.goto(cursor_locations[2])
        self.index = cursor_locations.index(self.position())


    def up(self):
        if self.index != 0:
            self.index -= 1
            self.goto(cursor_locations[self.index])

    def down(self):
        if self.index != 4:
            self.index += 1
            self.goto(cursor_locations[self.index])


