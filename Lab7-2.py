import pygame
from sys import exit
from mutagen.mp3 import MP3
pygame.init()

#Бар-ползунок
def get_music_length(filename):
    #получение длительности трека в секундах
    audio = MP3(filename)
    return audio.info.length

def draw_progress_bar():
    #рисунок ползунка
    if pygame.mixer.music.get_busy():  #если музыка играет
        current_time = pygame.mixer.music.get_pos() / 1000  # в секундах
        total_time = song_durations[current_song]
        progress = current_time / total_time  # Ддля проигранного времени

        bar_width = 200  # Ширина полоски
        bar_x = 50 
        bar_y = 350

        pygame.draw.rect(screen, (100, 100, 100), (bar_x, bar_y, bar_width, 5))  # Серый фон
        pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, int(bar_width * progress), 5))  # Белая заполненная часть

#Музка, переключение
def play_music(index):
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()

#Пауза
def draw_pause_button():
    if paused:
        # Кнопка воспроизведения
        pygame.draw.circle(screen, (255, 255, 255), (150, 400), 30)
        pygame.draw.polygon(screen, (0, 0, 0), [(140, 390), (140, 415), (165, 402.5)])
    else:
        # Кнопка паузы
        pygame.draw.circle(screen, (255, 255, 255), (150, 400), 30)
        pygame.draw.rect(screen, (0, 0, 0), (136, 390, 8, 25))
        pygame.draw.rect(screen, (0, 0, 0), (155, 390, 8, 25))


screen = pygame.display.set_mode((300, 500))
pygame.display.set_caption('MP3 Player')
screen.fill((30, 215, 96))

font = pygame.font.Font(None, 20)
font_2 = pygame.font.Font(None, 25)

music_1 = "music/Queen - Don't Stop Me Now.mp3"
music_2 = "music/The Beatles - Yesterday.mp3"
music_3 = "music/ACDC - Back In Black.mp3"
music_4 = "music/The Rolling Stones - Paint It, Black.mp3"
music_5 = 'music/Led Zeppelin - Stairway To Heaven.mp3'

music_1_cover = pygame.image.load("graphics/Queen_Jazz.png")
music_2_cover = pygame.image.load("graphics/Help!_ Beatles.jpg")
music_3_cover = pygame.image.load("graphics/Back in Black_ acdc.png")
music_4_cover = pygame.image.load("graphics/Aftermath_ RS.jpg")
music_5_cover = pygame.image.load("graphics/Led Zeppelin 4.jpg")

pygame.draw.circle(screen, (255, 255, 255), (150, 400), 30)
pygame.draw.polygon(screen, (255, 255, 255), [(215, 390), (215, 415), (240, 402.5)])
pygame.draw.rect(screen, (255, 255, 255), (240, 390, 8, 25))
pygame.draw.polygon(screen, (255, 255, 255), [(85, 390), (85, 415), (60, 402.5)])
pygame.draw.rect(screen, (255, 255, 255), (52, 390, 8, 25))
skip_right = font_2.render("->", False, (255, 255, 255))
skip_left = font_2.render("<-", False, (255, 255, 255))
# pygame.draw.rect(screen, (0, 0, 0), (50, 40, 200, 200))

playlist = [music_1, music_2, music_3, music_4, music_5]
song_durations = [get_music_length(song) for song in playlist]
albumlist = [music_1_cover, music_2_cover, music_3_cover, music_4_cover, music_5_cover]
current_song = 0
play_music(current_song)
paused = False

song_names = [
    "Queen - Don't Stop Me Now",
    "The Beatles - Yesterday",
    "AC/DC - Back In Black",
    "The Rolling Stones - Paint It, Black",
    "Led Zeppelin - Stairway To Heaven"
]


space_surface = font.render("SPACE", False, (255, 255, 255))
song_surface = font.render(song_names[current_song], False, (64, 64, 64))
screen.blit(albumlist[current_song], (40, 40, 200, 200))


while True:

    screen.blit(space_surface, (128, 435))
    screen.blit(skip_left, (60, 430))
    screen.blit(skip_right, (220, 430))
    screen.blit(song_surface, (40, 280))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                current_song = (current_song +1) % len(playlist)
                paused = False

                play_music(current_song)
                song_surface = font.render(song_names[current_song], False, (64, 64, 64))
                pygame.draw.rect(screen, (30, 215, 96), (0, 0, 300, 300))
                screen.blit(albumlist[current_song], (50, 40, 200, 200))
                

            if event.key == pygame.K_RIGHT:
                current_song = (current_song -1) % len(playlist)
                paused = False

                play_music(current_song)
                song_surface = font.render(song_names[current_song], False, (64, 64, 64))
                pygame.draw.rect(screen, (30, 215, 96), (0, 0, 300, 300))
                screen.blit(albumlist[current_song], (50, 40, 200, 200))

            if event.key == pygame.K_SPACE:

                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
        
        draw_pause_button()

    draw_pause_button()

    draw_progress_bar()

    pygame.display.update()