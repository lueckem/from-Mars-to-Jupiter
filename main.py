## to do:
## update asteroid graphics
## small tutorial
## easy,medium,hard
## optimize control sensibility

import pygame
import random

pygame.init()

#constants
display_height = 700
display_width = 600
ship_width = 60
ship_height = 80
shot_width = 5
shot_height = 15
shot_speed = 20
thing_width = 6
thing_speed = 6

large_text = 40
small_text = 20

num_small_asteroids = 10
small_asteroid_width = 30
small_asteroid_height = 30

num_medium_asteroids = 5
medium_asteroid_width = 70
medium_asteroid_height = 70

num_large_asteroids = 2
large_asteroid_width = 110
large_asteroid_height = 80

bonus_radius = 15
num_shot_boni = 1
num_score_boni = 1
num_slow_boni = 1

black = (0,0,0)
white = (255,255,255)
dark_white = (175,175,175)
red = (255,0,0)
bright_blue = (138,255,255)

paused = False

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('From Mars to Jupiter')
clock = pygame.time.Clock()

#load graphics
shipImg = pygame.image.load('ship.png')
asteroid_small_Img = pygame.image.load('asteroid_small.png')
asteroid_medium_Img = pygame.image.load('asteroid_medium.png')
asteroid_large_Img = pygame.image.load('asteroid_large.png')
tutorialImg =  pygame.image.load('tutorial.png')

#functions
def game_quit():
    pygame.quit()
    quit()
    
def draw_image(image, x, y):
    gameDisplay.blit(image, (x,y))

def message_display(text, size, x, y):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf, TextRect)
    
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

#checks if 2 objects crashed
def crashed(pos1,pos2, width_1, height_1, width_2, height_2):

    if pos1[0] - width_2 <= pos2[0] <= pos1[0] + width_1:
        if pos1[1] - height_2 <= pos2[1] <= pos1[1] + height_1:
            return True
    else:
        return False

def score_display(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(score), True, white)
    gameDisplay.blit(text,(0,0))

def shots_display(num_shots):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Shots: "+str(num_shots), True, white)
    gameDisplay.blit(text,(0,20))

