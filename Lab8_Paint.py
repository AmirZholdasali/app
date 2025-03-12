import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint - Enhanced")

# Colors
BACKGROUND_COLOR = (230, 230, 250)  # Лавандовый фон
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 69, 0)  # Ярко-красный
BLUE = (30, 144, 255)  # Королевский синий
GREEN = (0, 205, 102)  # Изумрудный зеленый
YELLOW = (255, 215, 0)  # Золотой
PURPLE = (147, 112, 219)  # Фиолетовый

# Canvas
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Color and mode settings
colors = {"red": RED, "blue": BLUE, "green": GREEN, "yellow": YELLOW, "purple": PURPLE, "erase": WHITE}
color = "red"
radius = 10
mouse_down = False
running = True
starting_position = None
last_position = None

mode_draw = "Draw"
mode_rect = "Rect"
mode_circle = "Circle"
mode = mode_draw  # Default mode

# Font for displaying current mode and color
font = pygame.font.SysFont("Arial", 18, bold=True)

# Main Loop
while running:
    screen.fill(BACKGROUND_COLOR)
    screen.blit(canvas, (0, 0))

    # Display current mode and color
    mode_text = font.render(f"Mode: {mode}", True, BLACK)
    color_text = font.render(f"Color: {color.capitalize()}", True, colors[color])
    screen.blit(mode_text, (10, 10))
    screen.blit(color_text, (10, 35))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change color or mode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = "red"
            elif event.key == pygame.K_g:
                color = "green"
            elif event.key == pygame.K_b:
                color = "blue"
            elif event.key == pygame.K_y:
                color = "yellow"
            elif event.key == pygame.K_p:
                color = "purple"
            elif event.key == pygame.K_e:
                color = "erase"
            elif event.key == pygame.K_c:
                canvas.fill(WHITE)
            elif event.key == pygame.K_1:
                mode = mode_draw
            elif event.key == pygame.K_2:
                mode = mode_circle
            elif event.key == pygame.K_3:
                mode = mode_rect

        # Mouse interactions
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
            starting_position = event.pos
            last_position = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
            if starting_position and mode in [mode_circle, mode_rect]:
                end_position = event.pos
                rect = pygame.Rect(
                    min(starting_position[0], end_position[0]),
                    min(starting_position[1], end_position[1]),
                    abs(end_position[0] - starting_position[0]),
                    abs(end_position[1] - starting_position[1])
                )
                if mode == mode_rect:
                    pygame.draw.rect(canvas, colors[color], rect, 4)  # Увеличенная толщина линии
                elif mode == mode_circle:
                    pygame.draw.ellipse(canvas, colors[color], rect, 4)  # Увеличенная толщина линии
        elif event.type == pygame.MOUSEMOTION and mouse_down:
            if mode == mode_draw:
                pygame.draw.line(canvas, colors[color], last_position, event.pos, radius * 2)
            last_position = event.pos

    pygame.display.flip()

pygame.quit()