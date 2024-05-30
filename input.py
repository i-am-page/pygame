import pygame, sys

SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1200

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

base_font = pygame.font.SysFont("monospace", 32)
user_text = "Hello World"
input = pygame.rect.Rect(600 - 100, 375 - 25, 200, 50)
color_active = pygame.Color("lightskyblue3")
color_passive = pygame.Color("gray15")
color = color_passive

active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input.collidepoint(event.pos):
                active = True
                color = color_active
            else:
                active = False
                color = color_passive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key ==pygame.K_RETURN:
                    user_text = "Checkmate"
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, input, 2)
    displayed_text = base_font.render(user_text, 1, (255, 255, 255))
    screen.blit(displayed_text, (input.x + 5, input.y + 10))
    input.w = max(220, displayed_text.get_width() + 10)

    pygame.display.flip()
    clock.tick(30)
