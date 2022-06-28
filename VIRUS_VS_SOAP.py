# from curses import window
# from operator import imod, truediv
# from pickle import FALSE
# from cv2 import transform
# from numpy import disp
import pygame
import random
import math
from pygame import mixer

pygame.init() #initialization of pygame
screen=pygame.display.set_mode((800,600))

# display
pygame.display.set_caption("VIRUS_SOAP VOL_1")
icon=pygame.image.load("coronavirus.png")
pygame.display.set_icon(icon)
img=pygame.image.load("13.png")
mixer.music.load("background.wav")
# transform.scale(img,(800,600))
# i=0
mixer.music.play(-1)
# player
player1=pygame.image.load("player.png")
# x1=0
# y1=0

x=340
y=550
x_change=0

#enmy list
enemy=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
no_enemys=6

#enemy
for i in range(no_enemys):
    enemy.append(pygame.image.load("ghost.png"))
    enemyx.append(random.randint(1,760))
    enemyy.append(random.randint(1,100))
    enemyx_change.append(0.3)
    enemyy_change.append(0.2)

#bullet
bull=pygame.image.load("soap.png")
bulletx=0
bullety=550
bulletx_change=0
bullety_change= 2
bullet_state ="ready"


score=0
font=pygame.font.Font("freesansbold.ttf",35)
textx=10
texty=10

over=pygame.font.Font("freesansbold.ttf",55)

def show_score(x1,y1):
    sr=font.render("SCORE   :"+ str(score),True,(255,255,255))
    screen.blit(sr,(x1,y1))
    
def game_over():
    gameover=over.render("ITS GAME OVER !!",True,(255,255,255))
    screen.blit(gameover,(250,300))

def player(x1,y1):
    screen.blit(player1,(x1,y1))
    
def enemy1(x1,y1,i):
    screen.blit(enemy[i],(x1,y1))
    
def bullet(x1,y1):
    global bullet_state
    bullet_state="fire"
    screen.blit(bull,(x1+4,y1+6))

def iscoll(enemyx,enemyy,bulletx,bullety):
    distence=math.sqrt(math.pow(enemyx-bulletx,2) + math.pow(enemyy-bullety,2))
    if distence<16:
        return True
    else:
        return False
        
run=True
while run:      #game loop
    screen.fill((255,255,255))                 #background
    screen.blit(img,(0,0))                                                # x -= 0.2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            
    #controls
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -0.4
            if event.key == pygame.K_RIGHT:
                x_change = +0.4
            
            # fire
            
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bs=mixer.Sound("laser.wav")
                    bs.play()
                    bulletx=x               
                    bullet(bulletx,bullety)
                    break
               
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                 x_change = 0
                 
    x += x_change    
    
    # player boundry
    if x <= 0:
        x=0
    elif x>=760:
        x=760
        
    # enemy boundry
    for i in range(no_enemys): 
        if enemyy[i] >500:
            # for j in range(no_enemys):
            enemyy[i] = 1000
            game_over()
            break
        enemyx[i] += enemyx_change[i]
        enemyy[i] += enemyy_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 0.3
        elif enemyx[i] >= 740:
            enemyx_change[i] = -0.3
        elif enemyy[i]<= 0:
            enemyy[i]=0
        elif enemyy[i]>=600:
            enemyy[i] = -0.2
            enemyy[i]=0
    
    #collition
        coll=iscoll(enemyx[i],enemyy[i],bulletx,bullety)
        if coll:
            cs=mixer.Sound("explosion.wav")
            cs.play()
            bullety=550
            bullet_state="ready"
            score+=1
            # print(score)
            enemyx[i]=random.randint(0,740)
            enemyy[i]=random.randint(40,100)
            
        enemy1(enemyx[i],enemyy[i],i)
    #bullet
    if bullety <= 0:
        bullety = 550
        bullet_state = "ready"
        
    if bullet_state is "fire":
        bullet(x,bullety)
        bullety -= bullety_change
        
    #collition
    
        
    
    player(x,y)
    show_score(textx,texty)
    pygame.display.update()
    