import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Red Ball Game")

clock = pygame.time.Clock()

ball_surf = pygame.Surface((50, 50), pygame.SRCALPHA)
pygame.draw.circle(ball_surf, (255, 0, 0), (25, 25), 25)

x, y = 255, 255

while True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 20
    if pressed[pygame.K_DOWN]: y += 20
    if pressed[pygame.K_LEFT]: x -= 20
    if pressed[pygame.K_RIGHT]: x += 20

    x = max(0, min(x, 450))
    y = max(0, min(y, 450))


    screen.blit(ball_surf, (x, y))

    clock.tick(60)

    pygame.display.update()
    