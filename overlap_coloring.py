import pygame, sys


SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1200

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.mouse.set_visible(False)

ship_surf = pygame.image.load("ship.png").convert_alpha()
ship_rect = ship_surf.get_rect(center=(300, 300))
ship_mask = pygame.mask.from_surface(ship_surf)

alpha_surf = pygame.image.load("alpha.png").convert_alpha()
alpha_pos = (100, 100)
alpha_mask = pygame.mask.from_surface(alpha_surf)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    ship_rect.center = pygame.mouse.get_pos()
    screen.blit(alpha_surf, alpha_pos)
    screen.blit(ship_surf, ship_rect)

    offset_x = alpha_pos[0] - ship_rect.left
    offset_y = alpha_pos[1] - ship_rect.top
    if ship_mask.overlap(alpha_mask, (offset_x, offset_y)):
        new_mask = ship_mask.overlap_mask(alpha_mask, (offset_x, offset_y))
        new_surf = new_mask.to_surface()
        new_surf.set_colorkey((0, 0, 0))
        for x in range(new_surf.get_size()[0]):
            for y in range(new_surf.get_size()[1]):
                if new_surf.get_at((x, y))[0] != 0:
                    new_surf.set_at((x, y), "orange")
        screen.blit(new_surf, ship_rect)

    pygame.display.flip()
    clock.tick(60)
