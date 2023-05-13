from turtle import Turtle, Screen
import time
from cursor import Cursor
starting_positions = [(0,150), (0, 100), (0, 50), (0, 0), (0, -50), (0, -100)]
level_of_difficulties = [0.3, 0.25, 0.15, 0.1, 0.05, 0.25]
index_of_difficulty = 0
difficulties = ["Escolha a Dificuldade:","Muito fácil","Fácil","Médio", "Difícil","Muito Difícil"]


class Difficulty(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.speed("fastest")
        self.penup()
        self.color("green")
        self.goto(0, 270)
        self.write_prompt()

    def write_prompt(self):
        for position in starting_positions:
            self.goto(position)
            list_difficulty = difficulties[starting_positions.index(position)]
            self.write(f" {list_difficulty} ", move=True, align="center", font=('Courier', 20, 'bold'))


def screen_control():
    difficulty.clear()
    cursor.hideturtle()
    global index_of_difficulty
    index_of_difficulty = cursor.index
    global cursor_is_on
    cursor_is_on = False


#screen = Screen()
#difficulty = Difficulty()
#cursor = Cursor()

#screen.listen()
#screen.onkey(cursor.up,"Up")
#screen.onkey(cursor.down,"Down")
#screen.onkey(screen_control, "Return")

#cursor_is_on = True
#while cursor_is_on:
#    screen.update()
#    time.sleep(0.2)



#print(level_of_difficulties[index_of_difficulty])


#screen.exitonclick()