#!/usr/bin/python

#Parcheesi
#
#Written by Eric Mesa
#Graphics by Eric Mesa
#
#Version 0.3

#TODO
#-update spaces2 so that when two are on the same space they look correct then implement capturing/blocking
#-alow players to select their color (but for now just have it assigned automatically)
#-allow players to select which piece will move the amount on each die
#-location is not detecting who's there, but may be unnecessary if I can compare spaces....

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
        self.left = False
        self.right = False

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
        #
        self.spaces2 = {1:(190,8), 2:(190,34),3:(190,61),4:(190,87),5:(190,113), 6:(190, 140), 7:(190,168),8:(190,202),9:(195,190), 10:(168, 190), 11:(140, 190), 12:(115, 190), 13:(86,190), 14:(60,190), 15:(34, 190), 16:(7,190), 17:(7,265), 18:(7,325), 19:(35, 335), 20:(61, 335), 21:(88, 335), 22:(115, 335), 23:(142,335), 24:(168, 335), 25:(193, 335), 26:(200, 387), 27:(193, 415), 28:(193,440), 29:(193, 467), 30:(193, 496), 31:(193, 523), 32:(193, 549), 33:(193, 575), 34:(293, 575), 35:(335, 575), 36:(335, 547), 37:(335, 524), 38:(335, 497), 39:(335, 467), 40:(335, 440), 41:(335, 416), 42:(333, 387), 43:(386, 378), 44:(413, 388), 45:(440, 388), 46:(465, 388), 47:(494, 388), 48:(521, 388), 49:(545, 388), 50:(573, 438), 51:(573, 317), 52:(577, 250), 53:(545, 250), 54:(519, 250), 55:(494, 250), 56:(467, 250), 57:(437, 250), 58:(413, 250), 59:(389, 247), 60:(330,192), 61:(337, 168), 62:(337, 139), 63:(337, 112), 64:(337, 86), 65:(337, 60), 66:(337, 34), 67:(337, 6), 68:(330, 6) }
        self.location = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        #self.location_old =  [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
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
        self.rolled = False
    
    def roll(self):
        self.die1 = random.randint(1,6)
        self.die2 = random.randint(1,6)
        self.rolled = True

class Player():
    def __init__(self, color):
        if color == "blue":
            self.piece1 = Piece((25,450), "blue")
            self.piece2 = Piece((25,500), "blue")
            self.piece3 = Piece((50, 450), "blue")
            self.piece4 = Piece((50, 500), "blue")
            self.startingpos = 22
            self.playername = "blue"
        elif color == "red":
            self.piece1 = Piece((500, 450), "red")
            self.piece2 = Piece((525, 450), "red")
            self.piece3 = Piece((500, 500), "red")
            self.piece4 = Piece((525, 500), "red")
            self.startingpos = 39
            self.playername = "red"
        elif color == "yellow":
            self.piece1 = Piece((25, 25), "yellow")
            self.piece2 = Piece((50, 25), "yellow")
            self.piece3 = Piece((25, 75), "yellow")
            self.piece4 = Piece((50, 75), "yellow")
            self.startingpos = 5
            self.playername = "yellow"
        elif color == "green":
            self.piece1 = Piece((500,25), "green")
            self.piece2 = Piece((525, 25), "green")
            self.piece3 = Piece((500, 75), "green")
            self.piece4 = Piece((525, 75), "green")
            self.startingpos = 56
            self.playername = "green"
            

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
    playerindex = 0
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
                    dice.roll()
                    #for debugging purposes
                    print "dice1:",dice.die1 
                    print "dice2: ", dice.die2
        
        if dice.rolled == True:
            dice_total = dice.die1 + dice.die2
            #for debugging purposes
            print players[playerindex].playername
            if players[playerindex].piece1.inbase:
                if dice.die1 == 5 or dice.die2 == 5:
                    #may want to use modulo 68 here so it doesn't crash
                    players[playerindex].piece1.leave_base(board.spaces[(players[playerindex].startingpos+dice_total)%68])
                    players[playerindex].piece1.inbase = False
                    board.location[(players[playerindex].startingpos-1)+dice_total][0]=1
                    players[playerindex].piece1.space = (players[playerindex].startingpos + dice_total)%68
                    #for debugging purposes
                    print players[playerindex].playername + "'s space:", players[playerindex].piece1.space
                    players[playerindex].piece1.left = True
                    #for debugging purposes
                    print board.location
            elif not players[playerindex].piece1.inbase:
                if (players[playerindex].piece1.space + dice_total)%68 == 0:
                    players[playerindex].piece1.update_pos(board.spaces[(players[playerindex].piece1.space + dice_total+1)%68])
                    #for debugging purposes
                    print board.location
                else:
                    players[playerindex].piece1.update_pos(board.spaces[(players[playerindex].piece1.space + dice_total)%68])
                board.location[(players[playerindex].piece1.space + dice_total-1)%68][0] = 0
                players[playerindex].piece1.space = (players[playerindex].piece1.space + dice_total)%68
                #for debugging purposes
                print players[playerindex].playername + "'s space:", players[playerindex].piece1.space
                board.location[(players[playerindex].piece1.space + dice_total-1)%68][0] = 1
                #for debugging purposes
                print board.location
                pygame.display.flip()
            dice.rolled = False
            if playerindex < 3:
                playerindex = playerindex + 1
            else:
                playerindex = 0
            #if e.type == pygame.MOUSEBUTTONDOWN:
            #    print pygame.mouse.get_pos()
            #    player1.piece1.update_pos(pygame.mouse.get_pos())
#print e.button

if __name__ == '__main__':main()
