from pygame import *

init()
screen = display.set_mode((800, 600))
display.set_caption('Parcheesi Board')

background = image.load('parcheesi_board.png').convert()
blue = image.load('blue_guy.png')
green = image.load('green_guy.png')
yellow = image.load('yellow_guy.png')
red = image.load('red_guy.png')

while 1:
    screen.blit(background, (0,0))
    screen.blit(blue, (10, 10))
    screen.blit(green, (20, 20))
    screen.blit(yellow, (30, 30))
    screen.blit(red, (40, 40))
    
    
    display.flip()
