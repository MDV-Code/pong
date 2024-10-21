from turtle import Turtle
import time
import random

class Ball(Turtle):
    def __init__(self, anfangs_richtung = random.randint(0,1)):
        super().__init__()
        self.shape("circle")
        self.goto(0, 0)
        self.penup()
        self.color("red")
        self.shapesize(2)
        self.ball_geschwindigkeit = 0.00025
        self.anfangs_richtung = anfangs_richtung
        self.ball_absolute_geschwindigkeit = 5
        self.anfang()
    ######################## BEWEGUNG DES BALLS
    def move(self):
            self.forward(self.ball_absolute_geschwindigkeit)
            time.sleep(self.ball_geschwindigkeit)
    
    def anfang(self):
        if self.anfangs_richtung == 1:
            self.setheading(180)
        if self.anfangs_richtung == 0:
            self.setheading(0)

        
        