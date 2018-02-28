import pygame
import random
 
# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0, 255, 0)

# Set the width and height of each snake segment
segment_width = 10
segment_height = 10
# Margin between each segment
segment_margin = 3
 
# Set initial speed
red_x_change = segment_width + segment_margin
red_y_change = 0

blue_x_change = segment_width + segment_margin 
blue_y_change = 0

red_score = 0
blue_score = 0

red_left = False
red_right = True
red_up = False
red_down = False

blue_left = False
blue_right = True
blue_up = False
blue_down = False

game_state = 0
#timer
timer = 0
seconds = 0

s_counter = True

alive = False
 
class RedSegment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super(RedSegment, self).__init__()
 
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(RED)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BlueSegment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super(BlueSegment, self).__init__()
 
        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Selector(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Selector, self).__init__()

        self.image = pygame.Surface([10,10])
        self.image.fill((255,255,255))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 1280x700 sized screen
screen = pygame.display.set_mode([1280, 700])

background = pygame.transform.scale(pygame.image.load('images/Snake.jpg'), (1280,700))


font = pygame.font.SysFont(False, 32)

def draw_text(display_text, font, surface, x_pos, y_pos, (r,g,b)):
    text_display = font.render(display_text, 1, (r,g,b))
    screen.blit(text_display, (x_pos, y_pos))
 
# Set the title of the window
pygame.display.set_caption('Snake Game')

pygame.mixer.init()
pygame.mixer.music.load('sound/Automation.mp3')
 
allspriteslist = pygame.sprite.Group()

blue_seg = pygame.sprite.Group()
red_seg = pygame.sprite.Group()

# Create an initial snake/Not Head group
red_snake_segments = []
for i in range(5): #250, 30
    rx = 150 - (segment_width + segment_margin) * i
    ry = 100
    segment = RedSegment(rx, ry)
    red_snake_segments.append(segment)
    allspriteslist.add(segment)
    red_seg.add(segment)

blue_snake_segments = []
for i in range(5): #250, 30
    bx = 150 - (segment_width + segment_margin) * i
    by = 670
    segment = BlueSegment(bx, by)
    blue_snake_segments.append(segment)
    allspriteslist.add(segment)
    blue_seg.add(segment)
 
clock = pygame.time.Clock()
done = False

music = True
music_num = 0


selector = Selector(150,197)

