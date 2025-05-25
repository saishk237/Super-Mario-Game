import pygame
import os
from pygame.locals import *
from .coin import Coin

class QuestionBlock(pygame.sprite.Sprite):
    def __init__(self, x, y, content="coin"):
        super().__init__()
        
        # Load block sprites
        self.sprites = {
            'active': pygame.image.load(os.path.join('assets', 'images', 'question_block.png')).convert_alpha(),
            'inactive': pygame.image.load(os.path.join('assets', 'images', 'question_block_inactive.png')).convert_alpha()
        }
        
        # Initial sprite and rect
        self.image = self.sprites['active']
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Block properties
        self.content = content  # What comes out when hit: "coin", "mushroom", etc.
        self.is_active = True
        self.hit_animation = False
        self.hit_timer = 0
        self.original_y = y
    
    def update(self):
        # Handle hit animation
        if self.hit_animation:
            self.hit_timer += 1
            
            # Move up then back down
            if self.hit_timer < 5:
                self.rect.y -= 2
            elif self.hit_timer < 10:
                self.rect.y += 2
            else:
                self.hit_animation = False
                self.hit_timer = 0
                self.rect.y = self.original_y
    
    def hit(self):
        if self.is_active:
            self.is_active = False
            self.hit_animation = True
            self.image = self.sprites['inactive']
            
            # Return the content type so the game can create the appropriate object
            return self.content
        return None
    
    def draw(self, screen, camera_offset):
        screen.blit(self.image, (self.rect.x - camera_offset, self.rect.y))
