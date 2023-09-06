import pygame
import random
import math
from pygame import mixer

#Intalize the pygame
pygame.init()
#create a screen
screen=pygame.display.set_mode((800,600))
#title and icon
pygame.display.set_caption("Space invadors")
icon=pygame.image.load('startup.png')
pygame.display.set_icon(icon)
#background
background=pygame.image.load('2474216.jpg')
#player
playerImg=pygame.image.load('player.png')
playerX=380
playerY=470
playerXChange=0
#enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyXChange=[]
enemyYChange=[]
enemyCount=6
enemy_blast=pygame.image.load('rocks.png')
for i in range(enemyCount):
    enemyImg.append(pygame.image.load('rock.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyXChange.append(0.3)
    enemyYChange.append(40)
#background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

#bullet
#ready-bullet is in the space ship
#fire-bullet fires form the space ship
bulletImg=pygame.image.load('bullet.png')
bulletX=380
bulletY=438
bulletXChange=0
bulletYChange=0.5
bulletState="Ready"
#collsion
def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance<=27:
        return True
    return False
#Score
score=0
font=pygame.font.Font('Super Corn.ttf',42)
textX=10
textY=10
def showScore(x,y):
   Score=font.render("Score :"+str(score),True,(255,255,255))
   screen.blit(Score,(x,y))
#Game over
game_over=False

font_game_over=pygame.font.Font('Super Corn.ttf',60)
gameover_X=300
gameover_Y=200
def gameOver(x,y):
   gameOver=font_game_over.render("GAME OVER",True,(255,255,255))
   screen.blit(gameOver,(x,y))
font_Restart=pygame.font.Font('Super Corn.ttf',60)
restart_X=150
restart_Y=300
def restart(x,y):
    restart=font_Restart.render("Press Tab to Restart",True,(255,255,255))
    screen.blit(restart,(x,y))


#to reset game
def allreset():
    playerX=380
    playerY=470
    playerXChange=0
    bulletX=380
    bulletY=438
    bulletXChange=0
    bulletYChange=0.5
    bulletState="Ready"
    score=0
    enemyImg=[]
    enemyX=[]
    enemyY=[]
    enemyXChange=[]
    enemyYChange=[]
    enemyCount=6
    enemy_blast=pygame.image.load('rocks.png')
    for i in range(enemyCount):
        enemyImg.append(pygame.image.load('rock.png'))
        enemyX.append(random.randint(0,736))
        enemyY.append(random.randint(50,150))
        enemyXChange.append(0.3)
        enemyYChange.append(40)
    game_over=False



#game loop
def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    if i>=enemyCount:
        screen.blit(enemy_blast,(x,y))
    else:

        screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global bulletState
    bulletState="fire"
    screen.blit(bulletImg,(x+16,y+16))

running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #if the keystroke is pressed then then
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerXChange=-0.3
            if event.key==pygame.K_RIGHT:
                playerXChange=0.3
            if event.key==pygame.K_SPACE and bulletState is "Ready":
                bullet_sound=mixer.Sound('laser.wav')
                bullet_sound.play()
                bulletX=playerX
                fire_bullet(bulletX,bulletY)
            if event.key==pygame.K_SPACE and game_over:
                allreset()

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_UP:
                playerXChange=0
        
    #for space ship direction
    playerX+=playerXChange
    
    if playerX<=0:
        playerX=0
    if playerX>=726:
        playerX=726
    #enemy
    for i in range(enemyCount):
        if enemyY[i]>440:
            for j in range(enemyCount):
                enemyY[j]=2000
            gameOver(gameover_X,gameover_Y)
            restart(restart_X,restart_Y)
            game_over=True
            continue
            
            
        

            
            

        enemyX[i]+=enemyXChange[i]
        if(enemyX[i]>=736):
            enemyX[i]=736
            enemyY[i]+=enemyYChange[i]
            enemyXChange[i]=-0.2
            
        if(enemyX[i]<=0):
            enemyX[i]=0
            enemyY[i]+=enemyYChange[i]
            enemyXChange[i]=0.2
        #collision detection
        collison=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collison:
            collision_sound=mixer.Sound('explosion.wav')
            collision_sound.play()
            bulletY=480
            bulletState="Ready"
            score+=1
            enemy(enemyX[i],enemyY[i],34)
            
            enemyX[i]=random.randint(0,736)
            enemyY[i]=random.randint(50,150)
        enemy(enemyX[i], enemyY[i],i)
    #bulllet
    if(bulletY<=0):
        bulletState="Ready"
        bulletY=438
    if bulletState is "fire":
        
        fire_bullet(bulletX,bulletY)

        bulletY-=bulletYChange
    
    

        
        
        
        
    
        
    
    
        
        
    showScore(textX,textY)
    player(playerX,playerY)
    pygame.display.update()