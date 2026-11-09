import pygame
import random
pygame.init()
maxfps = 60
WIDTH = 600
HEIGHT = 600
animateframe = 0
started = 0
groundx1 = 0
groundx2 = 290
playervel = 0
px = 50
py = 300
pdir = 1
playerframe = 1
game_over = 0
infoframe = 0
screen = pygame.display.set_mode((WIDTH,HEIGHT))
bg = pygame.image.load("pygame/flappy bird/images/bg.png")
ground = pygame.image.load("pygame/flappy bird/images/ground.png")
phitbox = pygame.Rect(px,py,30,30)
clock = pygame.time.Clock()
r_button_hitbox = pygame.Rect(240,220,150,75)
bird1 = pygame.image.load("pygame/flappy bird/images/bird1.png")
bird2 = pygame.image.load("pygame/flappy bird/images/bird2.png")
bird3 = pygame.image.load("pygame/flappy bird/images/bird3.png")
restart_button = pygame.image.load("pygame/flappy bird/images/restart.png")
pipedown = pygame.image.load("pygame/flappy bird/images/pipe.png")
pipeup = pygame.transform.flip(pipedown,False,True)
die_sound = pygame.mixer.Sound("pygame/flappy bird/images/Slap DIE.wav")
flap_sound = pygame.mixer.Sound("pygame/flappy bird/images/flap.wav")
restart_button = pygame.transform.scale(restart_button,(150,75))
info1 = pygame.image.load("pygame/flappy bird/images/tapinfo.png")
info2 = pygame.image.load("pygame/flappy bird/images/tapinfo2.png")
info1 = pygame.transform.scale(info1,(270,220))
info2 = pygame.transform.scale(info2,(270,220))
pipex =  10000
pipey = 0
pipeframe = 0
small = 0
score = 0
pipeuph = pygame.Rect(pipex,pipey,pipeup.get_width(),pipeup.get_height())
pipedownh = pygame.Rect(pipex,pipey,pipedown.get_width(),pipedown.get_height())
mode = 1
font = pygame.font.SysFont("sansserifcollection",40)
while True:
    clock.tick(maxfps)
    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over == 0:
                started = 1
                if mode == 1:
                    playervel = 9
                if mode == 2:
                    playervel = 10
                if mode == 3:
                    playervel = 12
                flap_sound.play()
            else:
                if r_button_hitbox.collidepoint(event.pos):
                    animateframe = 0
                    started = 0
                    groundx1 = 0
                    groundx2 = 290
                    playervel = 0
                    px = 50
                    py = 300
                    pdir = 1
                    playerframe = 1
                    game_over = 0
                    infoframe = 0
                    pipex =  10000
                    pipey = 0
                    pipeframe = 0
                    small = 0

            
            
        elif event.type == pygame.KEYDOWN:
            if started == 0:
                if event.key == pygame.K_1:
                    mode = 1
                if event.key == pygame.K_2:
                    mode = 2
                if event.key == pygame.K_3:
                    mode = 3
            if event.key == pygame.K_SPACE:
                if game_over == 0:
                    started = 1
                    if mode == 1:
                        playervel = 9
                    if mode == 2:
                        playervel = 10
                    if mode == 3:
                        playervel = 12
                    flap_sound.play()
                
        if event.type == pygame.QUIT:
            pygame.quit()
    score = font.render(score,True,"#FF7300")
    mode = font.render(score,True,"#00FF0D")
    if animateframe >= 30:
        animateframe = 0
        if playerframe == 3:
            playerframe = 1
        elif playerframe == 2:
            playerframe = 3
        elif playerframe == 1:
            playerframe = 2
    if started == 1 and game_over == 0:
        pipeuph.x = pipex
        pipeuph.y = pipey - 360
        pipedownh.x = pipex
        pipedownh.y = pipey + 360
        pipeframe += 1
        playervel -= 0.5
        pdir = playervel*3
        animateframe += 10
        py -= playervel
        phitbox.y = py
        groundx1 -= 6
        groundx2 -= 6
        if groundx1 <= -300:
            groundx1 = 300
        if groundx2 <= -300:
            groundx2 = 300
        if py >= 400 or py <= -10:
            game_over = 1
            die_sound.play()
 
    if pipeframe >= 190:
        pipeframe = 0
        pipex = 620
        pipey = random.randint(-200,100)
        if small == 1:
            score += 1
        small = 1
    pipex -= 6
    screen.blit(bg,(0,0))
    screen.blit(pipeup,(pipex,pipey-360))
    screen.blit(pipedown,(pipex,pipey+360))
    screen.blit(ground,(groundx1,450))
    screen.blit(ground,(groundx2,450))
    screen.blit("score: "+ str(score),(10,10))
    screen.blit("mode: "+ str(mode),(10,100))
    if started == 0 and game_over == 0:
        
        infoframe += 1
        if infoframe >= 0:
            screen.blit(info1,(180,220))
        else:
            screen.blit(info2,(180,220))
        if infoframe >= 30:
            
            infoframe = -30
    if pipeuph.colliderect(phitbox):
        game_over = 1
        die_sound.play()
        pipeuph.x = 10000
    if pipedownh.colliderect(phitbox):
        game_over = 1
        die_sound.play()
        pipedownh.x = 10000
    if game_over == 1:
        screen.blit(restart_button,(240,220))
    if playerframe == 3:
        screen.blit(pygame.transform.rotate(bird3,pdir),(px,py))
        
    elif playerframe == 2:
        
        screen.blit(pygame.transform.rotate(bird2,pdir),(px,py))
    elif playerframe == 1:
        
        screen.blit(pygame.transform.rotate(bird1,pdir),(px,py))
    pygame.display.update()
    
