import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Falling Objects")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (255, 0, 0)

player_width = 50
player_height = 50
player_x = screen_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Objek yang jatuh
falling_width = 30
falling_height = 30
falling_speed = 5

# Skor
score = 0
font = pygame.font.SysFont(None, 30)

# Fungsi untuk menampilkan skor
def show_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Loop utama game
running = True
clock = pygame.time.Clock()

falling_x = random.randint(0, screen_width - falling_width)
falling_y = -falling_height

while running:
    screen.fill(WHITE)
    
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Kontrol pemain
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
    
    # Membuat objek jatuh
    falling_y += falling_speed
    if falling_y > screen_height:
        falling_y = -falling_height
        falling_x = random.randint(0, screen_width - falling_width)
    
    # Menangkap objek
    if player_x < falling_x + falling_width and player_x + player_width > falling_x:
        if player_y < falling_y + falling_height and player_y + player_height > falling_y:
            score += 1
            falling_y = -falling_height
            falling_x = random.randint(0, screen_width - falling_width)

    # Menampilkan karakter pemain dan objek yang jatuh
    pygame.draw.rect(screen, BLUE, (falling_x, falling_y, falling_width, falling_height))
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))
    
    # Menampilkan skor
    show_score(score)

    # Update tampilan
    pygame.display.update()
    
    # Menentukan kecepatan game
    clock.tick(60)

# Keluar dari game
pygame.quit()