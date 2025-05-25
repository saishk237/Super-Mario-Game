import pygame
import os
from pygame.locals import *
from ..utils.constants import GRAVITY, FRICTION, PLAYER_ACCELERATION, PLAYER_MAX_SPEED, PLAYER_JUMP_POWER

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # Load player sprites
        self.sprites = {
            'idle': pygame.image.load(os.path.join('assets', 'images', 'player_idle.png')).convert_alpha(),
            'run': [
                pygame.image.load(os.path.join('assets', 'images', 'player_run1.png')).convert_alpha(),
                pygame.image.load(os.path.join('assets', 'images', 'player_run2.png')).convert_alpha(),
                pygame.image.load(os.path.join('assets', 'images', 'player_run3.png')).convert_alpha()
            ],
            'jump': pygame.image.load(os.path.join('assets', 'images', 'player_jump.png')).convert_alpha(),
            'death': pygame.image.load(os.path.join('assets', 'images', 'player_death.png')).convert_alpha()
        }
        
        # Initial sprite and rect
        self.image = self.sprites['idle']
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Animation variables
        self.animation_index = 0
        self.animation_timer = 0
        self.animation_speed = 5  # frames per animation change
        self.facing_right = True
        
        # Physics variables
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration = PLAYER_ACCELERATION
        self.friction = FRICTION
        self.gravity = GRAVITY
        self.jump_power = PLAYER_JUMP_POWER
        self.max_speed = PLAYER_MAX_SPEED
        
        # State variables
        self.is_jumping = False
        self.is_dead = False
        self.invincible = False
        self.invincible_timer = 0
        self.coin_collected = False
        self.enemy_killed = False
        self.death_animation_timer = 0
    
    def update(self, platforms, enemies, coins, question_blocks):
        if self.is_dead:
            self.death_animation()
            return
        
        self.handle_input()
        self.apply_physics()
        self.handle_animation()
        
        # Check collisions
        self.check_platform_collisions(platforms)
        self.check_enemy_collisions(enemies)
        self.check_coin_collisions(coins)
        self.check_question_block_collisions(question_blocks)
        
        # Handle invincibility timer
        if self.invincible:
            self.invincible_timer -= 1
            if self.invincible_timer <= 0:
                self.invincible = False
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
        
        # Horizontal movement
        if keys[K_LEFT]:
            self.velocity_x -= self.acceleration
            self.facing_right = False
        elif keys[K_RIGHT]:
            self.velocity_x += self.acceleration
            self.facing_right = True
        else:
            # Apply friction when no movement keys are pressed
            if self.velocity_x > 0:
                self.velocity_x -= self.friction
                if self.velocity_x < 0:
                    self.velocity_x = 0
            elif self.velocity_x < 0:
                self.velocity_x += self.friction
                if self.velocity_x > 0:
                    self.velocity_x = 0
    
    def apply_physics(self):
        # Limit horizontal speed
        if self.velocity_x > self.max_speed:
            self.velocity_x = self.max_speed
        elif self.velocity_x < -self.max_speed:
            self.velocity_x = -self.max_speed
        
        # Apply gravity
        self.velocity_y += self.gravity
        
        # Update position
        self.rect.x += int(self.velocity_x)
        self.rect.y += int(self.velocity_y)
        
        # Check if player fell off the screen
        if self.rect.y > 600:  # Screen height
            self.die()
    
    def jump(self):
        if not self.is_jumping:
            self.velocity_y = self.jump_power
            self.is_jumping = True
    
    def check_platform_collisions(self, platforms):
        # Store the previous y position
        previous_y = self.rect.y - int(self.velocity_y)
        
        # Check for collisions with platforms
        platform_hits = pygame.sprite.spritecollide(self, platforms, False)
        for platform in platform_hits:
            # Collision from above (player landing on platform)
            if self.velocity_y > 0 and previous_y < platform.rect.top:
                self.rect.bottom = platform.rect.top
                self.velocity_y = 0
                self.is_jumping = False
            # Collision from below (player hitting platform from below)
            elif self.velocity_y < 0 and previous_y > platform.rect.bottom:
                self.rect.top = platform.rect.bottom
                self.velocity_y = 0
            # Collision from the sides
            else:
                # Left collision
                if self.velocity_x > 0:
                    self.rect.right = platform.rect.left
                    self.velocity_x = 0
                # Right collision
                elif self.velocity_x < 0:
                    self.rect.left = platform.rect.right
                    self.velocity_x = 0
    
    def check_enemy_collisions(self, enemies):
        if self.invincible:
            return
            
        enemy_hits = pygame.sprite.spritecollide(self, enemies, False)
        for enemy in enemy_hits:
            # If player is falling and hits enemy from above
            if self.velocity_y > 0 and self.rect.bottom < enemy.rect.top + 10:
                enemy.die()
                self.velocity_y = self.jump_power * 0.6  # Bounce off enemy
                self.enemy_killed = True
            else:
                # Player gets hit by enemy
                self.die()
    
    def check_coin_collisions(self, coins):
        coin_hits = pygame.sprite.spritecollide(self, coins, True)
        if coin_hits:
            self.coin_collected = True
    
    def check_question_block_collisions(self, question_blocks):
        # Store the previous y position
        previous_y = self.rect.y - int(self.velocity_y)
        
        block_hits = pygame.sprite.spritecollide(self, question_blocks, False)
        for block in block_hits:
            # Hit block from below
            if self.velocity_y < 0 and previous_y > block.rect.bottom:
                self.rect.top = block.rect.bottom
                self.velocity_y = 0
                block.hit()
    
    def handle_animation(self):
        self.animation_timer += 1
        
        # Determine which animation to use
        if self.is_jumping:
            self.image = self.sprites['jump']
        elif abs(self.velocity_x) > 0.5:  # Running
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.animation_index = (self.animation_index + 1) % len(self.sprites['run'])
            self.image = self.sprites['run'][self.animation_index]
        else:  # Idle
            self.image = self.sprites['idle']
        
        # Flip image if facing left
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
        
        # Flash when invincible
        if self.invincible and self.animation_timer % 4 < 2:
            # Create a copy of the image and change its alpha
            alpha_img = self.image.copy()
            alpha_img.set_alpha(128)
            self.image = alpha_img
    
    def death_animation(self):
        self.death_animation_timer += 1
        self.image = self.sprites['death']
        
        # Simple death animation: rise up then fall down
        if self.death_animation_timer < 15:
            self.rect.y -= 5
        else:
            self.rect.y += 10
    
    def die(self):
        self.is_dead = True
        self.velocity_x = 0
        self.velocity_y = 0
        self.death_animation_timer = 0
    
    def respawn(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.is_dead = False
        self.is_jumping = False
        self.invincible = True
        self.invincible_timer = 60  # Invincible for 60 frames
    
    def draw(self, screen, camera_offset):
        screen.blit(self.image, (self.rect.x - camera_offset, self.rect.y))
