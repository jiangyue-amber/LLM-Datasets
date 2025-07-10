# Software Name: Shape_Twist
# Category: Puzzle_Game
# Description: Shape Twist is a puzzle game where players have to rotate and flip geometric shapes to fit them into a given silhouette. Players are presented with a silhouette and a set of shapes, including squares, triangles, and circles. They need to manipulate the shapes by rotating and flipping them to find the correct orientation and placement that matches the silhouette.

import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shape Twist")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Shape definitions (example)
class Shape:
    def __init__(self, points, color):
        self.points = points
        self.color = color
        self.x = 0
        self.y = 0
        self.angle = 0
        self.flipped = False

    def draw(self, surface):
        rotated_points = self.rotate_points()
        translated_points = self.translate_points(rotated_points)
        pygame.draw.polygon(surface, self.color, translated_points)

    def rotate_points(self):
        rotated_points = []
        for x, y in self.points:
            rad = math.radians(self.angle)
            new_x = x * math.cos(rad) - y * math.sin(rad)
            new_y = x * math.sin(rad) + y * math.cos(rad)
            rotated_points.append((new_x, new_y))
        if self.flipped:
            rotated_points = [(x * -1, y) for x,y in rotated_points]
        return rotated_points

    def translate_points(self, points):
          return [(x + self.x, y + self.y) for x, y in points]

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, angle):
        self.angle += angle

    def flip(self):
        self.flipped = not self.flipped


# Example shapes
square_points = [(0, 0), (50, 0), (50, 50), (0, 50)]
triangle_points = [(0, 0), (50, 0), (25, 50)]
circle_center = (100, 100)
circle_radius = 25


square = Shape(square_points, red)
square.set_position(100, 100)

triangle = Shape(triangle_points, green)
triangle.set_position(300, 100)


# Silhouette (example - simple rectangle)
silhouette_rect = pygame.Rect(500, 100, 100, 100)


# Game loop
running = True
selected_shape = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            # Basic shape selection (improve with more robust collision detection)
            if square.x < mouse_x < square.x + 50 and square.y < mouse_y < square.y + 50:
                selected_shape = square
            elif triangle.x < mouse_x < triangle.x + 50 and triangle.y < mouse_y < triangle.y + 50:
                selected_shape = triangle
            else:
                selected_shape = None
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and selected_shape:
                selected_shape.rotate(15)
            if event.key == pygame.K_f and selected_shape:
                selected_shape.flip()
            if event.key == pygame.K_LEFT and selected_shape:
                selected_shape.x -= 10
            if event.key == pygame.K_RIGHT and selected_shape:
                selected_shape.x += 10
            if event.key == pygame.K_UP and selected_shape:
                selected_shape.y -= 10
            if event.key == pygame.K_DOWN and selected_shape:
                selected_shape.y += 10
    # Drawing
    screen.fill(white)

    # Draw silhouette
    pygame.draw.rect(screen, black, silhouette_rect, 2)

    # Draw shapes
    square.draw(screen)
    triangle.draw(screen)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()