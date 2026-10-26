import pygame
pygame.init()
maxfps = 60
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
bg = pygame.image.load("pygame/flappy bird/images/bg.png")
ground = pygame.image.load("pygame/flappy bird/images/ground.png")
animateframe = 0
started = 0
groundx1 = 0
groundx2 = 290
playervel = 0
px = 50
py = 300
pdir = 90
bird1 = pygame.image.load("pygame/flappy bird/images/bird1.png")
bird2 = pygame.image.load("pygame/flappy bird/images/bird2.png")
bird3 = pygame.image.load("pygame/flappy bird/images/bird3.png")

playerframe = 1
clock = pygame.time.Clock()

phitbox = pygame.Rect(px,py,30,30)




while True:
    clock.tick(maxfps)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            started = 1
            playervel = 16
            pdir = 45
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                started = 1
                playervel = 16
                pdir = 45
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
    if started == 1:
        playervel -= 0.5
        pdir += 1
        animateframe += 10
        py -= playervel
        groundx1 -= 2
        groundx2 -= 2
        if groundx1 <= -300:
            groundx1 = 300
        if groundx2 <= -300:
            groundx2 = 300
        bird1 = pygame.transform.rotate(bird1,pdir)
        bird2 = pygame.transform.rotate(bird2,pdir)
        bird3 = pygame.transform.rotate(bird3,pdir)


    screen.blit(bg,(0,0))
    screen.blit(ground,(groundx1,450))
    screen.blit(ground,(groundx2,450))
    if playerframe == 3:
        screen.blit(bird3,(px,py))
    elif playerframe == 2:
        screen.blit(bird2,(px,py))
    elif playerframe == 1:
        screen.blit(bird1,(px,py))
    pygame.display.update()