#builds a button and does action if clicked
def button(text, x, y, width, height, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x <= mouse[0] <= x + width and y <= mouse[1] <= y + height:
        pygame.draw.rect(gameDisplay, white,(x, y, width, height))
        pygame.draw.rect(gameDisplay, black,(x + 2, y +2, width - 4, height - 4))
        message_display(text, small_text, x + width/2, y + height/2)
        if click[0] == 1:
            pygame.time.delay(100)
            action()
    else:
        pygame.draw.rect(gameDisplay, dark_white,(x, y, width, height))
        pygame.draw.rect(gameDisplay, black,(x + 2, y +2, width - 4, height - 4))
        message_display(text, small_text, x + width/2, y + height/2)

def unpause():
    global paused
    paused = False
    
#asks user question and displays and returns answer
def ask(question):
    answer = ""
    while 1:
        gameDisplay.fill(black)
        message_display("You got a Highscore!", large_text, display_width/2 , display_height/10)
        message_display(question + ": " + answer, large_text, display_width/2 , display_height/2)

        
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            key = event.key

            if key == pygame.K_BACKSPACE:
                answer = answer[0:-1]
            elif key == pygame.K_RETURN:
              break
            elif key <= 127:
                answer += chr(key)

        pygame.display.update()
    
    return answer

#key function for highscores
def getKey(item):
    return int(item[0])

#key function for Stars
def getKey_stars(star):
    return star.y

       
#classes
class Asteroid:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class Shot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bonus:
    def __init__(self, x, y, feature):
        self.x = x
        self.y = y
        self.feature = feature
        
class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y



#function to draw stars
def init_background(y,width,height,num):
    stars = []
    for i in range(0,num-1):
        stars.append(Star(random.randint(0,width),random.randint(y ,y + height)))
        
    stars.append(Star(random.randint(0,width), y))
    return stars

#controls and tutorial
def controls():
    exit_controls = False
    while exit_controls == False:
        gameDisplay.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: game_quit()

        message_display("Controls", large_text, display_width/2 , display_height/10)
        message_display("Move: Left and right arrow keys", small_text, 300, 130)
        message_display("Shoot: Space", small_text, 300, 160)
        message_display("Pause: p", small_text, 300, 190)

        draw_image(tutorialImg, 75, 240)
        #draw first bonus
        pygame.draw.circle(gameDisplay, white, (275,240+235), bonus_radius, 2)
        pygame.draw.rect(gameDisplay, red, (275 - bonus_radius/5 , 240+235 - (4*bonus_radius)/5, (2*bonus_radius)/5, (8*bonus_radius)/5))
        #draw second bonus
        pygame.draw.circle(gameDisplay, white, (300,240+275), bonus_radius, 2)
        message_display("+20", 10, 300, 240+275)
        #draw third bonus
        pygame.draw.circle(gameDisplay, white, (325,240+315), bonus_radius, 2)
        pygame.draw.polygon(gameDisplay, white, [[325 - 7, 240+315 - 7], [325 + 7, 240+315 -7], [325, 240+315 + 10]])
        
        button("back",display_width/3,610,200,50,menu)

        pygame.display.update()

def show_highscores():
    #get current highscores
    highscores = []
    file = open("highscores.txt", "r")
    for line in file:
        highscores.append(line)
    file.close()

    
    exit_highscores = False
    while exit_highscores == False:
        gameDisplay.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: game_quit()

        message_display("Highscores", large_text, display_width/2 , display_height/10)

        for i in range(0,len(highscores)):
            message_display(highscores[i][:-1], small_text, display_width/2 , 100 + (30*(i+1)))
        
        button("back",display_width/3,550,200,50,menu)

        pygame.display.update()


#main menu
def menu():
    exit_menu = False
    while exit_menu == False:
        gameDisplay.fill(black)
        for event in pygame.event.get():
                if event.type == pygame.QUIT: game_quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: game_loop()

        message_display("From Mars to Jupiter", large_text, display_width/2 , display_height/10)

        button("Play",display_width/3,150,200,50,game_loop)
        button("Controls",display_width/3,220,200,50,controls)
        button("Highscores",display_width/3,290,200,50,show_highscores)
        button("Quit",display_width/3,360,200,50,game_quit)

        pygame.display.update()

#menu that shows after you loose
def crash_menu(score):
    #make list of current highscores
    highscores = []
    file = open("highscores.txt", "r")
    for line in file:
        highscores.append(line)
    file.close()

    #convert list of lines to list of partitions
    for i in range(len(highscores)):
        highscores[i] = highscores[i][:-1]
        highscores[i] = highscores[i].partition(" ")
    

    #if the score is high enough ask for name, else only show menu
    if (len(highscores) > 0 and score > int(min(highscores, key = getKey)[0])) or len(highscores) < 10:
        gameDisplay.fill(black)
        username = ask("name")

        highscores.append((str(score)," ",username))
        highscores.sort(key=getKey, reverse = True)

        if len(highscores) > 10:
            highscores.remove(highscores[10])

        #convert list back to lines and write in file
        file = open("highscores.txt", "w")
        for i in range(len(highscores)):
            highscores[i] = highscores[i][0] + highscores[i][1] + highscores[i][2] + "\n"
            file.write(highscores[i])

        file.close()

    #crash_menu
    exit_crash_menu = False
    while exit_crash_menu == False:
        gameDisplay.fill(black)
        for event in pygame.event.get():
                if event.type == pygame.QUIT: game_quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: game_loop()

        message_display("Final Score: " + str(score), large_text, display_width/2 , display_height/10)

        button("Restart",display_width/3,150,200,50,game_loop)
        button("Menu",display_width/3,220,200,50,menu)
        button("Quit",display_width/3,290,200,50,game_quit)

        message_display("You can also press space to restart.", small_text, display_width/2 , 400)

        pygame.display.update()

#pause
def pause():
    while paused == True:
        gameDisplay.fill(black)
        for event in pygame.event.get():
                if event.type == pygame.QUIT: game_quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        unpause()
                        

        message_display("Pause", large_text, display_width/2 , display_height/10)

        button("Continue",display_width/3,150,200,50,unpause)
        button("Restart",display_width/3,220,200,50,game_loop)
        button("Quit",display_width/3,290,200,50,game_quit)

        message_display("You can also press p to continue.", small_text, display_width/2 , 400)

        pygame.display.update()
    


#Game Loop
def game_loop():

    global paused

    #variables
    x = (display_width * 0.45)
    y = (display_height * 0.85)
    shoot = False
    score = 0
    fallspeed = 2
    num_shots = 3
    
    timer = 3
    dtime = 0

    asteroids = list()
    boni = list()
    shots = list()
    #exhaust = list()

    #initialize background
    stars_1 = init_background(0, display_width, display_height, 100)
    stars_2 = init_background(-display_height, display_width, display_height, 60)
    

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

    #initialize boni
    for i in range(0, num_shot_boni):
        boni.append(Bonus(random.randint(0, display_width), random.randint(-6000, -1500),"shots"))
    for i in range(0, num_score_boni):
        boni.append(Bonus(random.randint(0, display_width), random.randint(-6000, -1500),"score"))
    for i in range(0, num_slow_boni):
        boni.append(Bonus(random.randint(0, display_width), random.randint(-6000, -1500),"slow"))


    exit_game = False

    while exit_game == False:
        gameDisplay.fill(black)

        #Catch Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: game_quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and num_shots > 0:
                    shoot = True
                if event.key == pygame.K_p:
                    paused = True
                    pause()
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 10
        if pressed[pygame.K_RIGHT]: x += 10
            

 
        #game logic

        #update background
        for star in stars_1:
            star.y += round(fallspeed/2)
        if min(stars_1, key = getKey_stars).y >= display_height:
            stars_1 = init_background(-display_height, display_width, display_height, random.randint(50,250))

        for star in stars_2:
            star.y += round(fallspeed/2)
        if min(stars_2, key = getKey_stars).y >= display_height:
            stars_2 = init_background(-display_height, display_width, display_height, random.randint(50,250))


        
        #handle timer
        if timer > 0:
            if x < 0 or x > (display_width - ship_width):
                timer = round(timer - dtime, 2)
                message_display('Come back! ' + str(timer), large_text, display_width/2, display_height/2)
        else:
            message_display("You left your route!", large_text, display_width/2, display_height/2)
            pygame.display.update()
            pygame.time.delay(1500)
            crash_menu(score)
        
            
        #update asteroids position and check for crashes
        for asteroid in asteroids:
            asteroid.y = asteroid.y + fallspeed
            if crashed((x,y), (asteroid.x,asteroid.y), ship_width, ship_height, asteroid.width, asteroid.height) == True:
                message_display("You crashed!", large_text, display_width/2, display_height/2)
                pygame.display.update()
                pygame.time.delay(1500)
                crash_menu(score)
            
            if asteroid.y >= display_height + 100:
                asteroid.y = -800
                score += 1
                if score % 20 == 0 and score < 300:
                    fallspeed += 1
                
                asteroid_crash = True
                while asteroid_crash == True:
                    num_crashes = 0
                    x_asteroid = random.randint(-small_asteroid_width/2, display_width - (small_asteroid_width/2))                        
                    for asteroid_2 in asteroids:
                        if crashed((asteroid_2.x, asteroid_2.y), (x_asteroid, asteroid.y), asteroid_2.width, asteroid_2.height, asteroid.width, asteroid.height) == True:
                            num_crashes += 1

                    if num_crashes == 0:
                        asteroid.x = x_asteroid
                        asteroid_crash = False

        #shoot
        if shoot == True:
            shots.append(Shot(x+8,y-shot_height+shot_speed))
            shots.append(Shot(x+48,y-shot_height+shot_speed))
            shoot = False
            num_shots -= 1

        for shot in shots:
            shot.y -= shot_speed
            if shot.y < -1000:
                shots.remove(shot)
            for asteroid in asteroids:
                if crashed ((shot.x,shot.y),(asteroid.x, asteroid.y), shot_width, shot_height, asteroid.width, asteroid.height) == True:
                    shots.remove(shot)
                    asteroid.y = display_height +1000


        #update boni
        for bonus in boni:
            bonus.y += fallspeed
            if bonus.y > display_height + 100:
                bonus.y = random.randint(-6000, -500)
                bonus.x = random.randint(0, display_width)

            if crashed((x,y), (bonus.x-bonus_radius,bonus.y-bonus_radius), ship_width, ship_height, 2*bonus_radius,2*bonus_radius) == True:
                bonus.y = random.randint(-6000, -500)
                if bonus.feature == "shots":
                    num_shots += 3
                elif bonus.feature == "score":
                    score += 20
                elif bonus.feature == "slow":
                    fallspeed -= 1

        #draw surface
        #draw background
        for star in stars_1:
            pygame.draw.circle(gameDisplay, white, [star.x, star.y], 2)

        for star in stars_2:
            pygame.draw.circle(gameDisplay, white, [star.x, star.y], 2)


        #draw ship         
        draw_image(shipImg, x, y)
        
        #draw asteroids
        for asteroid in asteroids:
            if asteroid.width == small_asteroid_width:
                draw_image(asteroid_small_Img, asteroid.x, asteroid.y)
            elif asteroid.width == medium_asteroid_width:
                draw_image(asteroid_medium_Img, asteroid.x, asteroid.y)
            else:
                draw_image(asteroid_large_Img, asteroid.x, asteroid.y)
            
        #draw boni
        for bonus in boni:
            pygame.draw.circle(gameDisplay, white, (bonus.x,bonus.y), bonus_radius, 2)
            if bonus.feature == "shots":
                pygame.draw.rect(gameDisplay, red, (bonus.x - bonus_radius/5 , bonus.y - (4*bonus_radius)/5, (2*bonus_radius)/5, (8*bonus_radius)/5))
            elif bonus.feature == "score":
                message_display("+20", 10, bonus.x, bonus.y)
            elif bonus.feature == "slow":
                pygame.draw.polygon(gameDisplay, white, [[bonus.x - 7, bonus.y - 7], [bonus.x + 7, bonus.y -7], [bonus.x, bonus.y + 10]])
                

        #draw shots
        for shot in shots:
            pygame.draw.rect(gameDisplay, red, (shot.x, shot.y, shot_width, shot_height))

        #draw exhaust
##        exhaust.append(Star(x + 27, y + 63 - thing_speed))
##        for thing in exhaust:
##            thing.y += thing_speed
##            if thing.y > display_height:
##                exhaust.remove(thing)
##            pygame.draw.rect(gameDisplay, bright_blue, (thing.x, thing.y, thing_width, thing_speed))
        pygame.draw.polygon(gameDisplay, bright_blue, [[x + 27, y +63], [x + 33, y + 63], [x + 30, y + 63 + 28]])

        
                    
        score_display(score)
        shots_display(num_shots)
        pygame.display.update()
        dtime = clock.tick(60) / 1000


#Main Sequence
menu()
game_loop()
game_quit()
