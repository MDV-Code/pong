from ball import Ball
from players import Players
from steuerung import Steuerung
from kollider import Kollider
from turtle import Screen
from map import Map


screen = Screen()
screen.tracer(0)
screen.listen()

players = Players()

steuerung = Steuerung(screen, players)


map = Map()
ball = Ball()

kollider = Kollider()

ball.setheading(135)

screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    players.player_movement()
    kollider.kollisions_detektor_player1(ball, players.player1, screen)
    kollider.kollisions_detektor_player2(ball, players.player2, screen)
    kollider.kollisions_rand(ball, map, screen)

    
    
        
screen.exitonclick()
