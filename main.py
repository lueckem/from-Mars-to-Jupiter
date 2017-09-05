import pygame

#variables
display_height = 800
display_width = 600
ship_width = 60
ship_height = 80

black = (0,0,0)
white = (255,255,255)

x = (display_width * 0.45)
y = (display_height * 0.9)
x_change = 0
y_change = 0

timer = 3
dtime = 0

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

pygame.init()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Working Title')
clock = pygame.time.Clock()
shipImg = pygame.image.load('ship.png')

exit_game = False

#Game Loop
while exit_game == False:
    gameDisplay.fill(black)

    #Catch Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0


    #game logic  
    x = x + x_change

    if x < 0 or x > (display_width - ship_width):
        timer = round(timer - dtime, 2)
        message_display('Come back! ' + str(timer))

    if timer <= 0:
        exit_game = True

    
    #draw surface
    draw_image(shipImg, x, y)
            
    pygame.display.update()
    dtime = clock.tick(60) / 1000


#Exit Sequence
pygame.quit()
quit()

