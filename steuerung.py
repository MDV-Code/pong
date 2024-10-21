class Steuerung():
    def __init__(self, screen, players):
       self.controller(screen, players) 

    def controller(self, screen, players):
        screen.onkeypress(players.up_player1, "Up")
        screen.onkeypress(players.down_player1, "Down")

        screen.onkeyrelease(players.release_up_player1, "Up")
        screen.onkeyrelease(players.release_down_player1, "Down")

        screen.onkeypress(players.up_player2, "w")
        screen.onkeypress(players.down_player2, "s")

        screen.onkeyrelease(players.release_up_player2, "w")
        screen.onkeyrelease(players.release_down_player2, "s")