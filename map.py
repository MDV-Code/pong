from turtle import Turtle
import random

class Map:
    def __init__(self):
        self.map_segments = []
        self.positions = []
        self.emptypositions = []
        self.position_maker()
        self.map_generate()
        self.colors = ["red", "blue", "green", "yellow", "purple", "pink", "magenta"]
        
    def map_generate(self):
        for position in self.positions:
            wand_teil = Turtle("square")
            wand_teil.penup()
            wand_teil.color("black")
            wand_teil.goto(460,position)
            self.map_segments.append(wand_teil)
            
        for position in self.positions:
            wand_teil = Turtle("square")
            wand_teil.penup()
            wand_teil.color("black")
            wand_teil.goto(-460,position)
            self.map_segments.append(wand_teil)
            
        for position in self.positions:
            wand_teil = Turtle("square")
            wand_teil.penup()
            wand_teil.color("black")
            wand_teil.goto(position, 380)
            self.map_segments.append(wand_teil)
            
        for position in self.positions:
            wand_teil = Turtle("square")
            wand_teil.penup()
            wand_teil.color("black")
            wand_teil.goto(position, -380)
            self.map_segments.append(wand_teil)
            
        for position in self.emptypositions:
            wand_teil = Turtle("square")
            wand_teil.penup()
            wand_teil.color("black")
            wand_teil.goto(position, -380)
            self.map_segments.append(wand_teil)
            
        for position in self.emptypositions:
            wand_teil = Turtle("square")
            wand_teil.penup()
            wand_teil.color("black")
            wand_teil.goto(position, 380)
            self.map_segments.append(wand_teil)
        
    def position_maker(self):
        for position in range(-380, 400, 20):
            self.positions.append(position)
            
        for position in range(400, 460, 20):
            self.emptypositions.append(position)
            
        for position in range(-440, -380, 20):
            self.emptypositions.append(position)
            
    def change_color_timer(self, screen):
        x = random.randint(0,6)
        for segment in self.map_segments:
            segment.color(self.colors[x])
        screen.update()
        for segment in self.map_segments:
            segment.color("black")
        screen.update()
        for segment in self.map_segments:
            segment.color(self.colors[x])
        screen.update()
        for segment in self.map_segments:
            segment.color("black")
        screen.update()

            
        
        

        
    
        
            
        