import pygame, sys


SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1200

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.mouse.set_visible(False)


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

    def update(self, pos):
        self.rect.center = pos

    def shoot(self):
        return Bullet(self.rect.center)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = pygame.Surface((50, 10))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.rect.x += 15

        if self.rect.x > SCREEN_WIDTH + 100:
            self.kill()
        if self.rect.x < 0 - 100:
            self.kill()


player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
bullet_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.shoot())

    screen.fill((0, 0, 0))
    bullet_group.draw(screen)
    player_group.draw(screen)
    bullet_group.update()
    player_group.update(pygame.mouse.get_pos())

    pygame.display.flip()
    clock.tick(60)
