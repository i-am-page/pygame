import pygame, sys

SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1200

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

rect1 = pygame.Rect(0, 0, 200, 200)
rect2 = pygame.Rect(600, 375, 200, 200)
rect1_speed = [5, 5]
rect2_speed = [5, 5]


def bouncing(rect1, rect2):
    global rect1_speed, rect2_speed
    pygame.draw.rect(screen, (255, 0, 0), rect1)
    pygame.draw.rect(screen, (0, 255, 0), rect2)

    rect1.x += rect1_speed[0]
    rect1.y += rect1_speed[1]

    rect2.x += rect2_speed[0]
    rect2.y += rect2_speed[1]

    if rect2.left <= 0 or rect2.right >= SCREEN_WIDTH:
        rect2_speed[0] *= -1
    if rect2.top <= 0 or rect2.bottom >= SCREEN_HEIGHT:
        rect2_speed[1] *= -1

    if rect1.left <= 0 or rect1.right >= SCREEN_WIDTH:
        rect1_speed[0] *= -1
    if rect1.top <= 0 or rect1.bottom >= SCREEN_HEIGHT:
        rect1_speed[1] *= -1

    collision_tolerance = 20

    if rect1.colliderect(rect2):
        if abs(rect1.top - rect2.bottom) <= collision_tolerance and rect1_speed[1] <= 0:
            rect1_speed[1] *= -1
            rect2_speed[1] *= -1
        if abs(rect1.bottom - rect2.top) <= collision_tolerance and rect1_speed[1] >= 0:
            rect1_speed[1] *= -1
            rect2_speed[1] *= -1
        if abs(rect1.left - rect2.right) <= collision_tolerance and rect1_speed[0] <= 0:
            rect1_speed[0] *= -1
            rect2_speed[0] *= -1
        if abs(rect1.right - rect2.left) <= collision_tolerance and rect1_speed[0] >= 0:
            rect1_speed[0] *= -1
            rect2_speed[0] *= -1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0, 0, 0))
    bouncing(rect1, rect2)
    pygame.display.flip()
    clock.tick(30)
