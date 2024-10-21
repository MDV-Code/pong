from map import Map

class Kollider():
    def __init__(self):
        pass
    ############################ PLAYER 1 KOLLISION       
    def kollisions_detektor_player1(self, ball, player1, screen):
        head = ball.heading()
        if abs(player1[0].ycor() - ball.ycor()) < 30 and abs(player1[0].xcor() - ball.xcor()) < 25:
            if head > 180 and head <= 360:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.5
                    
            else:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.5          
        if abs(player1[1].ycor() - ball.ycor()) < 30 and abs(player1[1].xcor() - ball.xcor()) < 25:
            if head > 180 and head <= 360:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.3

            else:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.3
       
        if abs(player1[2].ycor() - ball.ycor()) < 30 and abs(player1[2].xcor() - ball.xcor()) < 25:
            if head > 180 and head <= 360:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit - 0.7

            else:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit - 0.7
       
        if abs(player1[3].ycor() - ball.ycor()) < 30 and abs(player1[3].xcor() - ball.xcor()) < 25:
            if head > 180 and head <= 360:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.2

            else:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.2
     
        if abs(player1[4].ycor() - ball.ycor()) < 30 and abs(player1[4].xcor() - ball.xcor()) < 25:
            if head > 180 and head <= 360:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.5

            else:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.5
         
    
    ############################ PLAYER 2 KOLLISION
                    
    def kollisions_detektor_player2(self, ball, player2, screen):
        head = ball.heading()
        if abs(player2[0].ycor() - ball.ycor()) < 30 and abs(player2[0].xcor() - ball.xcor()) < 25:
            if head > 180 and head <= 360:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.5

            else:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.5          
            
        if abs(player2[1].ycor() - ball.ycor()) < 30 and abs(player2[1].xcor() - ball.xcor()) < 25:
            if head > 180 and head <= 360:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.3

            else:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.3
            
        if abs(player2[2].ycor() - ball.ycor()) < 30 and abs(player2[2].xcor() - ball.xcor()) < 25:
            if head > 180 and head <= 360:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit - 0.7

            else:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit - 0.7
            
        if abs(player2[3].ycor() - ball.ycor()) < 30 and abs(player2[3].xcor() - ball.xcor()) < 25:
            if head > 180 and head <= 360:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.2

            else:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.2
            
        if abs(player2[4].ycor() - ball.ycor()) < 30 and abs(player2[4].xcor() - ball.xcor()) < 25:
            if head > 180 and head <= 360:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.5

            else:
                ball.setheading(self.spiegelungs_rechner_y(head))
                if ball.ball_absolute_geschwindigkeit < 10:
                    ball.ball_absolute_geschwindigkeit = ball.ball_absolute_geschwindigkeit + 0.5
          
    ############################ WAND KOLLISION        
            
    def kollisions_rand(self, ball, map, screen):
        head = ball.heading()
        if abs(ball.ycor()) >= 360:
            ball.setheading(self.spiegelungs_rechner_x(head))
            map.change_color_timer(screen)
        elif abs(ball.xcor()) >= 440:
            ball.setheading(self.spiegelungs_rechner_y(head))
            map.change_color_timer(screen)
     
             
    
    ############################ SPIEGEL FUNKTIONEN
            
    def spiegelungs_rechner_x(self, head):
        return abs(head - 2 * 180)
    
    def spiegelungs_rechner_y(self, head):
        return abs(head + 90)
                
            
                

            
            