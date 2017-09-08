import pygame

pygame.init()

#variables
display_height = 800
display_width = 600
ship_width = 60
ship_height = 80

black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Working Title')
clock = pygame.time.Clock()

#load graphics
shipImg = pygame.image.load('ship.png')
asteroid_small_Img = pygame.image.load('asteroid_small.png')
asteroid_medium_Img = pygame.image.load('asteroid_medium.png')


#functions
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


#Game Loop
def main():
    x = (display_width * 0.45)
    y = (display_height * 0.9)

    timer = 3
    dtime = 0

    

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
                
        pygame.display.update()
        dtime = clock.tick(60) / 1000


#Main Sequence
main()
pygame.quit()
quit()
