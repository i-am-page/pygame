import pygame, sys


SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1200

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.mouse.set_visible(False)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill("red")
        self.rect = self.image.get_rect(center=(300, 300))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        if pygame.sprite.spritecollide(self, alpha, False, pygame.sprite.collide_mask):  # type: ignore
            self.image.fill("yellow")
        else:
            self.image.fill("red")


class Alpha(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("alpha.png").convert_alpha()
        self.rect = self.image.get_rect(center=(400, 400))
        self.mask = pygame.mask.from_surface(self.image)


player = pygame.sprite.GroupSingle(Player())  # type: ignore
alpha = pygame.sprite.GroupSingle(Alpha())  # type: ignore


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    player.update()
    
    alpha.draw(screen)
    player.draw(screen)
    #mask.overlap() -> tuple() // mask.overlap_area() -> int
    if pygame.sprite.spritecollide(player.sprite, alpha, False):
        if pygame.sprite.spritecollide(player.sprite, alpha, False, pygame.sprite.collide_mask):  # type: ignore
            player.update()
        else:
            player.update()

    pygame.display.flip()
    clock.tick(60)
