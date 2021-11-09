

import pygame, random

##############################################################################
#                                   CLASSES                                  #
##############################################################################
class Obstacles():
    x = y = d = xSpeed = ySpeed = typeO = 0

class Button():
    x = y = w = h = colour = text = 0

class User():
    x = y = xSpeed = ySpeed = colour = 0

class Player():
    name = score = 0

##############################################################################
#                                  FUNCTIONS                                 #
##############################################################################
def collideObstacles (x1,y1,w1,h1,x2,y2,w2,h2):
    return x1 <= x2+w2 and x1+w1 >= x2 and y1 <= y2+h2 and y1+h1 >= y2

##############################################################################
#                      ONE TIME SETUP (GLOBAL VARIABLES)                     #
##############################################################################
pygame.init()
screen = pygame.display.set_mode([500,720])
pygame.display.set_caption("Final Draft!")

width = screen.get_width()
height = screen.get_height()

gameState = "Menu"
score = 0
navy = (0,0,139)
player = Player()

font40 = pygame.font.SysFont("Times New Roman", 40, bold = True, italic = False)
font20 = pygame.font.SysFont("Times New Roman", 20, bold = True, italic = True)
font12 = pygame.font.SysFont("Times New Roman", 12, bold = True, italic = False)

startButton = Button()
startButton.w = 120
startButton.h = 80
startButton.x = width*0.8 - 120
startButton.y = height - 200
startButton.colour = (0,0,0)
startButton.text = "Play"

infoButton = Button()
infoButton.w = 200
infoButton.h = 80
infoButton.x = width*0.5 - 200
infoButton.y = height - 200
infoButton.colour = (0,0,0)
infoButton.text = "How to Play"

menuButton = Button()
menuButton.w = 100
menuButton.h = 50
menuButton.x = width/2 - 50
menuButton.y = height - 200
menuButton.colour = (0,0,0)
menuButton.text = "MENU"

