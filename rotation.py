import pygame,sys


SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1200

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

image = pygame.image.load("kingkong.png")
#image = pygame.Surface((200,200))
#image.fill((255,0,0))
image_rect = image.get_rect(center = (600,375))
angle = 1

def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface, angle,2)
    rotated_surface_rect = rotated_surface.get_rect(center = (600,375))
    return rotated_surface,rotated_surface_rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    angle+=-3
    screen.fill((0,0,0))
    rotated_img, rotated_img_rect = rotate(image,angle)

    screen.blit(rotated_img,rotated_img_rect)
    pygame.display.flip()
    clock.tick(30)