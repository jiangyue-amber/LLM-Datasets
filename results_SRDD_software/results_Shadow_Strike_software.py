# Software Name: Shadow_Strike
# Category: Action_Game
# Description: Shadow Strike is an action game where players take on the role of a stealthy assassin infiltrating enemy bases. Players must complete missions by silently eliminating targets, avoiding detection, and overcoming security measures. The game features a variety of levels with increasing difficulty, challenging players to strategize their approach and make precise strikes. With realistic stealth mechanics, immersive gameplay, and stunning graphics, Shadow Strike offers a thrilling and intense action gaming experience.

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shadow Strike")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player properties
player_size = 32
player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT - player_size - 20
player_speed = 5

# Enemy properties
enemy_size = 32
enemy_speed = 2
enemies = []  # List to hold enemy positions (x, y, detected)

# Game variables
score = 0
game_over = False
stealth_mode = True
detection_radius = 100
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)

# Helper functions
def draw_player(x, y):
    pygame.draw.rect(screen, GREEN if stealth_mode else RED, (x, y, player_size, player_size))

def draw_enemy(x, y, detected):
    color = RED if detected else GRAY
    pygame.draw.rect(screen, color, (x, y, enemy_size, enemy_size))

def create_enemy():
    x = random.randint(0, SCREEN_WIDTH - enemy_size)
    y = random.randint(50, 200)
    enemies.append([x, y, False]) #x, y, detected

def enemy_detects_player(enemy_x, enemy_y, player_x, player_y):
    distance = ((enemy_x - player_x)**2 + (enemy_y - player_y)**2)**0.5
    return distance <= detection_radius

def display_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def display_game_over():
    text = font.render("Game Over! Press SPACE to restart", True, RED)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Reset game
            game_over = False
            score = 0
            player_x = SCREEN_WIDTH // 2 - player_size // 2
            enemies = []

    if not game_over:
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
            player_x += player_speed
        if keys[pygame.K_UP]:
            stealth_mode = True
        if keys[pygame.K_DOWN]:
            stealth_mode = False

        # Enemy logic
        if len(enemies) < 5:
            if random.randint(0, 100) < 2:
                create_enemy()

        for enemy in enemies:
            enemy[0] += enemy_speed
            if enemy[0] <= 0 or enemy[0] >= SCREEN_WIDTH - enemy_size:
                enemy_speed *= -1

            # Enemy detection
            if enemy_detects_player(enemy[0], enemy[1], player_x, player_y) and not stealth_mode:
                enemy[2] = True
                game_over = True
            else:
                enemy[2] = False

        # Check for game over (collision with detected enemy)
        for enemy in enemies:
            if enemy[2] and player_x < enemy[0] + enemy_size and player_x + player_size > enemy[0] and player_y < enemy[1] + enemy_size and player_y + player_size > enemy[1]:
                game_over = True
                break

        # Score update (simple example)
        score += 1

        # Drawing
        screen.fill(BLACK)
        draw_player(player_x, player_y)
        for enemy in enemies:
            draw_enemy(enemy[0], enemy[1], enemy[2])
        display_score()

    else:
        # Game over screen
        display_game_over()

    pygame.display.flip()
    clock.tick(60) #60 fps

pygame.quit()
sys.exit()