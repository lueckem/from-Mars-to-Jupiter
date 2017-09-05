import pygame

#variables
display_height = 800
display_width = 600
black = (0,0,0)
white = (255,255,255)

x = (display_width * 0.45)
y = (display_height * 0.9)

#functions
def draw_image(image, x, y):
    gameDisplay.blit(image, (x,y))

pygame.init()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Working Title')
clock = pygame.time.Clock()
shipImg = pygame.image.load('ship.png')

exit_game = False

#Game Loop
while exit_game == False:

    #Catch Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    gameDisplay.fill(black)
    draw_image(shipImg, x, y)
            
    pygame.display.update()
    clock.tick(60)


#Exit Sequence
pygame.quit()
quit()