while not done:
    
    if game_state ==0:
        allspriteslist.empty()
        for i in range(25):
            x = 750 
            y = 650 - (segment_height + segment_margin) * i
            special_segment = BlueSegment(x,y)
            allspriteslist.add(special_segment)

        for i in range(25):
            x = 1000 - (segment_height + segment_margin) *i
            y = 250
            special_segment = RedSegment(x,y)
            allspriteslist.add(special_segment)
        alive = False
        blue_score = 0
        red_score = 0
        seconds = 0
        if music:
            pygame.mixer.music.play(-1)
            music = False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selector.rect.y == 467:
                        selector.rect.y = 267
                    elif selector.rect.y == 267:
                        selector.rect.y = 197
                    else:
                        selector.rect.y = 467
                if event.key == pygame.K_DOWN:
                    if selector.rect.y == 197:
                        selector.rect.y = 267
                    elif selector.rect.y == 267:
                        selector.rect.y = 467
                    else:
                        selector.rect.y = 197
                if event.key == pygame.K_RETURN and selector.rect.y == 197:
                    game_state =2
                    allspriteslist.empty()
                    music = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('sound/actionmusic.wav')

                if event.key == pygame.K_RETURN and selector.rect.y == 267:
                    game_state = 1
                    allspriteslist.empty()

                if event.key == pygame.K_RETURN and selector.rect.y == 467:
                    done=True

        
        screen.fill((0,0,0))
        screen.blit(selector.image, (selector.rect.x, selector.rect.y))
        draw_text('Play', font, screen, 175, 195, (255,255,255))
        draw_text('How to Play', font, screen, 175, 265, (255,255,255))
        draw_text('Quit', font, screen, 175, 465, (255,255,255))
        font = pygame.font.SysFont(False, 64)
        draw_text('THE SNAKE GAME', font, screen, 700, 50, (255,255,255))
        font = pygame.font.SysFont(False, 32)
        allspriteslist.draw(screen)

    if game_state == 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state = 0

        screen.fill((0,0,0))
        font = pygame.font.SysFont(False, 64)
        draw_text('HOW TO PLAY:', font, screen, 450, 100, (255,255,255))
        font = pygame.font.SysFont(False, 32)
        draw_text('Red Controls: WASD', font, screen, 300, 200, (255,255,255))
        draw_text('Blue Controls: ARROW KEYS', font, screen, 650, 200, (255,255,255))
        draw_text('Do not run into yourself, your opponent, or the walls.', font,screen,350, 300, (255,255,255))
        draw_text('Press ESC to exit', font, screen, 500, 600, (255,255,255))
    if game_state ==2:

        if seconds >=3:
            if music:
                pygame.mixer.music.play(-1)
                music = False
        
        if seconds == 0:
            sc = ((0,0,0))
            tc = ((255,255,255))
            
        timer += clock.get_time()
        
        if timer >=1000:
            seconds +=1
            timer =0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
     
            # Set the speed based on the key pressed
            # We want the speed to be enough that we move a full
            # segment, plus the margin.
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_a and not red_right:
                    red_x_change = (segment_width + segment_margin) * -1
                    red_y_change = 0
                    red_left = True
                    red_right = False
                    red_up = False
                    red_down = False
                elif event.key == pygame.K_d and not red_left:
                    red_x_change = (segment_width + segment_margin)
                    red_y_change = 0
                    red_left = False
                    red_right = True
                    red_up = False
                    red_down = False
                elif event.key == pygame.K_w and not red_down:
                    red_x_change = 0
                    red_y_change = (segment_height + segment_margin) * -1
                    red_left = False
                    red_right = False
                    red_up = True
                    red_down = False
                elif event.key == pygame.K_s and not red_up:
                    red_x_change = 0
                    red_y_change = (segment_height + segment_margin)
                    red_left = False
                    red_right = False
                    red_up = False
                    red_down = True
                    
                if event.key == pygame.K_LEFT and not blue_right:
                    blue_x_change = (segment_width + segment_margin) * -1
                    blue_y_change = 0
                    blue_left = True
                    blue_right = False
                    blue_up = False
                    blue_down = False
                elif event.key == pygame.K_RIGHT and not blue_left:
                    blue_x_change = (segment_width + segment_margin)
                    blue_y_change = 0
                    blue_left = False
                    blue_right = True
                    blue_up = False
                    blue_down = False
                elif event.key == pygame.K_UP and not blue_down:
                    blue_x_change = 0
                    blue_y_change = (segment_height + segment_margin) * -1
                    blue_left = False
                    blue_right = False
                    blue_up = True
                    blue_down = False
                elif event.key == pygame.K_DOWN and not blue_up:
                    blue_x_change = 0
                    blue_y_change = (segment_height + segment_margin)
                    blue_left = False
                    blue_right = False
                    blue_up = False
                    blue_down = True

                if event.key==pygame.K_RETURN:
                    blue_score = 0
                    red_score = 0

                if event.key == pygame.K_ESCAPE:
                    game_state = 0
                    pygame.mixer.music.load('sound/Automation.mp3')
                    music = True


     
        # Get rid of last segment of the snake
        # .pop() command removes last item in list
        '''if alive:
            red_old_segment = red_snake_segments.pop()
            allspriteslist.remove(red_old_segment)
            blue_old_segment = blue_snake_segments.pop()
            allspriteslist.remove(blue_old_segment)'''
         
        
        if alive:
            s_counter = True
            rx = red_snake_segments[0].rect.x + red_x_change
            ry = red_snake_segments[0].rect.y + red_y_change
            segment = RedSegment(rx, ry)
         
            # Insert new segment into the list
            red_snake_segments.insert(0, segment)
            allspriteslist.add(segment)
            red_head = red_snake_segments[0]

            # Figure out where new segment will be
            bx = blue_snake_segments[0].rect.x + blue_x_change
            by = blue_snake_segments[0].rect.y + blue_y_change
            segment = BlueSegment(bx, by)
         
            # Insert new segment into the list
            blue_snake_segments.insert(0, segment)
            allspriteslist.add(segment)
            blue_head = blue_snake_segments[0]

            for segment in range(1, len(red_snake_segments)):
                if red_snake_segments[segment].rect.x == red_head.rect.x and red_snake_segments[segment].rect.y == red_head.rect.y:
                    alive = False
                    blue_score += 1
            
                if blue_snake_segments[segment].rect.x == blue_head.rect.x and blue_snake_segments[segment].rect.y == blue_head.rect.y:
                    alive = False
                    red_score += 1
            
                if red_snake_segments[segment].rect.x == blue_head.rect.x and red_snake_segments[segment].rect.y == blue_head.rect.y:
                    alive = False
                    red_score += 1
            
                if blue_snake_segments[segment].rect.x == red_head.rect.x and blue_snake_segments[segment].rect.y == red_head.rect.y:
                    alive = False
                    blue_score += 1

                if blue_head.rect.x == red_head.rect.x and blue_head.rect.y == red_head.rect.y:
                    sc = ((0,0,0))
                    tc = ((255,255,255))

            if blue_head.rect.x <=0:
                alive = False
                red_score +=1
            if blue_head.rect.x >=1280:
                alive = False
                red_score +=1
            if blue_head.rect.y <=0:
                alive = False
                red_score +=1
            if blue_head.rect.y >=700:
                alive = False
                red_score +=1

            if red_head.rect.x <=0:
                alive = False
                blue_score +=1
            if red_head.rect.x >=1280:
                alive = False
                blue_score +=1
            if red_head.rect.y <=0:
                alive = False
                blue_score +=1
            if red_head.rect.y >=700:
                alive = False
                blue_score +=1
        else:
            blue_x_change = 0
            blue_y_change = 0
            red_x_change = 0
            red_y_change = 0
            if s_counter:
                seconds = 0
                timer = 0
                s_counter = False
                
            if seconds > 2:
                red_left = False
                red_right = True
                red_up = False
                red_down = False

                blue_left = False
                blue_right = True
                blue_up = False
                blue_down = False
                alive = True
                allspriteslist.empty()
                blue_x_change = (segment_width + segment_margin)
                blue_y_change = 0
                red_x_change = (segment_width + segment_margin)
                red_y_change = 0
                red_snake_segments = []
                for i in range(5): #250, 30
                    rx = 150 - (segment_width + segment_margin) * i
                    ry = 100
                    segment = RedSegment(rx, ry)
                    red_snake_segments.append(segment)
                    allspriteslist.add(segment)

                blue_snake_segments = []
                for i in range(5): #250, 30
                    bx = 150 - (segment_width + segment_margin) * i
                    by = 659
                    segment = BlueSegment(bx, by)
                    blue_snake_segments.append(segment)
                    allspriteslist.add(segment)

        # -- Draw everything
        # Clear screen
        screen.fill(sc)

        allspriteslist.draw(screen)

        draw_text('Red Score: '+str(red_score), font, screen, 50, 10, tc)
        draw_text('Blue Score: '+str(blue_score), font, screen, 1080, 10, tc)

        if seconds ==0:
            draw_text('3', font, screen, 640, 350, tc)
            
        if seconds ==1:
            draw_text('2', font, screen, 640, 350, tc)
            
        if seconds == 2:
            draw_text('1', font, screen, 640, 350, tc)

    # Flip screen
    pygame.display.flip()
 
    # Pause
    clock.tick(30)
 
pygame.quit()

