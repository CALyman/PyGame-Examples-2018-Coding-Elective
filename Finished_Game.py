import pygame
import random
from pygame.locals import *  

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600)) 

pygame.display.set_caption("Coins Game") 

clock = pygame.time.Clock()

def draw_text(display_text, font, screen, x_pos, y_pos, r,g,b):
    text_display = font.render(display_text, 1, (r,g,b))
    screen.blit(text_display, (x_pos, y_pos))

small_font = pygame.font.SysFont('americantypewriter', 18)
font = pygame.font.SysFont('americantypewriter', 24)
big_font = pygame.font.SysFont('americantypewriter', 36)

mushroom1 = pygame.image.load("images/red_mushroom.png") #loading the mushroom image from the images folder
coin = pygame.image.load("images/coin.png")
points = 0

mushroom_x = 350
mushroom_y = 250
coin_x = random.randint(50,700)
coin_y =  random.randint(50,500)

timer = 0
seconds = 30
time_display = "0:30"

delay_timer = 0
high_score = 37

pygame.key.set_repeat(1,1)

game_is_running = True  

while game_is_running:  

    clock.tick(600)
    if seconds !=0:
        timer += clock.get_time()
        if timer >= 1000:
            seconds -= 1
            timer =0
            if seconds <10:
                time_display = "0:0{}".format(seconds)
            else:
                time_display = "0:{}".format(seconds)

    for event in pygame.event.get():  

        if event.type == QUIT:  
            game_is_running = False

        
        if event.type == KEYDOWN:  # checking to see if a key is being pressed
            if seconds != 0:
                if event.key == K_d:  # checking to see if the "d" key is being pressed
                    mushroom_x +=10  # add 5 to the variable "x", which will move the mushroom image 5 units to the right 
                if event.key == K_a:  # checking to see if the "a" key is being pressed
                    mushroom_x -=10  # subtract 5 to the variable "x", which will move the mushroom image 5 units to the left
                if event.key == K_w:  # checking to see if the "w" key is being pressed
                    mushroom_y -=10  # subtract 5 from variable "y", which will move the mushroom image up 5 units
                if event.key == K_s:  # checking to see if the "s" key is being pressed
                    mushroom_y +=10  # adding 5 to variable y, which will make the mushroom move down 5 units
            if event.key == K_SPACE:
                if seconds == 0:
                    seconds = 30
                    timer = 0
                    delay_timer = 0
                    points = 0
                    time_display = "0:{}".format(seconds)

    if seconds != 0:

        if mushroom_y+100>coin_y and mushroom_y - 100 < coin_y:

            if mushroom_x > coin_x and mushroom_x < coin_x + 100 or mushroom_x+100 > coin_x and mushroom_x + 100 < coin_x+100:
                coin_x = random.randint(50,700)
                coin_y =  random.randint(50,500)
                points += 1
            
    screen.fill((250, 250, 250))
    if seconds == 0:
        delay_timer += clock.get_time()
        if delay_timer >= 1500:
            delay_timer = 1500
            draw_text('Press "Space" to continue', small_font, screen, 295, 70, 0, 0, 0)
    draw_text(str(time_display), big_font, screen, 365, 25, 0, 0, 0)
    draw_text("Points: " + str(points), font, screen, 50, 50, 0, 0, 0)
    screen.blit(mushroom1, (mushroom_x, mushroom_y)) #blitting (basically putting the image on) the screen at x and y positions
    screen.blit(coin, (coin_x, coin_y))
    pygame.display.flip()  
    pygame.display.update()  

pygame.quit()  