##############################################################################
#                                 GAME LOOP                                  #
##############################################################################
while True:
    # ========================== HANDLE EVENTS ============================= #
    done = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
            break
        # ==================== MOUSE DOWN ==================== #
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            if gameState == "Menu":
                if mouseX >= startButton.x and mouseX <= startButton.x + startButton.w and mouseY >= startButton.y and mouseY <= startButton.y + startButton.h:
                    #probelm w game state returning to reset in game state (fixed by setting timer to 0 and variables to og value)

                    score = 0
                    user = User()
                    user.x = 250
                    user.y = height-300
                    user.xSpeed = 0
                    user.ySpeed = 2
                    user.colour = (255,0,0)
                    lines = [[250,height],[250,height-200],[250,height-300]]
                    lineySpeed = 2

                    name = ""

                    scores = []
                    obstacles = []
                    
                    for i in range(45):
                        while True:
                            
                                
                            obstacle = Obstacles()
                            obstacle.typeO = random.randint(0,1)
                            obstacle.d = random.randint(10,20)
                            obstacle.x = random.randint(0,width - obstacle.d) 
                            obstacle.y = random.randint(0,height) - height
                            obstacle.xSpeed = 0
                            obstacle.ySpeed = 2
                            freeSpace = True

                            #guarentee theres an obstacle in the middle, so the user is forced to use the spacebar everytime
                            if i == 0:
                                obstacle.x = width/2

                            #some obstacles still overlapping
                            for i in range(len(obstacles)):
                                if collideObstacles (obstacle.x - obstacle.d/2 ,obstacle.y -obstacle.d/2 ,obstacle.d*2,obstacle.d*2, obstacles[i].x - obstacles[i].d/2 ,obstacles[i].y - obstacles[i].d/2  ,obstacles[i].d*2,obstacles[i].d*2) == True:
                                    freeSpace = False
                                    break
                                
                            if freeSpace == True:
                                obstacles.append(obstacle)
                                break
                            
                    gameState = "In Game"
                    
                elif mouseX >= infoButton.x and mouseX <= infoButton.x + infoButton.w and mouseY >= infoButton.y and mouseY <= infoButton.y + infoButton.h:
                    gameState = "Info"

                    
        # ==================== MOUSE UP ====================== #
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            
        # ==================== KEY DOWN ====================== #
        elif event.type == pygame.KEYDOWN:
            if gameState == "In Game":
                if event.key == pygame.K_SPACE:
                            
                    if user.xSpeed == 0:
                        user.xSpeed = 2
                        user.x = user.x + user.xSpeed
                        lines.append([user.x,user.y])
                    else:
                        user.xSpeed = user.xSpeed*-1
                        user.x = user.x + user.xSpeed
                        lines.append([user.x,user.y])

                                        
            if gameState == "Info":
                if event.key == pygame.K_BACKSPACE:
                    gameState = "Menu"
                    
            if gameState == "End Game":
                if event.key == pygame.K_BACKSPACE:
                    gameState = "Menu"

                if event.key == pygame.K_RIGHT:
                    gameState = "Highscores"
                    
                if event.key == pygame.K_a:
                    name = name + "a"

                if event.key == pygame.K_b:
                    name = name + "b"

                if event.key == pygame.K_c:
                    name = name + "c"

                if event.key == pygame.K_d:
                    name =name + "d"

                if event.key == pygame.K_e:
                    name = name + "e"

                if event.key == pygame.K_f:
                    name = name + "f"

                if event.key == pygame.K_g:
                    name = name + "g"

                if event.key == pygame.K_h:
                    name = name + "h"

                if event.key == pygame.K_i:
                    name = name + "i"

                if event.key == pygame.K_j:
                    name = name + "j"

                if event.key == pygame.K_k:
                    name = name + "k"

                if event.key == pygame.K_l:
                    name = name + "l"

                if event.key == pygame.K_m:
                    name = name + "m"

                if event.key == pygame.K_n:
                    name = name + "n"

                if event.key == pygame.K_o:
                    name = name + "o"

                if event.key == pygame.K_p:
                    name = name + "p"

                if event.key == pygame.K_q:
                    name = name + "q"

                if event.key == pygame.K_r:
                    name = name + "r"

                if event.key == pygame.K_s:
                    name = name + "s"

                if event.key == pygame.K_t:
                    name = name + "t"

                if event.key == pygame.K_u:
                    name = name + "u"

                if event.key == pygame.K_v:
                    name = name + "v"

                if event.key == pygame.K_w:
                    name = name + "w"

                if event.key == pygame.K_x:
                    name = name + "x"

                if event.key == pygame.K_y:
                    name = name + "y"

                if event.key == pygame.K_z:
                    name = name + "z"


                if event == pygame.K_RETURN:
                    goodscore = True

                    if goodscore == True:
                        player.name = []
                        player.name.append (name)
                        name = ""
                        player.score = score
                        scores.append(score)

                gameState = "HighScore"

            if gameState == "Highscores":
                if event.key == pygame.K_r:
                    gameState = "Menu"
                    
            
                    
        # ==================== KEY UP ======================== #
        elif event.type == pygame.KEYUP:
            if gameState == "End Game":
                    if event.key == pygame.K_BACKSPACE:
                        gameState = "Menu"
    if done == True:
       break
    
    # ============================== MOVE STUFF ============================ #
    if gameState == "In Game":
 #obstacles to start falling at timer = 1
        for i in range(len(obstacles)): 
            obstacles[i].y = obstacles[i].y + obstacles[i].ySpeed
            if obstacles[i].y > height:
                obstacles[i].y = 0

        for i in range(len(lines)):
            if i == len(lines) - 1:
                lines[i][0] = lines[i][0] + user.xSpeed
                user.x = user.x + user.xSpeed
            else:
                lines[i][1] = lines[i][1] + user.ySpeed
        
    # ============================== COLLISION ============================= #
    if gameState == "In Game":
        #only works for some obstacles
        for obstacle in obstacles:
            if collideObstacles (obstacle.x,obstacle.y,obstacle.d,obstacle.d,user.x,user.y,1,1) == True:
                gameState = "End Game"
                
        if user.x == width or user.x == 0:
            gameState = "End Game"

        if lines[i][1] == height or lines[i][1] == 0:
            gameState = "End Game"

    if gameState == "End Game":
        scores.append(score)

    # ============================== DRAW STUFF ============================ #
    if gameState == "Menu":
        screen.fill ((109,109,109))

        text1 = font40.render('Avoid the Black', True, (255,0,0))
        screen.blit(text1,[width/2 - 150, height/3])

        pygame.draw.rect(screen, startButton.colour, [startButton.x, startButton.y, startButton.w, startButton.h])
        text1 = font40.render(startButton.text, True, (255,0,0))
        screen.blit(text1, [startButton.x+20, startButton.y+20])

        pygame.draw.rect(screen, infoButton.colour, [infoButton.x-10, infoButton.y, infoButton.w+31, infoButton.h])
        text2 = font40.render(infoButton.text, True, (255,0,0))
        screen.blit(text2, [infoButton.x+10, infoButton.y+20])


    elif gameState == "Info":
        screen.fill((0,0,0))
        
        title = font20.render('How to Play', True, (255,255,255))
        info1 = font12.render('Avoid the Black is a game of personal record.', True, (255,255,255))
        info2 = font12.render('To win the game, you must avoid all obstacles that approach you.',True, (255,255,255))
        info3 = font12.render('If you collide with any obstacles, you will lose.',True, (255,255,255))
        info4 = font12.render('As the player, you can only move diagonally left or right. (45 degrees or 135 degrees)',True, (255,255,255))
        info5 = font12.render('If you want to move diagonally, use the SPACEBAR key.',True, (255,255,255))
        goback = font20.render('PRESS <BACKSPACE> TO RETURN TO MENU', True, (255,255,255))

        screen.blit(title, [width*0.05, height*0.1])
        screen.blit(info1, [width*0.05, height*0.2])
        screen.blit(info2, [width*0.05, height*0.24])
        screen.blit(info3, [width*0.05, height*0.28])
        screen.blit(info4, [width*0.05, height*0.32])
        screen.blit(info5, [width*0.05, height*0.36])
        screen.blit(goback, [width*0.05, height*0.8])
        
    elif gameState == "In Game":
        screen.fill((47,79,79))
        
        text = font40.render('Time: ' + str(score), True, (0,0,0))
        score = score + 0.01
        screen.blit(text, [10, 10])
        
        for obstacle in obstacles:
            if obstacle.typeO == 0:
                pygame.draw.ellipse (screen, (0,0,0) , [obstacle.x, obstacle.y, obstacle.d, obstacle.d])
            else:
                pygame.draw.rect (screen, (0,0,0), [obstacle.x, obstacle.y, obstacle.d, obstacle.d])

        pygame.draw.lines(screen,(255,0,0),False,lines,4)
            
        #loop of lines.. every time the user changes position, a new line is made and the other line moves down


    elif gameState == "End Game":
        screen.fill ((255,0,0))
        text = font40.render('Time = ' + str(score), True, navy)
        screen.blit(text, [80, height/2])

    #fix username input
        text = font20.render('Enter Name = ' + name), True, navy)
        screen.blit(text, [80, height/2 + 50])
                    
        scorestate = font20.render('PRESS <RIGHT ARROW> TO SEE HIGHSCORES', True, (255,255,255))
        screen.blit(scorestate, [width*0.05, height*0.8])

        text = font20.render('PRESS <BACKSPACE> TO SEE MENU', True, (255,255,255))
        screen.blit(text, [width*0.05, height*0.7])


    elif gameState == "Highscores":
        screen.fill ((255,0,0))
        text = font20.render('HIGHSCORES',True,navy)
        screen.blit(text, [80,50])

        #fix highscores
        text = font20.render('Players',True,navy)
        screen.blit(text, [80,80])

        text = font20.render('Score',True,navy)
        screen.blit(text, [120,80])

        for score in scores:
            text1 = font20.render(str(player.name[0]),True,navy)
            screen.blit(text1, [80,120 + scores.index(player.score)])

            text2 = font20.render(str(player.score[0]),True,navy)
            screen.blit(text2, [120,120 + scores.index(player.score)])
            
        
        menuback = font20.render('PRESS <r> TO RETURN TO MENU', True, (255,255,255))
        screen.blit(menuback, [width*0.05, height*0.8])
        
        
        text = font20.render('HIT <BACKSPACE> TO PLAY AGAIN', True, navy)
        screen.blit(text, [30, height - 100])


    # ===================== PYGAME STUFF (NO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(10)

