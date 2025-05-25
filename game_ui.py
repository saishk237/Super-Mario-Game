import pygame
import os
from pygame.locals import *

class GameUI:
    def __init__(self):
        # Initialize fonts
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.large_font = pygame.font.Font(None, 72)
        
        # Load UI images
        self.coin_icon = pygame.image.load(os.path.join('assets', 'images', 'coin_icon.png')).convert_alpha()
        self.life_icon = pygame.image.load(os.path.join('assets', 'images', 'life_icon.png')).convert_alpha()
    
    def draw(self, screen, score, lives, level):
        # Create a semi-transparent UI background for better readability
        ui_bg = pygame.Surface((screen.get_width(), 40))
        ui_bg.set_alpha(100)
        ui_bg.fill((0, 0, 0))
        screen.blit(ui_bg, (0, 0))
        
        # Draw score with shadow for better visibility
        score_shadow = self.font.render(f"SCORE: {score}", True, (0, 0, 0))
        score_text = self.font.render(f"SCORE: {score}", True, (255, 255, 255))
        screen.blit(score_shadow, (22, 12))
        screen.blit(score_text, (20, 10))
        
        # Draw coin icon and count
        screen.blit(self.coin_icon, (20, 50))
        coin_shadow = self.font.render(f"x {score // 100}", True, (0, 0, 0))
        coin_text = self.font.render(f"x {score // 100}", True, (255, 255, 255))
        screen.blit(coin_shadow, (52, 52))
        screen.blit(coin_text, (50, 50))
        
        # Draw lives
        screen.blit(self.life_icon, (20, 90))
        lives_shadow = self.font.render(f"x {lives}", True, (0, 0, 0))
        lives_text = self.font.render(f"x {lives}", True, (255, 255, 255))
        screen.blit(lives_shadow, (52, 92))
        screen.blit(lives_text, (50, 90))
        
        # Draw level number
        level_shadow = self.font.render(f"LEVEL {level}", True, (0, 0, 0))
        level_text = self.font.render(f"LEVEL {level}", True, (255, 255, 255))
        screen.blit(level_shadow, (screen.get_width() - level_text.get_width() - 18, 12))
        screen.blit(level_text, (screen.get_width() - level_text.get_width() - 20, 10))
    
    def draw_game_over(self, screen, score):
        # Darken the screen
        overlay = pygame.Surface((screen.get_width(), screen.get_height()))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # Draw game over text with shadow for better visibility
        game_over_shadow = self.large_font.render("GAME OVER", True, (0, 0, 0))
        game_over_text = self.large_font.render("GAME OVER", True, (255, 0, 0))
        
        # Position text
        text_x = screen.get_width() // 2 - game_over_text.get_width() // 2
        text_y = screen.get_height() // 3
        
        # Draw shadow slightly offset
        screen.blit(game_over_shadow, (text_x + 3, text_y + 3))
        screen.blit(game_over_text, (text_x, text_y))
        
        # Draw final score with shadow
        score_shadow = self.font.render(f"Final Score: {score}", True, (0, 0, 0))
        score_text = self.font.render(f"Final Score: {score}", True, (255, 255, 255))
        
        # Position score text
        score_x = screen.get_width() // 2 - score_text.get_width() // 2
        score_y = screen.get_height() // 2
        
        # Draw shadow slightly offset
        screen.blit(score_shadow, (score_x + 2, score_y + 2))
        screen.blit(score_text, (score_x, score_y))
        
        # Draw restart instructions with shadow
        restart_shadow = self.font.render("Press SPACE to restart", True, (0, 0, 0))
        restart_text = self.font.render("Press SPACE to restart", True, (0, 255, 0))
        
        # Position restart text
        restart_x = screen.get_width() // 2 - restart_text.get_width() // 2
        restart_y = screen.get_height() // 2 + 50
        
        # Draw shadow slightly offset
        screen.blit(restart_shadow, (restart_x + 2, restart_y + 2))
        screen.blit(restart_text, (restart_x, restart_y))
        
        # Draw quit instructions with shadow
        quit_shadow = self.font.render("Press ESC to quit", True, (0, 0, 0))
        quit_text = self.font.render("Press ESC to quit", True, (255, 255, 255))
        
        # Position quit text
        quit_x = screen.get_width() // 2 - quit_text.get_width() // 2
        quit_y = screen.get_height() // 2 + 90
        
        # Draw shadow slightly offset
        screen.blit(quit_shadow, (quit_x + 2, quit_y + 2))
        screen.blit(quit_text, (quit_x, quit_y))
