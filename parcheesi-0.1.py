#!/usr/bin/python

#Parcheesi
#
#Written by Eric Mesa
#Graphics by Eric Mesa
#
#Version 0.1

#TODO
#-fix up game logic to detect if there's another piece in the same square and determine whether to eat or form a blockade
#-alow players to select their color (but for now just have it assigned automatically)
#-fix up game logic so that there are turns between players
#-allow players to select which piece will move the amount on each die
#-fix up blit so that it updates on turns

import pygame, random

class Piece():
    """This is a piece for the game
    Returns piece object
    Functions:  update_pos
    Attributes:  position"""
    
    def __init__(self, position, color):
        self.image = pygame.image.load(color+'_guy.png')
        self.position = position
        self.original_pos = position
        self.inbase = True
        self.space = 0

    def leave_base(self, new_position):
        self.inbase = False
        self.position = new_position

    def update_pos(self,new_position):
        self.position = new_position

    def eaten(self):
        self.position=self.original_pos
        self.inbase = True


class Board():
    """This class controls the board 
    and is responsible for turning spaces
    on the board into coordinates
    Functions:  translate
    Attributes:  spaces, spaces2, locations"""

    def __init__(self):
        self.image = pygame.image.load('parcheesi_board.png').convert()
        self.spaces = {1:(238,8), 2:(240,34),3:(240,61),4:(240,87),5:(240,113), 6:(240, 140), 7:(240,168),8:(243,202),9:(195,243), 10:(168, 240), 11:(140, 240), 12:(115, 240), 13:(86,240), 14:(60,240), 15:(34, 240), 16:(7,240), 17:(7,315), 18:(7,385), 19:(35, 385), 20:(61, 385), 21:(88, 385), 22:(115, 388), 23:(142,385), 24:(168, 385), 25:(193, 372), 26:(243, 387), 27:(243, 415), 28:(243,440), 29:(243, 467), 30:(243, 496), 31:(243, 523), 32:(243, 549), 33:(243, 575), 34:(314, 575), 35:(385, 575), 36:(385, 547), 37:(385, 524), 38:(385, 497), 39:(385, 467), 40:(385, 440), 41:(385, 416), 42:(373, 387), 43:(386, 338), 44:(413, 338), 45:(440, 338), 46:(465, 338), 47:(494, 338), 48:(521, 338), 49:(545, 338), 50:(573, 338), 51:(573, 267), 52:(577, 200), 53:(545, 200), 54:(519, 200), 55:(494, 200), 56:(467, 200), 57:(437, 200), 58:(413, 200), 59:(389, 207), 60:(370, 192), 61:(387, 168), 62:(387, 139), 63:(387, 112), 64:(387, 86), 65:(387, 60), 66:(387, 34), 67:(387, 6), 68:(310, 6) }
        self.spaces2 = {}
        self.location = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.location_old =  [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.blue_locations = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.red_locations = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.yellow_locations = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.green_locations = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        #for roll_box, first tuple is xmin and xmax and second is ymin and ymax
        self.rollbox = ((613, 787), (102, 184))
        #print len(self.blue_locations)

    def translate(self,space):
        """Translates pices to coordinates"""

    #spaces should be a dictionary with coordinates for each space on the board
    #spaces2 should be the coordinates for when there are two pieces on the board

class Dice():
    def __init__(self):
        self.die1 = 0
        self.die2 = 0
    
    def roll(self):
        self.die1 = random.randint(1,6)
        self.die2 = random.randint(1,6)

class Player():
    def __init__(self, color):
        if color == "blue":
            self.piece1 = Piece((25,450), "blue")
            self.piece2 = Piece((25,500), "blue")
            self.piece3 = Piece((50, 450), "blue")
            self.piece4 = Piece((50, 500), "blue")
            self.startingpos = 22
        elif color == "red":
            self.piece1 = Piece((500, 450), "red")
            self.piece2 = Piece((525, 450), "red")
            self.piece3 = Piece((500, 500), "red")
            self.piece4 = Piece((525, 500), "red")
            self.startingpos = 39
        elif color == "yellow":
            self.piece1 = Piece((25, 25), "yellow")
            self.piece2 = Piece((50, 25), "yellow")
            self.piece3 = Piece((25, 75), "yellow")
            self.piece4 = Piece((50, 75), "yellow")
            self.startingpos = 5
        elif color == "green":
            self.piece1 = Piece((500,25), "green")
            self.piece2 = Piece((525, 25), "green")
            self.piece3 = Piece((500, 75), "green")
            self.piece4 = Piece((525, 75), "green")
            self.startingpos = 56
            

def main():
    #Init
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Parcheesi')
    done = False
    
    #Players/board/dice
    player1 = Player("blue")
    player2 = Player("red")
    player3 = Player("yellow")
    player4 = Player("green")
    players = (player1, player2, player3, player4)
    board = Board()
    dice = Dice()

    while done == False:
        screen.blit(board.image, (0,0))
        for player in players:
            screen.blit(player.piece1.image, (player.piece1.position))
            screen.blit(player.piece2.image, (player.piece2.position))
            screen.blit(player.piece3.image, (player.piece3.position))
            screen.blit(player.piece4.image, (player.piece4.position))

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_ESCAPE:
                    done = True
            if e.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x > board.rollbox[0][0] and x < board.rollbox[0][1] and y > board.rollbox[1][0] and y < board.rollbox[1][1]: 
                    for player in players:
                        dice.roll()
                        dice_total = dice.die1 + dice.die2
                        print dice_total
                        if player.piece1.inbase:
                            if dice.die1 == 5 or dice.die2 == 5:
                                #may want to use modulo 68 here so it doesn't crash
                                player.piece1.leave_base(board.spaces[player.startingpos+dice_total])
                                player.piece1.inbase = False
                                board.location[21+dice_total][0]=1
                                player.piece1.space = player.startingpos + dice_total
                        if not player.piece1.inbase:
                            player.piece1.update_pos(board.spaces[player.piece1.space + dice_total])
                            player.piece1.space = player.piece1.space + dice_total
                            board.location = board.location_old
                            board.location[player1.piece1.space + dice_total-1][0] = 1
                        pygame.display.flip()
            #if e.type == pygame.MOUSEBUTTONDOWN:
            #    print pygame.mouse.get_pos()
            #    player1.piece1.update_pos(pygame.mouse.get_pos())
#print e.button

if __name__ == '__main__':main()
