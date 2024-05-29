import pygame, sys
from PIL import Image

pygame.init()
clock = pygame.time.Clock()

SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1200
SCALE_FACTOR = (SCREEN_WIDTH / 10, SCREEN_HEIGHT / 10)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Animation")


def gif_to_png(gif_path, output_path):
    img = Image.open(gif_path)
    if img.is_animated:
        for i in range(img.n_frames):
            img.seek(i)
            img.save(f"{output_path}/frame_{i}.png")
    else:
        img.save(f"{output_path}/image.png")


gif_to_png("frog_atk.gif", "frogs")


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, path, animating=False):
        super().__init__()
        self.cur_index = 0
        self.is_animating = animating
        self.frames = []
        self.frames.append(
            pygame.transform.scale(pygame.image.load("frogs/frame_0.png"), SCALE_FACTOR)
        )
        self.frames.append(
            pygame.transform.scale(pygame.image.load("frogs/frame_1.png"), SCALE_FACTOR)
        )
        self.frames.append(
            pygame.transform.scale(pygame.image.load("frogs/frame_2.png"), SCALE_FACTOR)
        )
        self.frames.append(
            pygame.transform.scale(pygame.image.load("frogs/frame_3.png"), SCALE_FACTOR)
        )
        self.frames.append(
            pygame.transform.scale(pygame.image.load("frogs/frame_4.png"), SCALE_FACTOR)
        )
        self.frames.append(
            pygame.transform.scale(pygame.image.load("frogs/frame_5.png"), SCALE_FACTOR)
        )
        self.frames.append(
            pygame.transform.scale(pygame.image.load("frogs/frame_6.png"), SCALE_FACTOR)
        )
        self.frames.append(
            pygame.transform.scale(pygame.image.load("frogs/frame_7.png"), SCALE_FACTOR)
        )
        self.frames.append(
            pygame.transform.scale(pygame.image.load("frogs/frame_8.png"), SCALE_FACTOR)
        )
        self.frames.append(
            pygame.transform.scale(pygame.image.load("frogs/frame_9.png"), SCALE_FACTOR)
        )

        self.image = self.frames[self.cur_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def animate(self):
        self.is_animating = True

    def update(self, speed):
        if self.is_animating:
            self.cur_index += speed
            if self.cur_index == 9:
                self.cur_index = 0
                self.is_animating = False
            self.image = self.frames[int(self.cur_index)]


moving_sprites = pygame.sprite.Group()
player = Player((100, 100), "frog_atk.gif")
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.animate()

    screen.fill((255, 255, 255))
    moving_sprites.draw(screen)
    moving_sprites.update(0.3)
    pygame.display.flip()
    clock.tick(60)
