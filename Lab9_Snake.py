import pygame
import random
from sys import exit
import time

WIDTH, HEIGHT = (800, 600)
BLOCK_SIZE = 10
WALL_BLOCKS = 3
GAME_ICON = "snake.png"
GAME_TITLE = "Snake Game"
INITIAL_GAME_SPEED = 10
BACKGROUND_COLOR = (0, 0, 0)
INITIAL_APPLES = 3
INITIAL_SNAKE_LENGTH = 3
SIZE_X = WIDTH // BLOCK_SIZE - WALL_BLOCKS * 2
SIZE_Y = HEIGHT // BLOCK_SIZE - WALL_BLOCKS * 2
APPLE_COLOR = (191, 31, 31)
SUPER_APPLE_COLOR = (255, 255, 0)  # цвет супер яблок
APPLE_RADIUS = BLOCK_SIZE // 4
SUPER_APPLE_LIFETIME = 5  # время супер яблок
WALL_COLOR = (31, 31, 31)
TEXT_COLOR = (255, 255, 255)

# 
def main():
    screen, clock = initialize_pygame()
    game_state = initialize_game_state()
    last_super_apple_time = time.time()
    
    while game_state["program_running"]:
        current_time = time.time()
        handle_super_apple_timer(game_state, current_time)
        clock.tick(game_state["game_speed"])
        events = get_events()
        update_game_state(events, game_state)
        update_screen(screen, game_state)
    perform_shutdown()

# удаление СЯ
def handle_super_apple_timer(game_state, current_time):
    for apple in list(game_state["super_apples"]):
        x, y, creation_time = apple
        if current_time - creation_time > SUPER_APPLE_LIFETIME:
            game_state["super_apples"].remove(apple)

# Инициализация стостояния игры
def initialize_game_state():
    return {
        "program_running": True,
        "game_running": False,
        "game_paused": False,
        "game_speed": INITIAL_GAME_SPEED,
        "score": 0,
        "snake": [],
        "apples": [],       # Обычные яблоки(1 очка)
        "super_apples": [], # Супер яблоки (3 очка)
        "apple_eaten": False
    }

# Размещение обычных яблок
def place_apples(apples, game_state):
    for _ in range(apples):
        x = random.randint(0, SIZE_X - 1)
        y = random.randint(0, SIZE_Y - 1)
        while (x, y) in game_state["apples"] or (x, y) in game_state["snake"]:
            x = random.randint(0, SIZE_X - 1)
            y = random.randint(0, SIZE_Y - 1)
        game_state["apples"].append((x, y))

# Размещение супер яблок
def place_super_apple(game_state):
    x = random.randint(0, SIZE_X - 1)
    y = random.randint(0, SIZE_Y - 1)
    while (x, y) in game_state["apples"] or (x, y) in game_state["snake"]:
        x = random.randint(0, SIZE_X - 1)
        y = random.randint(0, SIZE_Y - 1)
    game_state["super_apples"].append((x, y, time.time()))

# Проверка поедания яблок
def check_apple_consumption(game_state):
    # Проверка обычных яблок
    for apple in list(game_state["apples"]):
        if apple == game_state["snake"][0]:
            game_state["apples"].remove(apple)
            game_state["apple_eaten"] = True
            game_state["score"] += 1
            game_state["game_speed"] = round(game_state["game_speed"] * 1.1)
            return

    # Проверка супер яблок
    for super_apple in list(game_state["super_apples"]):
        x, y, _ = super_apple
        if (x, y) == game_state["snake"][0]:
            game_state["super_apples"].remove(super_apple)
            game_state["apple_eaten"] = True
            game_state["score"] += 3
            game_state["game_speed"] = round(game_state["game_speed"] * 1.1)
            return

# Изменение состояния игры
def update_game_state(events, game_state):
    check_key_presses(events, game_state)
    if game_state["game_running"] and not game_state["game_paused"]:
        move_snake(game_state)
        check_collisions(game_state)
        check_apple_consumption(game_state)
        # 10% шанс появления супер-яблока каждую секунду
        if random.random() < 0.01:
            place_super_apple(game_state)

