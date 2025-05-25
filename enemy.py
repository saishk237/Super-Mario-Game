import pygame
import os
from pygame.locals import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_type="goomba"):
        super().__init__()
        
        self.enemy_type = enemy_type
        
        # Load enemy sprites
        if enemy_type == "goomba":
            self.sprites = [
                pygame.image.load(os.path.join('assets', 'images', 'goomba1.png')).convert_alpha(),
                pygame.image.load(os.path.join('assets', 'images', 'goomba2.png')).convert_alpha()
            ]
            self.squished_sprite = pygame.image.load(os.path.join('assets', 'images', 'goomba_squished.png')).convert_alpha()
        elif enemy_type == "koopa":
            self.sprites = [
                pygame.image.load(os.path.join('assets', 'images', 'koopa1.png')).convert_alpha(),
                pygame.image.load(os.path.join('assets', 'images', 'koopa2.png')).convert_alpha()
            ]
            self.squished_sprite = pygame.image.load(os.path.join('assets', 'images', 'koopa_shell.png')).convert_alpha()
        
        # Initial sprite and rect
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Animation variables
        self.animation_index = 0
        self.animation_timer = 0
        self.animation_speed = 10  # frames per animation change
        
        # Movement variables
        self.direction = -1  # -1 for left, 1 for right
        self.speed = 2 if enemy_type == "goomba" else 3  # Koopas are faster
        
        # State variables
        self.is_dead = False
        self.death_timer = 0
    
    def update(self, platforms, camera_offset):
        if self.is_dead:
            self.death_timer += 1
            if self.death_timer > 30:  # Remove after 30 frames
                self.kill()
            return
        
        # Only update enemies that are on screen or close to it
        if not (self.rect.x > camera_offset - 100 and self.rect.x < camera_offset + 900):
            return
        
        # Move enemy
        self.rect.x += self.direction * self.speed
        
        # Check for platform edges to change direction
        self.check_platform_edges(platforms)
        
        # Handle animation
        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.animation_index = (self.animation_index + 1) % len(self.sprites)
            self.image = self.sprites[self.animation_index]
    
    def check_platform_edges(self, platforms):
        # Check if the enemy is about to walk off a platform
        edge_check = pygame.Rect(self.rect.x + self.direction * self.speed, self.rect.y + 5, self.rect.width, 5)
        
        platform_ahead = False
        for platform in platforms:
            if platform.rect.colliderect(edge_check):
                platform_ahead = True
                break
        
        # If no platform ahead, change direction
        if not platform_ahead:
            self.direction *= -1
            # Move away from the edge
            self.rect.x += self.direction * self.speed
        
        # Check for collisions with platforms on the sides
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # Left collision
                if self.direction > 0:
                    self.rect.right = platform.rect.left
                    self.direction = -1
                # Right collision
                elif self.direction < 0:
                    self.rect.left = platform.rect.right
                    self.direction = 1
    
    def die(self):
        self.is_dead = True
        self.image = self.squished_sprite
        self.rect.y += self.rect.height - self.squished_sprite.get_height()
        self.rect.height = self.squished_sprite.get_height()
    
    def draw(self, screen, camera_offset):
        # Flip the sprite based on direction if not dead
        if not self.is_dead and self.direction > 0:
            flipped_image = pygame.transform.flip(self.image, True, False)
            screen.blit(flipped_image, (self.rect.x - camera_offset, self.rect.y))
        else:
            screen.blit(self.image, (self.rect.x - camera_offset, self.rect.y))
