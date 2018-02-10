import pygame  # imports PyGame
from pygame.locals import *  # imports more stuff from pygame

pygame.init()  # initializes PyGame
screen = pygame.display.set_mode((800, 600))  # sets size for screen

pygame.display.set_caption("Blank Screen")  # sets the caption of the screen

clock = pygame.time.Clock()  # the "clock" of PyGame, and the thing making the ticks of the game

game_is_running = True  # variable establishing whether game is running or not

while game_is_running:  # while loop

    clock.tick(60)  # number of fps (frames per second)

    for event in pygame.event.get():  # for loop going through every possible "event" in pygame

        if event.type == QUIT:  # testing to see if the event is "QUIT", meaning pressing the quit button
            game_is_running = False

    screen.fill((250, 250, 250))  # fills screen with white. the three numbers are rgb (red, green, blue) values
    pygame.display.flip()  # important
    pygame.display.update()  # also important

pygame.quit()  # quits PyGame once while loop is done