# Отрисовка яблок
def draw_apples(screen, apples, super_apples):
    # Обычные яблоки
    for apple in apples:
        x = apple[0] * BLOCK_SIZE + WALL_BLOCKS * BLOCK_SIZE
        y = apple[1] * BLOCK_SIZE + WALL_BLOCKS * BLOCK_SIZE
        rect = ((x, y), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, APPLE_COLOR, rect, border_radius=APPLE_RADIUS)
    
    # Супер яблоки
    for super_apple in super_apples:
        x, y, _ = super_apple
        x = x * BLOCK_SIZE + WALL_BLOCKS * BLOCK_SIZE
        y = y * BLOCK_SIZE + WALL_BLOCKS * BLOCK_SIZE
        pygame.draw.circle(screen, SUPER_APPLE_COLOR, 
                          (x + BLOCK_SIZE // 2, y + BLOCK_SIZE // 2), 
                          BLOCK_SIZE // 2)

# Запуск новой игры
def initialize_new_game(game_state):
    game_state["snake"] = []
    game_state["apples"] = []
    game_state["super_apples"] = []
    place_snake(INITIAL_SNAKE_LENGTH, game_state)
    place_apples(INITIAL_APPLES, game_state)
    game_state["direction"] = (1, 0)
    game_state["game_paused"] = False
    game_state["score"] = 0
    game_state["game_speed"] = INITIAL_GAME_SPEED
    game_state["apple_eaten"] = False

# Змея
def place_snake(length, game_state):
    x = SIZE_X // 2
    y = SIZE_Y // 2
    game_state["snake"] = [(x, y)]
    for i in range(1, length):
        game_state["snake"].append((x - i, y))

# Движение змеи
def move_snake(game_state):
    x = game_state["snake"][0][0] + game_state["direction"][0]
    y = game_state["snake"][0][1] + game_state["direction"][1]
    game_state["snake"].insert(0, (x, y))
    if not game_state["apple_eaten"]:
        game_state["snake"].pop()
    else:
        game_state["apple_eaten"] = False

# Проверка коллизии
def check_collisions(game_state):
    x, y = game_state["snake"][0]
    if (
        x < 0 or y < 0 or x >= SIZE_X or y >= SIZE_Y or
        len(game_state["snake"]) > len(set(game_state["snake"]))
    ):
        game_state["game_running"] = False

# Обработка событий
def check_key_presses(events, game_state):
    if "quit" in events:
        game_state["program_running"] = False
    elif not game_state["game_running"]:
        if "escape" in events:
            game_state["program_running"] = False
        elif "enter" in events:
            initialize_new_game(game_state)
            game_state["game_running"] = True
    elif game_state["game_paused"]:
        if "space" in events:
            game_state["game_paused"] = False
        elif "escape" in events:
            game_state["game_paused"] = False
            game_state["game_running"] = False
    else:
        if "escape" in events or "space" in events:
            game_state["game_paused"] = True
        if "up" in events:
            game_state["direction"] = (0, -1)
        if "down" in events:
            game_state["direction"] = (0, 1)
        if "left" in events:
            game_state["direction"] = (-1, 0)
        if "right" in events:
            game_state["direction"] = (1, 0)

# Получение событий от игрока
def get_events():
    events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            events.append("quit")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                events.append("up")
            elif event.key == pygame.K_DOWN:
                events.append("down")
            elif event.key == pygame.K_LEFT:
                events.append("left")
            elif event.key == pygame.K_RIGHT:
                events.append("right")
            elif event.key == pygame.K_SPACE:
                events.append("space")
            elif event.key == pygame.K_RETURN:
                events.append("enter")
            elif event.key == pygame.K_ESCAPE:
                events.append("escape")
    return events

# Обновление экрана
def update_screen(screen, game_state):
    screen.fill(BACKGROUND_COLOR)
    if not game_state["game_running"]:
        print_new_game_message(screen)
    elif game_state["game_paused"]:
        print_game_paused_message(screen)
    else:
        draw_apples(screen, game_state["apples"], game_state["super_apples"])
        draw_snake(screen, game_state["snake"])
    draw_walls(screen)
    print_score(screen, game_state["score"])
    pygame.display.flip()

# Отрисовка змеи
def draw_snake(screen, snake):
    for segment in snake:
        x = segment[0] * BLOCK_SIZE + WALL_BLOCKS * BLOCK_SIZE
        y = segment[1] * BLOCK_SIZE + WALL_BLOCKS * BLOCK_SIZE
        rect = ((x, y), (BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, (0, 255, 0), rect)

# Отрисовка стен
def draw_walls(screen):
    pygame.draw.rect(screen, WALL_COLOR, ((0, 0), (WIDTH, WALL_BLOCKS * BLOCK_SIZE)))
    pygame.draw.rect(screen, WALL_COLOR, ((0, 0), (WALL_BLOCKS * BLOCK_SIZE, HEIGHT)))
    pygame.draw.rect(screen, WALL_COLOR, ((0, HEIGHT - WALL_BLOCKS * BLOCK_SIZE), (WIDTH, HEIGHT)))
    pygame.draw.rect(screen, WALL_COLOR, ((WIDTH - WALL_BLOCKS * BLOCK_SIZE, 0), (WIDTH, HEIGHT)))

# Отображение счета
def print_score(screen, score):
    font = pygame.font.SysFont("Courier New", 24, bold=True)
    text = font.render("Score: " + str(score), True, TEXT_COLOR)
    text_rect = text.get_rect()
    text_rect.topleft = (WALL_BLOCKS * BLOCK_SIZE, 0)
    screen.blit(text, text_rect)

# Сообщение о паузе
def print_game_paused_message(screen):
    font = pygame.font.SysFont("Courier New", 24, bold=True)
    text = font.render("PAUSED", True, TEXT_COLOR)
    text2 = font.render("Press SPACE to resume", True, TEXT_COLOR)
    text3 = font.render("Press ESC to quit", True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    text2_rect = text2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    text3_rect = text3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(text, text_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)

# Сообщение о начале игры
def print_new_game_message(screen):
    font = pygame.font.SysFont("Courier New", 35, bold=True)
    font2 = pygame.font.SysFont("font/Pixeltype.ttf", 40, bold=False)
    text1 = font.render("Enter to start", True, TEXT_COLOR)
    text2 = font.render("Esc to leave", True, TEXT_COLOR)
    text3 = font2.render("SNAKE GAME", False, (31, 200, 31))
    text1_rect = text1.get_rect()
    text2_rect = text2.get_rect()
    text3_rect = text3.get_rect()
    text1_rect.topleft = (280, 300)
    text2_rect.topleft = (300, 400)
    text3_rect.topleft = (310, 200)
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)

# Выключение программы
def perform_shutdown():
    pygame.quit()
    exit()

# Запуск пайгейм
def initialize_pygame():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    icon = pygame.image.load(GAME_ICON)
    pygame.display.set_icon(icon)
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()
    return screen, clock

main()