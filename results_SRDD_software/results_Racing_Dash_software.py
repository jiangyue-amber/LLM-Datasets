# Software Name: Racing_Dash
# Category: Racing_Game
# Description: Racing Dash is a racing game software that offers an immersive and adrenaline-pumping experience with high-speed races on city streets. Players can choose from a variety of sleek and powerful street racing cars and compete in thrilling races against AI opponents. The objective is to outmaneuver opponents, navigate through traffic, and reach the finish line first. The game features realistic physics, stunning graphics, and responsive controls to provide an exhilarating racing experience.

import pygame
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Dash")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# Car dimensions
CAR_WIDTH = 40
CAR_HEIGHT = 60

# Player car starting position
player_x = WIDTH // 2 - CAR_WIDTH // 2
player_y = HEIGHT - CAR_HEIGHT - 20
player_speed = 5

# Opponent car
opponent_width = 40
opponent_height = 60
opponent_x = random.randint(0, WIDTH - opponent_width)
opponent_y = -opponent_height
opponent_speed = 3

# Road settings
road_width = 300
road_x = WIDTH // 2 - road_width // 2

# Game loop
running = True
clock = pygame.time.Clock()

# Score
score = 0
font = pygame.font.Font(None, 36)

def draw_car(x, y, color):
    pygame.draw.rect(screen, color, (x, y, CAR_WIDTH, CAR_HEIGHT))

def draw_opponent(x, y):
    pygame.draw.rect(screen, RED, (x, y, opponent_width, opponent_height))

def display_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over():
    text = font.render("Game Over! Press any key to restart.", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                waiting = False

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > road_x:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < road_x + road_width - CAR_WIDTH:
        player_x += player_speed

    # Opponent movement
    opponent_y += opponent_speed
    if opponent_y > HEIGHT:
        opponent_x = random.randint(road_x, road_x + road_width - opponent_width)
        opponent_y = -opponent_height
        score += 10

    # Collision detection
    if player_x < opponent_x + opponent_width and player_x + CAR_WIDTH > opponent_x and player_y < opponent_y + opponent_height and player_y + CAR_HEIGHT > opponent_y:
        game_over()
        player_x = WIDTH // 2 - CAR_WIDTH // 2
        player_y = HEIGHT - CAR_HEIGHT - 20
        opponent_x = random.randint(0, WIDTH - opponent_width)
        opponent_y = -opponent_height
        score = 0

    # Drawing
    screen.fill(GRAY)
    pygame.draw.rect(screen, BLACK, (road_x, 0, road_width, HEIGHT))  # Road
    draw_car(player_x, player_y, WHITE)  # Player car
    draw_opponent(opponent_x, opponent_y) # Opponent car
    display_score(score)

    # Update display
    pygame.display.update()

    # Frame rate
    clock.tick(60)

pygame.quit()