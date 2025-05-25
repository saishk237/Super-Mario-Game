import pygame
import os
from pygame.locals import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, platform_type="ground"):
        super().__init__()
        
        self.platform_type = platform_type
        
        # Load platform sprites based on type
        if platform_type == "ground":
            self.image = pygame.image.load(os.path.join('assets', 'images', 'ground_tile.png')).convert_alpha()
        elif platform_type == "brick":
            self.image = pygame.image.load(os.path.join('assets', 'images', 'brick_tile.png')).convert_alpha()
        elif platform_type == "pipe":
            self.image = pygame.image.load(os.path.join('assets', 'images', 'pipe_tile.png')).convert_alpha()
        
        # Create a surface for the platform with the correct size
        self.width = width
        self.height = height
        
        # Create a rect for collision detection
        self.rect = pygame.Rect(x, y, width, height)
        
        # Store original image for tiling
        self.original_image = self.image
    
    def draw(self, screen, camera_offset):
        # For small platforms, just draw the image
        if self.width <= self.original_image.get_width() and self.height <= self.original_image.get_height():
            screen.blit(self.original_image, (self.rect.x - camera_offset, self.rect.y))
        else:
            # For larger platforms, tile the image properly to avoid distortion
            tile_width = self.original_image.get_width()
            tile_height = self.original_image.get_height()
            
            # Calculate how many complete tiles we need
            x_tiles = self.width // tile_width
            y_tiles = self.height // tile_height
            
            # Calculate the remaining partial tiles
            x_remainder = self.width % tile_width
            y_remainder = self.height % tile_height
            
            # Draw complete tiles
            for x in range(x_tiles):
                for y in range(y_tiles):
                    screen.blit(self.original_image, 
                               (self.rect.x + x * tile_width - camera_offset, 
                                self.rect.y + y * tile_height))
            
            # Draw partial tiles on right edge
            if x_remainder > 0:
                for y in range(y_tiles):
                    screen.blit(self.original_image, 
                               (self.rect.x + x_tiles * tile_width - camera_offset, 
                                self.rect.y + y * tile_height),
                               (0, 0, x_remainder, tile_height))
            
            # Draw partial tiles on bottom edge
            if y_remainder > 0:
                for x in range(x_tiles):
                    screen.blit(self.original_image, 
                               (self.rect.x + x * tile_width - camera_offset, 
                                self.rect.y + y_tiles * tile_height),
                               (0, 0, tile_width, y_remainder))
            
            # Draw partial tile at bottom-right corner
            if x_remainder > 0 and y_remainder > 0:
                screen.blit(self.original_image, 
                           (self.rect.x + x_tiles * tile_width - camera_offset, 
                            self.rect.y + y_tiles * tile_height),
                           (0, 0, x_remainder, y_remainder))
