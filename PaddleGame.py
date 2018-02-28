#import statments
import pygame
import random
import math
import sys
from pygame.locals import *

#starting python and text display
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Sound/pong_hit.wav')
screen = pygame.display.set_mode((640, 700))
font = pygame.font.SysFont(None, 64)

def draw_text(display_string, font, surface, x_pos, y_pos, (r,g,b)):
    text_display = font.render(display_string, 10, (r, g, b))
    surface.blit(text_display, (x_pos, y_pos))

#clocks and timing 1
main_clock = pygame.time.Clock()
pygame.display.set_caption('Paddle Game')

#seconds
timer = 0.0
seconds = 0
minutes = 0

#players and ball
pl = 100
player1 = pygame.Rect(10, 200, 10, pl)
player2 = pygame.Rect(620, 200, 10, pl)
player1_down = False
player2_down = False
player1_up = False
player2_up = False
ball_can_move = False
speed = [-4, 4]
player1_score = 0
player2_score = 0
x_pos = 320
y_pos = 100
middle_line = pygame.Rect(318, 0, 5, 700)
p1_y_axis = 200
p2_y_axis = 200
player_speed = 5
paddle_speed = 2
practice = 0
practice_buffer = pygame.Rect(630, 0, 10, 700)

#draw player function
def draw_paddle1():
    pygame.draw.rect(screen, (0,0,0), paddle1)
    
def draw_paddle2():
    pygame.draw.rect(screen, (0,0,0), paddle2)
    
def draw_p1():
    pygame.draw.rect(screen, (0, 0, 0), player1)

def draw_p2():
    pygame.draw.rect(screen, (0,0,0), player2)

def middle():
    pygame.draw.rect(screen, (0,0,0), middle_line)

def draw_screen():
    screen.fill((255, 255, 255))

def practice_b():
    pygame.draw.rect(screen, (0,0,0), practice_buffer)

#game loop
while True:
    
    player_speed = 5
    
    timer += main_clock.get_time()
    
    if timer >= 1000:
        seconds += 1
        timer = 0
        
    if practice==0:
        if timer == 0:
            pl -=1
        if seconds%20==0 and timer ==0:
            if speed[0]>0:
                speed[0]+=1
            else:
                speed[0]-=1
                
            if speed[1]>0:
                speed[1]+=1
            else:
                speed[1]-=1
            
        
    player1 = pygame.Rect(10, p1_y_axis, 10, pl)
    player2 = pygame.Rect(620, p2_y_axis, 10, pl)

    #events and exiting
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                player1_up = True
                player1_down = False
            if event.key == K_s:
                player1_down = True
                player1_up = False
            if event.key == K_UP:
                player2_up = True
                player2_down = False
            if event.key == K_DOWN:
                player2_down = True
                player2_up = False
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_s:
                player1_down = False
            if event.key == K_w:
                player1_up = False
            if event.key == K_DOWN:
                player2_down = False
            if event.key == K_UP:
                player2_up = False
            if event.key == K_RETURN:
                ball_can_move = False
                pl = 100
                player1_score = 0
                player2_score = 0
            if event.key == K_1:
                player1_score +=1
                seconds += 60
            if event.key == K_0:
                player2_score +=1
            if event.key == K_BACKSPACE:
                seconds = 0
                practice +=1
                if practice>1:
                    practice = 0
                ball_can_move = False
                player1_score = 0
                player2_score = 0

    #player movement
    if player1_up:
        p1_y_axis -= player_speed
    if player1_down:
        p1_y_axis += player_speed
    if player2_up:
        p2_y_axis -= player_speed
    if player2_down:
        p2_y_axis += player_speed

    #player boundaries

    if p1_y_axis <=0:
        p1_y_axis = 1
    if p1_y_axis >=650:
        p1_y_axis = 649
    if p2_y_axis <=0:
        p2_y_axis = 1
    if p2_y_axis >=650:
        p2_y_axis = 649

    #ball can move

    if seconds >=2:
        ball_can_move = True
        
    #ball movement
    if ball_can_move:
        
        if pl <= 20:
            pl = 21
        x_pos += speed[0]
        y_pos += speed[1]

        if ball.y <=20:
            pygame.mixer.music.load('Sound/pong_hit.wav')
            pygame.mixer.music.play()
            y_pos += 10
            speed[1] = -speed[1]
        if ball.y >= 680:
            pygame.mixer.music.load('Sound/pong_hit.wav')
            pygame.mixer.music.play()
            y_pos -= 10
            speed[1] = -speed[1]

        #score change
        if ball.x <=0:
            seconds = 0
            timer = 0
            pygame.mixer.music.load('Sound/pong_death.wav')
            pygame.mixer.music.play()
            blue = 100
            red = 100
            ball_can_move = False
            if practice == 0:
                player2_score += 1
        if ball.x >=640:
            seconds = 0
            timer = 0
            pygame.mixer.music.load('Sound/pong_death.wav')
            pygame.mixer.music.play()
            color_change = 5
            red = 100
            blue = 100
            ball_can_move = False
            if practice == 0:
                player1_score +=1

        #player collision
        if ball.colliderect(player1):
            pygame.mixer.music.load('Sound/pong_hit.wav')
            pygame.mixer.music.play()
            x_pos +=10
            speed[0] = -speed[0]
        
        if practice ==0:
            if ball.colliderect(player2):
                pygame.mixer.music.load('Sound/pong_hit.wav')
                pygame.mixer.music.play()
                x_pos -=10
                speed[0] = -speed[0]

    else:
        speed[0] = -4
        speed[1] = 4
        x_pos = 320
        y_pos = 250
        pl = 100
        player_speed = 5

    #blitting
    draw_screen()

    if practice == 1:
        
        if ball.colliderect(practice_buffer):
            pygame.mixer.music.load('Sound/pong_hit.wav')
            pygame.mixer.music.play()
            speed[0] = -speed[0]
            x_pos -= 10
    
    draw_p1()
    
    if practice==0:
        draw_p2()
        middle()
        draw_text(str(player1_score), font, screen, 160, 20, (0,0,0))
        draw_text(str(player2_score), font, screen, 480, 20, (0,0,0))

    else:
        practice_b()
    
    ball = pygame.draw.circle(screen, (0,0,0), (x_pos, y_pos), 7, 0)
    
    pygame.display.flip()
    
    #updating display changes
    pygame.display.update()

    main_clock.tick(60)
    
