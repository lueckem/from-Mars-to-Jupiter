import pygame
import random

pygame.init()

#constants
display_height = 700
display_width = 600
ship_width = 60
ship_height = 80

num_small_asteroids = 10
small_asteroid_width = 30
small_asteroid_height = 30

num_medium_asteroids = 5
medium_asteroid_width = 70
medium_asteroid_height = 70

num_large_asteroids = 2
large_asteroid_width = 100
large_asteroid_height = 100

black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Working Title')
clock = pygame.time.Clock()

#load graphics
shipImg = pygame.image.load('ship.png')
asteroid_small_Img = pygame.image.load('asteroid_small.png')
asteroid_medium_Img = pygame.image.load('asteroid_medium.png')
asteroid_large_Img = pygame.image.load('asteroid_large.png')

#functions
def draw_image(image, x, y):
    gameDisplay.blit(image, (x,y))

def message_display(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf, TextRect)
    
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def crashed(pos1,pos2, width_1, height_1, width_2, height_2):
    if pos2[0] >= pos1[0] - width_2 and pos2[0] <= pos1[0] + width_1:
        if pos2[1] >= pos1[1] - height_2 and pos2[1] <= pos1[1] + height_1:
            return True
    else:
        return False

def score_display(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(score), True, white)
    gameDisplay.blit(text,(0,0))

#classes
class Asteroid:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height



#Game Loop
def main():

    #variables
    x = (display_width * 0.45)
    y = (display_height * 0.9)
    score = 0
    fallspeed = 2

    timer = 3
    dtime = 0

    asteroids = list()
    

    #initialize Asteroids
    for i in range(0,num_small_asteroids):
        asteroids.append(Asteroid(0,0,small_asteroid_width,small_asteroid_height))
    for i in range(0,num_medium_asteroids):
        asteroids.append(Asteroid(0,0,medium_asteroid_width,medium_asteroid_height))
    for i in range(0,num_large_asteroids):
        asteroids.append(Asteroid(0,0,large_asteroid_width,large_asteroid_height))

    
    for i in range(0,num_small_asteroids + num_medium_asteroids + num_large_asteroids):
        asteroid_crash = True
        
        while asteroid_crash == True:
            num_crashes = 0
            x_asteroid = random.randint(-small_asteroid_width/2, display_width - (small_asteroid_width/2))
            y_asteroid = random.randint(-2000, -500)

            if i <= num_small_asteroids:                            
                for asteroid in asteroids:
                    if crashed((asteroid.x,asteroid.y), (x_asteroid,y_asteroid), asteroid.width, asteroid.height, small_asteroid_width, small_asteroid_height) == True:
                        num_crashes += 1
            elif i <= num_medium_asteroids:
                for asteroid in asteroids:
                    if crashed((asteroid.x,asteroid.y), (x_asteroid,y_asteroid), asteroid.width, asteroid.height, medium_asteroid_width, medium_asteroid_height) == True:
                        num_crashes += 1
            else:
                for asteroid in asteroids:
                    if crashed((asteroid.x,asteroid.y), (x_asteroid,y_asteroid), asteroid.width, asteroid.height, large_asteroid_width, large_asteroid_height) == True:
                        num_crashes += 1

            if num_crashes == 0:
                asteroids[i].x = x_asteroid
                asteroids[i].y = y_asteroid
                asteroid_crash = False
            

    exit_game = False

    while exit_game == False:
        gameDisplay.fill(black)

        #Catch Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 10
        if pressed[pygame.K_RIGHT]: x += 10

 
        #game logic
        #handle timer
        if timer > 0:
            if x < 0 or x > (display_width - ship_width):
                timer = round(timer - dtime, 2)
                message_display('Come back! ' + str(timer), display_width/2, display_height/2)
        else:
            message_display("You left your route!",display_width/2, display_height/2)
            message_display("Final Score: " + str(score) ,display_width/2, display_height/2 + 60)
            #Final Score: " + str(score))
        
            pygame.display.update()
            pygame.time.delay(2000)
            main()
            
        #update asteroids position and check for crashes
        for asteroid in asteroids:
            asteroid.y = asteroid.y + fallspeed
            if crashed((x,y), (asteroid.x,asteroid.y), ship_width, ship_height, asteroid.width, asteroid.height) == True:
                message_display("You crashed!",display_width/2, display_height/2)
                message_display("Final Score: " + str(score) ,display_width/2, display_height/2 + 60)
                pygame.display.update()
                pygame.time.delay(2000)
                main()

            
            if asteroid.y >= display_height + 100:
                asteroid.y = -800
                score += 1
                if score % 20 == 0:
                    fallspeed += 1
                
                asteroid_crash = True
                while asteroid_crash == True:
                    num_crashes = 0
                    x_asteroid = random.randint(-small_asteroid_width/2, display_width - (small_asteroid_width/2))                        
                    for asteroid_2 in asteroids:
                        if crashed((asteroid_2.x, asteroid_2.y), (x_asteroid, asteroid.y), asteroid_2.width, asteroid_2.height, asteroid.width, asteroid.height) == True:
                            num_crashes += 1

                    if num_crashes <= 1:
                        asteroid.x = x_asteroid
                        asteroid_crash = False
                        

        #draw surface
        draw_image(shipImg, x, y)

        for asteroid in asteroids:
            if asteroid.width == small_asteroid_width:
                draw_image(asteroid_small_Img, asteroid.x, asteroid.y)
            elif asteroid.width == medium_asteroid_width:
                draw_image(asteroid_medium_Img, asteroid.x, asteroid.y)
            else:
                draw_image(asteroid_large_Img, asteroid.x, asteroid.y)
        
        score_display(score)        
        pygame.display.update()
        dtime = clock.tick(60) / 1000


#Main Sequence
main()
pygame.quit()
quit()
