import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

screen_time = 0
btn_press_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            btn_press_time = pygame.time.get_ticks()
            screen.fill((255,255,255))
    
    screen_time = pygame.time.get_ticks()

    if screen_time - btn_press_time >= 2000:
        screen.fill((0,0,0))
    
    pygame.display.flip()
    clock.tick(60)