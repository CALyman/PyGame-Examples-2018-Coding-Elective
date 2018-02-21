import pygame
import random
from pygame.locals import *  

pygame.init()
pygame.font.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600)) 

pygame.display.set_caption("Coins Game") 

clock = pygame.time.Clock()

def draw_text(display_text, font, screen, x_pos, y_pos, r,g,b):
    text_display = font.render(display_text, 1, (r,g,b))
    screen.blit(text_display, (x_pos, y_pos))

small_font = pygame.font.SysFont('americantypewriter', 18)
font = pygame.font.SysFont('americantypewriter', 24)
big_font = pygame.font.SysFont('americantypewriter', 36)

coin_collect = pygame.mixer.Sound('sound/sfx_coin_single2 copy.wav')
countdown = pygame.mixer.Sound('sound/sfx_sounds_Blip11 copy.wav')
speed_power_up = pygame.mixer.Sound('sound/sfx_sounds_powerup11 copy.wav')
freeze_power_up = pygame.mixer.Sound('sound/sfx_sound_neutral3 copy.wav')
time_bonus_power_up = pygame.mixer.Sound('sound/sfx_sounds_pause7_in copy.wav')

mushrooms = ["images/red_mushroom.png", "images/blue_mushroom.png", "images/green_mushroom.png", "images/yellow_mushroom.png", "images/purple_mushroom.png", "images/freeze_mushroom.png", "images/time_bonus_mushroom.png"]
n = 0
speed_power = False
freeze_power = False
time_bonus_power = False

mushroom = pygame.image.load("images/red_mushroom.png") #loading the mushroom image from the images folder
coin = pygame.image.load("images/coin.png")
speed_coin = pygame.image.load("images/speed_coin.png")
time_bonus_coin = pygame.image.load("images/time_bonus_coin.png")
freeze_coin = pygame.image.load("images/freeze_coin.png")
time_bonus_coin = pygame.image.load("images/time_bonus_coin.png")
pause_button = pygame.image.load("images/pause.png")
points = 0
speed = 10

mushroom_x = 350
mushroom_y = 250
coin_x = random.randint(50,700)
coin_y =  random.randint(50,500)

speed_coin_x = random.randint(50, 700)
speed_coin_y = random.randint(50, 500)
freeze_coin_x = random.randint(50, 700)
freeze_coin_y = random.randint(50, 500)
time_bonus_coin_x = random.randint(50, 700)
time_bonus_coin_y = random.randint(50, 500)
random_time_speed_start = random.randint(20, 40)
random_time_speed_stop = random_time_speed_start -5
random_time_freeze_start = random.randint(20, 40)
random_time_freeze_stop = random_time_freeze_start -5
random_time_time_bonus_start = random.randint(20, 40)
random_time_time_bonus_stop = random_time_time_bonus_start -5


timer = 0
seconds = 45
time_display = "0:45"


delay_timer = 0
speed_timer = 0
freeze_timer = 0
time_bonus_timer = 0
highscore = 61

pygame.key.set_repeat(1,1)

