import pygame, sys


SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1200

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

alpha_suf = pygame.image.load("alpha.png").convert_alpha()
alpha_pos = (100, 100)
alpha_mask = pygame.mask.from_surface(alpha_suf)

new_alpha_suf = alpha_mask.to_surface()
new_alpha_suf.set_colorkey((0, 0, 0))

surf_w, surf_h = new_alpha_suf.get_size()
for x in range(surf_w):
    for y in range(surf_h):
        if new_alpha_suf.get_at((x, y))[0] != 0:
            new_alpha_suf.set_at((x, y), "orange")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    offset = 4
    screen.blit(new_alpha_suf,(alpha_pos[0]+ offset,alpha_pos[1]))
    screen.blit(new_alpha_suf,(alpha_pos[0]- offset,alpha_pos[1]))
    screen.blit(new_alpha_suf,(alpha_pos[0],alpha_pos[1]+ offset))
    screen.blit(new_alpha_suf,(alpha_pos[0],alpha_pos[1]- offset))
    screen.blit(new_alpha_suf,(alpha_pos[0]- offset,alpha_pos[1]- offset))
    screen.blit(new_alpha_suf,(alpha_pos[0]+ offset,alpha_pos[1]+ offset))
    screen.blit(new_alpha_suf,(alpha_pos[0]+ offset,alpha_pos[1]- offset))
    screen.blit(new_alpha_suf,(alpha_pos[0]- offset,alpha_pos[1]+ offset))

    screen.blit(alpha_suf, alpha_pos)
    
    # for pos in alpha_mask.outline():
    #     pygame.draw.circle(screen, "yellow", (pos[0] + alpha_pos[0], pos[1] + alpha_pos[1]), 3)



    pygame.display.flip()
    clock.tick(60)
