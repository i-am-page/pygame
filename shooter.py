import pygame, sys
import random

SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1200
TARGET_AMOUNT = 12

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
current_time = 0
backgound = pygame.transform.scale(
    pygame.image.load("bg_blue.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)
)
pygame.mouse.set_visible(False)

title = "Western Gunner"
base_title = pygame.font.SysFont("monospace", 54)

start_text = "Start"
base_start_text = pygame.font.SysFont("monospace", 32)
start_rect = pygame.rect.Rect(600 - 100, 375 - 50, 200, 50)
quit_text = "Quit"
base_quit_text = pygame.font.SysFont("monospace", 32)
quit_rect = pygame.rect.Rect(600 - 90, 375 + 10, 180, 50)


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, path) -> None:
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()
        self.gunshot_sound = pygame.mixer.Sound("gun_sound.mp3")

    def shoot(self, target_group):
        self.gunshot_sound.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)
        if len(target_group)==0:
            game.new_stage()

    def update(self) -> None:
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, path, pos) -> None:
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = pos


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


class GameState:
    def __init__(self) -> None:
        self.state = "intro"
        self.target_group = create_targets()

    def new_stage(self):
        self.target_group = create_targets()
        self.main_stage()

    def main_stage(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rect.collidepoint(event.pos):
                    self.state = "intro"
                    quit_rect.center = (600 - 90, 375 + 10)
                crosshair.shoot(self.target_group)

        current_time = pygame.time.get_ticks()
        screen.blit(backgound, (0, 0))

        quit_rect.topleft = (0, 0)
        displayed_quit = base_quit_text.render(quit_text, 1, pygame.Color("red"))
        screen.blit(displayed_quit, (quit_rect.x + 40, quit_rect.y + 10))
        pygame.draw.rect(screen, pygame.color.Color("lightskyblue3"), quit_rect, 1)

        self.target_group.draw(screen)
        crosshair_group.draw(screen)
        crosshair_group.update()
        pygame.display.flip()

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    pygame.mixer.Sound("game_start.mp3").play()
                    self.state = "main_stage"
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        current_time = pygame.time.get_ticks()
        quit_rect.topleft =(600-90,375+10)
        screen.blit(backgound, (0, 0))
        displayed_title = base_title.render(title, 1, pygame.Color("red"))
        displayed_start = base_start_text.render(start_text, 1, pygame.Color("red"))
        displayed_quit = base_quit_text.render(quit_text, 1, pygame.Color("red"))
        screen.blit(displayed_title, (600 - 230, 375 - 250))
        screen.blit(displayed_start, (start_rect.x + 45, start_rect.y + 10))
        screen.blit(displayed_quit, (quit_rect.x + 40, quit_rect.y + 10))
        pygame.draw.rect(screen, pygame.color.Color("lightskyblue3"), start_rect, 1)
        pygame.draw.rect(screen, pygame.color.Color("lightskyblue3"), quit_rect, 1)
        crosshair_group.draw(screen)
        crosshair_group.update()
        pygame.display.flip()

    def stage_manager(self):
        if self.state == "main_stage":
            self.main_stage()
        if self.state == "intro":
            self.intro()


crosshair_group = pygame.sprite.Group()
crosshair = Crosshair("crosshair.png")
crosshair_group.add(crosshair)
game = GameState()


while True:
    game.stage_manager()
    clock.tick(60)
