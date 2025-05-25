import pygame
import os
from pygame.locals import *

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # Load coin sprites for animation
        self.sprites = [
            pygame.image.load(os.path.join('assets', 'images', 'coin1.png')).convert_alpha(),
            pygame.image.load(os.path.join('assets', 'images', 'coin2.png')).convert_alpha(),
            pygame.image.load(os.path.join('assets', 'images', 'coin3.png')).convert_alpha(),
            pygame.image.load(os.path.join('assets', 'images', 'coin4.png')).convert_alpha()
        ]
        
        # Initial sprite and rect
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Animation variables
        self.animation_index = 0
        self.animation_timer = 0
        self.animation_speed = 8  # frames per animation change
    
    def update(self):
        # Handle animation
        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.animation_index = (self.animation_index + 1) % len(self.sprites)
            self.image = self.sprites[self.animation_index]
    
    def draw(self, screen, camera_offset):
        screen.blit(self.image, (self.rect.x - camera_offset, self.rect.y))
