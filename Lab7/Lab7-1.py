import pygame
from sys import exit
from datetime import datetime
pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Mickey Mouse Clock")

clock_img = pygame.image.load("graphics/clock.jpeg")
clock_img = pygame.transform.scale(clock_img, (600, 500))
left_hand = pygame.image.load("graphics/lefthand.png").convert_alpha()
right_hand = pygame.image.load("graphics/righthand.png").convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    now = datetime.now()
    angle_min = -now.minute *6
    angle_sec = -now.second *6

    rotated_left = pygame.transform.rotate(left_hand, angle_sec)
    rotated_right = pygame.transform.rotate(right_hand, angle_min)

    left_rect = rotated_left.get_rect(center=(300, 250))
    right_rect = rotated_right.get_rect(center=(300, 250))

    screen.fill((255, 255, 255))
    screen.blit(clock_img, (0, 0))
    screen.blit(rotated_left, left_rect)
    screen.blit(rotated_right, right_rect)

    pygame.display.update()
