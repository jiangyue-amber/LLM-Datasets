# Software Name: Animation_Creator
# Category: Graphics
# Description: Animation Creator is a graphics software application that allows users to create and edit animations. It provides a variety of tools and features for designing and animating characters, objects, and scenes. Users can easily create keyframes, adjust timing, and apply smooth transitions between frames. The software supports various animation techniques such as traditional frame-by-frame animation, skeletal animation, and motion capture. Users can also add special effects and sound to enhance their animations. Animation Creator offers a user-friendly interface with intuitive controls for easy animation creation and editing.

import sys
import os
import time
import math
import random

try:
    import pygame
    from pygame.locals import *
except ImportError:
    print("Pygame is required to run this program. Please install it.")
    sys.exit()

class AnimationCreator:
    def __init__(self, width=800, height=600, fps=30):
        pygame.init()
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Animation Creator")
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_frame = 0
        self.keyframes = {}
        self.selected_object = None # Example: could be a rectangle, circle, image etc.
        self.objects = []  # List of objects in the animation
        self.background_color = (255, 255, 255)  # White default background
        self.playback_speed = 1.0 # Normal speed
        self.is_playing = False
        self.animation_length = 100 # default length of animation in frames

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                elif event.key == K_SPACE:
                    self.is_playing = not self.is_playing
                elif event.key == K_LEFT:
                    self.current_frame = max(0, self.current_frame - 1)
                elif event.key == K_RIGHT:
                    self.current_frame = min(self.animation_length - 1, self.current_frame + 1)
                elif event.key == K_s and pygame.key.get_mods() & KMOD_CTRL:
                    self.save_animation()

            elif event.type == MOUSEBUTTONDOWN:
                # Example: Add a simple rectangle on click
                x, y = pygame.mouse.get_pos()
                rect = {"type": "rect", "x": x, "y": y, "width": 50, "height": 50, "color": (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))}
                self.objects.append(rect)
                self.keyframes[self.current_frame] = self.objects[:] # copy of the objects.
                self.selected_object = rect

            elif event.type == MOUSEBUTTONUP:
                 self.selected_object = None

            elif event.type == MOUSEMOTION:
                if self.selected_object:
                    x, y = pygame.mouse.get_pos()
                    self.selected_object['x'] = x
                    self.selected_object['y'] = y
                    if self.current_frame not in self.keyframes:
                        self.keyframes[self.current_frame] = self.objects[:]
                    else:
                        self.keyframes[self.current_frame] = self.objects[:]
    def update(self):
        if self.is_playing:
            self.current_frame = (self.current_frame + self.playback_speed) % self.animation_length
            self.current_frame = int(self.current_frame)

    def draw(self):
        self.screen.fill(self.background_color)

        # Interpolate between keyframes to get the object states for the current frame
        if self.keyframes:
            frame_objects = self.interpolate_frames(self.current_frame)
            for obj in frame_objects:
                if obj['type'] == 'rect':
                    pygame.draw.rect(self.screen, obj['color'], (obj['x'], obj['y'], obj['width'], obj['height']))
                #Add more object types (circles, images, etc.) here

        pygame.display.flip()

    def interpolate_frames(self, frame_number):
        # Find the keyframes before and after the current frame
        before_frame = -1
        after_frame = float('inf')
        before_objects = None
        after_objects = None

        sorted_frames = sorted(self.keyframes.keys())

        for i in range(len(sorted_frames)):
            if sorted_frames[i] <= frame_number:
                before_frame = sorted_frames[i]
                before_objects = self.keyframes[before_frame]

            if sorted_frames[i] >= frame_number and sorted_frames[i] < after_frame:
                after_frame = sorted_frames[i]
                after_objects = self.keyframes[after_frame]

        # If there's only one keyframe, return it
        if before_frame == after_frame:
            return before_objects

        # If the current frame is before the first keyframe or after the last, return the closest keyframe
        if before_frame == -1:
            return after_objects
        if after_frame == float('inf'):
            return before_objects

        # Interpolate the object properties between the two keyframes
        interpolation_factor = (frame_number - before_frame) / (after_frame - before_frame)
        interpolated_objects = []

        # Assuming the number and type of objects are consistent between keyframes
        # This needs more robust error handling and object matching in a real application
        if before_objects and after_objects and len(before_objects) == len(after_objects):
            for i in range(len(before_objects)):
                before_obj = before_objects[i]
                after_obj = after_objects[i]
                if before_obj['type'] == after_obj['type']:
                    if before_obj['type'] == 'rect':
                        x = before_obj['x'] + (after_obj['x'] - before_obj['x']) * interpolation_factor
                        y = before_obj['y'] + (after_obj['y'] - before_obj['y']) * interpolation_factor
                        width = before_obj['width']
                        height = before_obj['height'] # Assuming dimensions don't change during interpolation
                        color = before_obj['color'] # Assuming colours don't change
                        interpolated_obj = {'type': 'rect', 'x': x, 'y': y, 'width': width, 'height': height, 'color': color}
                        interpolated_objects.append(interpolated_obj)
                    #Add more object types to interpolate

        return interpolated_objects

    def save_animation(self):
        # Basic Save Functionality
        filename = "animation_data.txt"
        try:
             with open(filename, 'w') as file:
                file.write(str(self.keyframes))
             print(f"Animation saved to {filename}")
        except Exception as e:
             print(f"Error saving animation: {e}")

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    animation_creator = AnimationCreator()
    animation_creator.run()