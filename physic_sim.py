import pygame, sys, pymunk

SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1200

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
space = pymunk.Space()
space.gravity = (0,500)

def create_apple(space):
    body = pymunk.Body(2,100,pymunk.Body.DYNAMIC)
    body.position = (200,200)
    shape = pymunk.Circle(body,80)
    space.add(body, shape)
    return shape

def draw_apples(apples):
    for apple in apples:
        x_pos = int(apple.body.position.x)
        y_pos = int(apple.body.position.y)
        pygame.draw.circle(screen, (0,255,0),(x_pos,y_pos),80)

def create_static_ball(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (150,600)
    shape = pymunk.Circle(body,80)
    space.add(body,shape)
    return shape

def draw_static_ball(balls):
    for ball in balls:
        x_pos = int(ball.body.position.x)
        y_pos = int(ball.body.position.y)
        pygame.draw.circle(screen, (0,0,255),(x_pos,y_pos),80)

apples = []
apples.append(create_apple(space))

balls = []
balls.append(create_static_ball(space))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

    screen.fill((0, 0, 0))
    draw_apples(apples)
    draw_static_ball(balls)
    space.step(1/50)
    pygame.display.flip()
    clock.tick(30)