r = 255

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
                if event.key == K_d or event.key == K_RIGHT:  # checking to see if the "d" key is being pressed
                    mushroom_x += speed  # add 5 to the variable "x", which will move the mushroom image 5 units to the right 
                if event.key == K_a or event.key == K_LEFT:  # checking to see if the "a" key is being pressed
                    mushroom_x -= speed  # subtract 5 to the variable "x", which will move the mushroom image 5 units to the left
                if event.key == K_w or event.key == K_UP:  # checking to see if the "w" key is being pressed
                    mushroom_y -= speed  # subtract 5 from variable "y", which will move the mushroom image up 5 units
                if event.key == K_s or event.key == K_DOWN:  # checking to see if the "s" key is being pressed
                    mushroom_y += speed  # adding 5 to variable y, which will make the mushroom move down 5 units
            if event.key == K_SPACE:
                if seconds == 0:
                    seconds = 45
                    timer = 0
                    delay_timer = 0
                    points = 0
                    time_display = "0:{}".format(seconds)
                    random_time_speed_start = random.randint(20, 40)
                    random_time_speed_stop = random_time_speed_start -5
                    random_time_freeze_start = random.randint(20, 40)
                    random_time_freeze_stop = random_time_freeze_start -5
                    random_time_time_bonus_start = random.randint(20, 40)
                    random_time_time_bonus_stop = random_time_time_bonus_start -5
                    speed_coin_x = random.randint(50, 700)
                    speed_coin_y = random.randint(50, 500)
                    freeze_coin_x = random.randint(50, 700)
                    freeze_coin_y = random.randint(50, 500)
                    time_bonus_coin_x = random.randint(50, 700)
                    time_bonus_coin_y = random.randint(50, 500)


    if mushroom_x < 0:
        mushroom_x = 0
    if mushroom_x > 700:
        mushroom_x = 700
    if mushroom_y <0:
        mushroom_y = 0
    if mushroom_y > 500:
        mushroom_y = 500

    if freeze_power:
    
        seconds = current_seconds
        mushroom = pygame.image.load(mushrooms[5])
        freeze_timer += clock.get_time()
        if freeze_timer >=9000:
            freeze_power = False
            freeze_timer = 0
            mushroom = pygame.image.load(mushrooms[0])

    else:
        current_seconds = seconds

    if time_bonus_power:

        mushroom = pygame.image.load(mushrooms[6])
        time_bonus_timer += clock.get_time()
        if time_bonus_timer >=5000:
            time_bonus_power = False
            time_bonus_timer = 0
            mushroom = pygame.image.load(mushrooms[0])

    else:
        r = 255

    if speed_power:
        if n == 5:
            n = 0
        mushroom = pygame.image.load(mushrooms[n])
        n +=1
        speed =  30

        speed_timer += clock.get_time()
        if speed_timer >=9000:
            speed_power = False
            speed_timer = 0
            mushroom = pygame.image.load(mushrooms[0])
            speed = 10


    screen.fill((250, 250, 250))

    if seconds != 0:

        if mushroom_y+100>coin_y and mushroom_y - 64 < coin_y:

            if mushroom_x > coin_x and mushroom_x < coin_x + 100 or mushroom_x+100 > coin_x and mushroom_x + 100 < coin_x+100:
                coin_x = random.randint(50,700)
                coin_y =  random.randint(50,500)
                points += 1
                coin_collect.play()

        if seconds < random_time_speed_start and seconds > random_time_speed_stop:

            if not speed_power:
                screen.blit(speed_coin, (speed_coin_x, speed_coin_y))
            else:
                speed_coin_x = -100
                speed_coin_y = -100
                
            if mushroom_y+100>speed_coin_y and mushroom_y - 64 < speed_coin_y:

                if mushroom_x > speed_coin_x and mushroom_x < speed_coin_x + 100 or mushroom_x+100 > speed_coin_x and mushroom_x + 100 < speed_coin_x+100:
                    speed_power_up.play()
                    speed_power = True

        if seconds < random_time_freeze_start and seconds > random_time_freeze_stop:

            if not freeze_power:
                screen.blit(freeze_coin, (freeze_coin_x, freeze_coin_y))
            else:
                freeze_coin_x = -100
                freeze_coin_y = -100
            
            if mushroom_y+100> freeze_coin_y and mushroom_y - 64 < freeze_coin_y:

                if mushroom_x > freeze_coin_x and mushroom_x < freeze_coin_x + 100 or mushroom_x+100 > freeze_coin_x and mushroom_x + 100 < freeze_coin_x+100:
                    freeze_power_up.play()
                    freeze_power = True

        if seconds < random_time_time_bonus_start and seconds > random_time_time_bonus_stop:

            if not time_bonus_power:
                screen.blit(time_bonus_coin, (time_bonus_coin_x, time_bonus_coin_y))
            else:
                time_bonus_coin_x = -100
                time_bonus_coin_y = -100
            
            if mushroom_y+100> time_bonus_coin_y and mushroom_y - 64 < time_bonus_coin_y:

                if mushroom_x > time_bonus_coin_x and mushroom_x < time_bonus_coin_x + 100 or mushroom_x+100 > time_bonus_coin_x and mushroom_x + 100 < time_bonus_coin_x+100:
                    time_bonus_power_up.play()
                    time_bonus_power = True
                    seconds +=5
                    timer = 0
                
    
    if seconds == 0:
        delay_timer += clock.get_time()
        if delay_timer >= 1500:
            delay_timer = 1500
            draw_text('Press "Space" to continue', small_font, screen, 295, 70, 0, 0, 0)
            
    draw_text(str(time_display), big_font, screen, 365, 25, 0, 0, 0)
    if seconds < 11:
        if timer == 0 and seconds != 0:
            countdown.play()
        if int(seconds)%2 == 0:
            draw_text(str(time_display), big_font, screen, 365, 25, 255, 0, 0)
    if freeze_power:
        draw_text(str(time_display), big_font, screen, 365, 25, 0, 215, 255)

    if time_bonus_power:
        draw_text(str(time_display), big_font, screen, 365, 25, r, 0, 0)
        r -= 5
        if r < 0:
            r = 0

    if points > highscore:
        highscore = points
            
    draw_text("Points: " + str(points), font, screen, 50, 50, 0, 0, 0)
    draw_text("Highscore: "+str(highscore), font, screen, 50, 25, 0, 0, 0)
    screen.blit(mushroom, (mushroom_x, mushroom_y)) #blitting (basically putting the image on) the screen at x and y positions
    screen.blit(coin, (coin_x, coin_y))
    screen.blit(pause_button, (700, 25))
    pygame.display.flip()  
    pygame.display.update()  

pygame.quit()  
