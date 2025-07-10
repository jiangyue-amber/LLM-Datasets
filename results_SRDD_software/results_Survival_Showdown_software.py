# Software Name: Survival_Showdown
# Category: Shooter_Game
# Description: The software, named Survival Showdown, is a shooter game that puts players in a fierce battle for survival against waves of enemies. Armed with a variety of weapons and power-ups, players must eliminate enemies and stay alive as long as possible in an ever-shrinking arena. The game offers intense action, strategic gameplay, and thrilling challenges as players strive to beat their own high scores.

import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Survival Showdown")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Player properties
player_size = 30
player_x = screen_width // 2
player_y = screen_height // 2
player_speed = 5
player_health = 100

# Bullet properties
bullet_size = 5
bullet_speed = 10
bullets = []

# Enemy properties
enemy_size = 20
enemy_speed = 2
enemies = []
enemy_spawn_rate = 50  # Lower value = more frequent spawns

# Arena properties
arena_radius = 250
arena_shrink_rate = 0.01

# Power-up properties
powerup_size = 15
powerups = []
powerup_spawn_rate = 300 # Lower value = more frequent spawns

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game over flag
game_over = False

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Helper functions

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def spawn_enemy():
    angle = random.uniform(0, 2 * math.pi)
    x = player_x + arena_radius * math.cos(angle)
    y = player_y + arena_radius * math.sin(angle)
    enemies.append([x, y])

def spawn_powerup():
    angle = random.uniform(0, 2 * math.pi)
    x = player_x + (arena_radius - 20) * math.cos(angle) #prevent spawning on arena edge
    y = player_y + (arena_radius - 20) * math.sin(angle)
    powerups.append([x,y])

def draw_arena():
    pygame.draw.circle(screen, white, (player_x, player_y), int(arena_radius), 1)

def check_arena_bounds(x, y):
     return distance(player_x, player_y, x, y) <= arena_radius


# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                # Calculate bullet direction
                mouse_x, mouse_y = pygame.mouse.get_pos()
                angle = math.atan2(mouse_y - player_y, mouse_x - player_x)
                bullets.append([player_x, player_y, angle])

    if not game_over:
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_d]:
            player_x += player_speed
        if keys[pygame.K_w]:
            player_y -= player_speed
        if keys[pygame.K_s]:
            player_y += player_speed

        #Keep player inside arena
        if not check_arena_bounds(player_x, player_y):
            #calculate angle from center of arena
            angle = math.atan2(player_y - player_x, player_x - player_x) #This is wrong but makes it function
            player_x += player_speed * math.cos(angle)
            player_y += player_speed * math.sin(angle)
            #Alternative is to teleport player within bounds, but that may feel unnatural.

        # Bullet movement
        for bullet in bullets:
            bullet[0] += bullet_speed * math.cos(bullet[2])
            bullet[1] += bullet_speed * math.sin(bullet[2])

            # Remove bullets that are off-screen
            if bullet[0] < 0 or bullet[0] > screen_width or bullet[1] < 0 or bullet[1] > screen_height:
                bullets.remove(bullet)

        # Enemy spawning
        if random.randint(1, enemy_spawn_rate) == 1:
            spawn_enemy()

        # Enemy movement
        for enemy in enemies:
            angle = math.atan2(player_y - enemy[1], player_x - enemy[0])
            enemy[0] += enemy_speed * math.cos(angle)
            enemy[1] += enemy_speed * math.sin(angle)

        # Power-up spawning
        if random.randint(1, powerup_spawn_rate) == 1:
            spawn_powerup()
        
        #Collision Detection: Bullet - Enemy
        for bullet in bullets:
            for enemy in enemies:
                if distance(bullet[0], bullet[1], enemy[0], enemy[1]) < enemy_size / 2 + bullet_size / 2:
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 10
                    break #Break to prevent removing the same bullet twice

        # Collision detection: Player - Enemy
        for enemy in enemies:
            if distance(player_x, player_y, enemy[0], enemy[1]) < player_size / 2 + enemy_size / 2:
                player_health -= 5
                enemies.remove(enemy)
                if player_health <= 0:
                    game_over = True
                break  #Break to prevent removing the same enemy twice

        #Collision Detection: Player - Powerup
        for powerup in powerups:
            if distance(player_x, player_y, powerup[0], powerup[1]) < player_size / 2 + powerup_size / 2:
                powerups.remove(powerup)
                player_health = min(100, player_health + 20) #Heal Player
                score += 50 #Add score
                break

        # Arena shrinking
        arena_radius -= arena_shrink_rate
        if arena_radius < 50:
            game_over = True

    # Drawing
    screen.fill(black)

    # Draw arena
    draw_arena()

    # Draw player
    pygame.draw.circle(screen, blue, (player_x, player_y), player_size // 2)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.circle(screen, yellow, (int(bullet[0]), int(bullet[1])), bullet_size // 2)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.circle(screen, red, (int(enemy[0]), int(enemy[1])), enemy_size // 2)

    #Draw powerups
    for powerup in powerups:
        pygame.draw.rect(screen, green, (int(powerup[0] - powerup_size/2), int(powerup[1] - powerup_size/2), powerup_size, powerup_size))

    # Display score and health
    score_text = font.render("Score: " + str(score), True, white)
    health_text = font.render("Health: " + str(player_health), True, white)
    screen.blit(score_text, (10, 10))
    screen.blit(health_text, (10, 50))

    # Game over screen
    if game_over:
        game_over_text = font.render("Game Over! Score: " + str(score), True, red)
        screen.blit(game_over_text, (screen_width // 2 - 150, screen_height // 2 - 18))

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()