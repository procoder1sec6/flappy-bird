import pygame
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
die_sound = pygame.mixer.Sound("pygame/flappy bird/images/Slap DIE.wav")
flap_sound = pygame.mixer.Sound("pygame/flappy bird/images/flap.wav")
restart_button = pygame.transform.scale(restart_button,(150,75))
info1 = pygame.image.load("pygame/flappy bird/images/tapinfo.png")
info2 = pygame.image.load("pygame/flappy bird/images/tapinfo2.png")
info1 = pygame.transform.scale(info1,(200,200))
info2 = pygame.transform.scale(info2,(200,200))



while True:
    clock.tick(maxfps)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over == 0:
                started = 1
                playervel = 10
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

            
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over == 0:
                    started = 1
                    playervel = 10
                    flap_sound.play()
                
        if event.type == pygame.QUIT:
            pygame.quit()
    
    if animateframe >= 30:
        animateframe = 0
        if playerframe == 3:
            playerframe = 1
        elif playerframe == 2:
            playerframe = 3
        elif playerframe == 1:
            playerframe = 2
    if started == 1 and game_over == 0:
        playervel -= 0.5
        pdir = playervel*3
        animateframe += 10
        py -= playervel
        groundx1 -= 2
        groundx2 -= 2
        if groundx1 <= -300:
            groundx1 = 300
        if groundx2 <= -300:
            groundx2 = 300
        if py >= 400:
            game_over = 1
            die_sound.play()

    
    screen.blit(bg,(0,0))
    screen.blit(ground,(groundx1,450))
    screen.blit(ground,(groundx2,450))
    if started == 0 and game_over == 0:
        
        infoframe += 1
        if infoframe >= 1:
            print("works")
            screen.blit(info1,(240,220))
        elif infoframe >= 60:
            screen.blit(info2,(240,220))
            infoframe = 0
    if game_over == 1:
        screen.blit(restart_button,(240,220))
        

    if playerframe == 3:
        
        screen.blit(pygame.transform.rotate(bird3,pdir),(px,py))
    elif playerframe == 2:
        
        screen.blit(pygame.transform.rotate(bird2,pdir),(px,py))
    elif playerframe == 1:
        
        screen.blit(pygame.transform.rotate(bird1,pdir),(px,py))
    pygame.display.update()
