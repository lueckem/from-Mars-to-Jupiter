import pygame
import random

pygame.init()

#constants
display_height = 800
display_width = 600
ship_width = 60
ship_height = 80
fallspeed = 50

num_small_asteroids = 10
small_asteroid_width = 30
small_asteroid_height = 30
small_asteroids = list()

num_medium_asteroids = 2
medium_asteroid_width = 70
medium_asteroid_width = 70
medium_asteroids = list()

black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Working Title')
clock = pygame.time.Clock()

#load graphics
shipImg = pygame.image.load('ship.png')
asteroid_small_Img = pygame.image.load('asteroid_small.png')
asteroid_medium_Img = pygame.image.load('asteroid_medium.png')



def draw_image(image, x, y):
    gameDisplay.blit(image, (x,y))

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def crashed(pos1,pos2, width_1, height_1, width_2, height_2):
    if pos2[0] >= pos1[0] - width_2 and pos2[0] <= pos1[0] + width_1:
        if pos2[1] >= pos1[1] - height_2 and pos2[1] <= pos1[1] + height_1:
            return True
    else:
        return False
                    


#Game Loop
def main():

    #variables
    x = (display_width * 0.45)
    y = (display_height * 0.9)

    timer = 3
    dtime = 0


    #initialize Asteroids
    x_asteroid = display_width - (small_asteroid_width/2)
    y_asteroid = -500
        
    for i in range(0,num_small_asteroids):
        asteroid_crash = True
        
        while asteroid_crash == True:
            num_crashes = 0
            x_asteroid = random.randint(-small_asteroid_width/2, display_width - (small_asteroid_width/2))
            y_asteroid = random.randint(-2000, -500)
                                        
            for asteroid in small_asteroids:
                if crashed(asteroid, (x_asteroid,y_asteroid), small_asteroid_width, small_asteroid_height, small_asteroid_width, small_asteroid_height) == True:
                    num_crashes += 1

            if num_crashes == 0:
                small_asteroids.append((x_asteroid, y_asteroid))
                asteroid_crash = False
            
        #for i in range(0,num_medium_asteroids):
        #medium_asteroids.append((0,0))


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
                message_display('Come back! ' + str(timer))
        else:
            message_display("You left your route!")
            pygame.time.delay(2000)
            main()

        
        #draw surface
        draw_image(shipImg, x, y)
##        for asteroid in small_asteroids:
##            y_new = asteroid[1] + fallspeed
##            print (small_asteroids)
##            draw_image(asteroid_small_Img, asteroid[0], asteroid[1])
                
        pygame.display.update()
        dtime = clock.tick(60) / 1000


#Main Sequence
main()
pygame.quit()
quit()
