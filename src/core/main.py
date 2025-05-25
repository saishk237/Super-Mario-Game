import pygame
import sys
import os
from pygame.locals import *

# Import game modules
from ..entities.player import Player
from ..entities.enemy import Enemy
from ..entities.platform_tile import Platform
from ..entities.coin import Coin
from ..entities.question_block import QuestionBlock
from .level_manager import LevelManager
from ..ui.game_ui import GameUI
from ..utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE, SKY_BLUE, INITIAL_LIVES

# Initialize pygame
pygame.init()
pygame.mixer.init()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.level_manager = LevelManager()
        self.ui = GameUI()
        
        # Load background music
        pygame.mixer.music.load(os.path.join('assets', 'sounds', 'background_music.wav'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # Loop indefinitely
        
        # Load sound effects
        self.jump_sound = pygame.mixer.Sound(os.path.join('assets', 'sounds', 'jump.wav'))
        self.coin_sound = pygame.mixer.Sound(os.path.join('assets', 'sounds', 'coin.wav'))
        self.death_sound = pygame.mixer.Sound(os.path.join('assets', 'sounds', 'death.wav'))
        
        # Game state
        self.score = 0
        self.lives = INITIAL_LIVES
        self.current_level = 1
        self.game_over = False
        
        # Initialize the first level
        self.load_level(self.current_level)
    
    def load_level(self, level_number):
        # Reset level-specific variables
        self.camera_offset = 0
        
        # Load level data from level manager
        level_data = self.level_manager.load_level(level_number)
        
        # Create game objects from level data
        self.player = Player(level_data['player_start_x'], level_data['player_start_y'])
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.question_blocks = pygame.sprite.Group()
        
        # Create platforms
        for platform_data in level_data['platforms']:
            platform = Platform(platform_data['x'], platform_data['y'], 
                               platform_data['width'], platform_data['height'],
                               platform_data['type'])
            self.platforms.add(platform)
        
        # Create enemies
        for enemy_data in level_data['enemies']:
            enemy = Enemy(enemy_data['x'], enemy_data['y'], enemy_data['type'])
            self.enemies.add(enemy)
        
        # Create coins
        for coin_data in level_data['coins']:
            coin = Coin(coin_data['x'], coin_data['y'])
            self.coins.add(coin)
        
        # Create question blocks
        for block_data in level_data['question_blocks']:
            block = QuestionBlock(block_data['x'], block_data['y'], block_data['content'])
            self.question_blocks.add(block)
        
        # Set level properties
        self.level_width = level_data['level_width']
        self.flagpole_x = level_data['flagpole_x']
        
        # Load background
        self.background = pygame.image.load(os.path.join('assets', 'images', f'background_level{level_number}.png')).convert()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                if event.key == K_SPACE:
                    if self.game_over:
                        # Restart the game when space is pressed on game over screen
                        self.restart_game()
                    elif not self.player.is_jumping:
                        self.player.jump()
                        self.jump_sound.play()
    
    def restart_game(self):
        # Reset game state
        self.score = 0
        self.lives = INITIAL_LIVES
        self.current_level = 1
        self.game_over = False
        
        # Load the first level
        self.load_level(self.current_level)
    
    def update(self):
        if self.game_over:
            return
        
        # Update player
        self.player.update(self.platforms, self.enemies, self.coins, self.question_blocks)
        
        # Check if player collected a coin
        if self.player.coin_collected:
            self.score += 100
            self.coin_sound.play()
            self.player.coin_collected = False
        
        # Check if player hit an enemy
        if self.player.enemy_killed:
            self.score += 200
            self.player.enemy_killed = False
        
        # Check if player died
        if self.player.is_dead:
            self.lives -= 1
            self.death_sound.play()
            if self.lives <= 0:
                self.game_over = True
            else:
                # Respawn player
                self.player.respawn(self.level_manager.get_current_level()['player_start_x'], 
                                   self.level_manager.get_current_level()['player_start_y'])
        
        # Update camera position to follow player
        self.camera_offset = max(0, self.player.rect.x - SCREEN_WIDTH // 3)
        self.camera_offset = min(self.camera_offset, self.level_width - SCREEN_WIDTH)
        
        # Update enemies
        self.enemies.update(self.platforms, self.camera_offset)
        
        # Update coins animation
        self.coins.update()
        
        # Update question blocks
        self.question_blocks.update()
        
        # Check if player reached the flagpole
        if self.player.rect.x >= self.flagpole_x:
            self.current_level += 1
            if self.current_level > self.level_manager.get_level_count():
                # Player beat the game
                self.game_over = True
            else:
                # Load next level
                self.load_level(self.current_level)
    
    def draw(self):
        # Draw background - fix tiling to prevent distortion
        bg_width = self.background.get_width()
        for i in range(-1, int(SCREEN_WIDTH / bg_width) + 2):
            self.screen.blit(self.background, ((i * bg_width) - (self.camera_offset % bg_width), 0))
        
        # Draw game objects
        for platform in self.platforms:
            platform.draw(self.screen, self.camera_offset)
        
        for enemy in self.enemies:
            enemy.draw(self.screen, self.camera_offset)
        
        for coin in self.coins:
            coin.draw(self.screen, self.camera_offset)
        
        for block in self.question_blocks:
            block.draw(self.screen, self.camera_offset)
        
        # Draw player
        self.player.draw(self.screen, self.camera_offset)
        
        # Draw UI
        self.ui.draw(self.screen, self.score, self.lives, self.current_level)
        
        # Draw game over screen if needed
        if self.game_over:
            self.ui.draw_game_over(self.screen, self.score)
        
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
