from turtle import Turtle
import time
from turtle import Screen

screen = Screen()
screen.tracer(0)

player1 = []
player1_up = False
player1_down = False

player1_position = [(-420,-100),(-420,-80),(-420,-60),(-420,-40),(-420,-20)]
for position in player1_position:
            new_segment_player1 = Turtle("square")
            new_segment_player1.color("black")
            new_segment_player1.penup()
            new_segment_player1.goto(position)
            player1.append(new_segment_player1)
            
def player_movement():
        for i in player1:
            if player1_up and player1[4].ycor() != 360:
                i.setheading(90)
                i.forward(5)
            elif player1_down and player1[4].ycor() != -280:
                i.setheading(270)
                i.forward(5)
                
def up_player1():
    global player1_up
    player1_up = True
            
def release_up_player1():
    global player1_up
    player1_up = False

def down_player1():
    global player1_down
    player1_down = True
        
def release_down_player1():
    global player1_down
    player1_down = False
    
screen.listen()
screen.onkeypress(up_player1, "Up")
screen.onkeypress(down_player1, "Down")

screen.onkeyrelease(release_up_player1, "Up")
screen.onkeyrelease(release_down_player1, "Down")

screen.update()
game_is_on = True
while game_is_on:
    time.sleep(0.009)
    screen.update()
    player_movement()

screen.exitonclick()