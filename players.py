from turtle import Turtle
import random

class Players(Turtle):
    def __init__(self):
        self.player1 = []
        self.player1_position = [(-420,-100),(-420,-80),(-420,-60),(-420,-40),(-420,-20)]
        self.player1_up = False
        self.player1_down = False

        self.player2 = []
        self.player2_position = [(420,100),(420,80),(420,60),(420,40),(420,20)]
        self.player2_up = False
        self.player2_down = False
        
        self.colors = ["red", "blue", "green", "yellow", "purple", "pink", "magenta"]
        
        for position in self.player1_position:
            new_segment_player1 = Turtle("square")
            new_segment_player1.color("black")
            new_segment_player1.penup()
            new_segment_player1.goto(position)
            self.player1.append(new_segment_player1)
            
        for position in self.player2_position:
            new_segment_player2 = Turtle("square")
            new_segment_player2.color("black")
            new_segment_player2.penup()
            new_segment_player2.goto(position)
            self.player2.append(new_segment_player2)
        
    def player_movement(self):
        for i in self.player1:
            if self.player1_up and self.player1[4].ycor() != 360:
                i.setheading(90)
                i.forward(5)
            elif self.player1_down and self.player1[4].ycor() != -280:
                i.setheading(270)
                i.forward(5)
        for i in self.player2:
            if self.player2_up and self.player2[4].ycor() != 280:
                i.setheading(90)
                i.forward(5)
            elif self.player2_down and self.player2[4].ycor() != -360:
                i.setheading(270)
                i.forward(5)
 
    def up_player1(self):
        self.player1_up = True
            
    def release_up_player1(self):
        self.player1_up = False

    def down_player1(self):
        self.player1_down = True
            
    def release_down_player1(self):
        self.player1_down = False
        
    def up_player2(self):
        self.player2_up = True
            
    def release_up_player2(self):
        self.player2_up = False

    def down_player2(self):
        self.player2_down = True
            
    def release_down_player2(self):
        self.player2_down = False
    
    def change_color_timer1(self, screen):
        x = random.randint(0,6)
        for segment in self.player1:
            segment.color(self.colors[x])
        screen.update()
        for segment in self.player1:
            segment.color("black")
        screen.update()
        for segment in self.player1:
            segment.color(self.colors[x])
        screen.update()
        for segment in self.player1:
            segment.color("black")
        screen.update()    
        
    def change_color_timer2(self, screen):
        x = random.randint(0,6)
        for segment in self.player1:
            segment.color(self.colors[x])
        screen.update()
        for segment in self.player1:
            segment.color("black")
        screen.update()
        for segment in self.player1:
            segment.color(self.colors[x])
        screen.update()
        for segment in self.player1:
            segment.color("black")
        screen.update()    
