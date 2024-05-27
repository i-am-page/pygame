import pygame, sys
import random

SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1200
TARGET_AMOUNT = 12


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, path) -> None:
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()
        self.gunshot_sound = pygame.mixer.Sound("gun_sound.mp3")

    def shoot(self):
        self.gunshot_sound.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self) -> None:
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, path, pos) -> None:
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = pos

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
current_time = 0
backgound = pygame.transform.scale(
    pygame.image.load("bg_blue.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)
)
pygame.mouse.set_visible(False)


crosshair_group = pygame.sprite.Group()
crosshair = Crosshair("crosshair.png")
crosshair_group.add(crosshair)


def create_targets():
    target_group = pygame.sprite.Group()
    while len(target_group) != TARGET_AMOUNT:
        x, y = random.randint(100, SCREEN_WIDTH - 100), random.randint(
            100, SCREEN_HEIGHT - 100
        )
        new_target = Target("target.png", (x, y))
        pygame.sprite.spritecollide(new_target, target_group, True)
        target_group.add(new_target)
    return target_group
target_group = create_targets()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
        if event.type == pygame.KEYDOWN:
            target_group = create_targets()
            

    current_time = pygame.time.get_ticks()
    screen.blit(backgound, (0, 0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    pygame.display.flip()
 

    clock.tick(60)
