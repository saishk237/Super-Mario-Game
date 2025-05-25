import pygame
import os

# Initialize pygame
pygame.init()

# Create directories if they don't exist
os.makedirs('assets/images', exist_ok=True)

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
SKIN = (255, 200, 150)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def create_improved_mario():
    # Create improved Mario sprites with a face
    
    # Player idle
    idle = pygame.Surface((32, 48), pygame.SRCALPHA)
    
    # Hat and hair
    pygame.draw.rect(idle, RED, (0, 0, 32, 12))  # Hat
    pygame.draw.rect(idle, BROWN, (0, 12, 32, 4))  # Hair
    
    # Face
    pygame.draw.rect(idle, SKIN, (0, 16, 32, 12))  # Face
    pygame.draw.rect(idle, BLACK, (8, 20, 4, 4))  # Left eye
    pygame.draw.rect(idle, BLACK, (20, 20, 4, 4))  # Right eye
    pygame.draw.rect(idle, BROWN, (12, 24, 8, 4))  # Mustache
    
    # Body
    pygame.draw.rect(idle, RED, (0, 28, 32, 12))  # Shirt
    pygame.draw.rect(idle, BLUE, (0, 40, 32, 8))  # Overalls
    
    pygame.image.save(idle, os.path.join('assets', 'images', 'player_idle.png'))
    
    # Player run frames
    for i in range(1, 4):
        run = pygame.Surface((32, 48), pygame.SRCALPHA)
        
        # Hat and hair
        pygame.draw.rect(run, RED, (0, 0, 32, 12))  # Hat
        pygame.draw.rect(run, BROWN, (0, 12, 32, 4))  # Hair
        
        # Face
        pygame.draw.rect(run, SKIN, (0, 16, 32, 12))  # Face
        pygame.draw.rect(run, BLACK, (8, 20, 4, 4))  # Left eye
        pygame.draw.rect(run, BLACK, (20, 20, 4, 4))  # Right eye
        pygame.draw.rect(run, BROWN, (12, 24, 8, 4))  # Mustache
        
        # Body
        pygame.draw.rect(run, RED, (0, 28, 32, 12))  # Shirt
        pygame.draw.rect(run, BLUE, (0, 40, 32, 8))  # Overalls
        
        # Different leg positions for animation
        if i == 1:
            pygame.draw.rect(run, BLUE, (5, 40, 10, 8))  # Left leg
            pygame.draw.rect(run, BLUE, (20, 36, 10, 12))  # Right leg
            pygame.draw.rect(run, BROWN, (20, 44, 10, 4))  # Right shoe
            pygame.draw.rect(run, BROWN, (5, 44, 10, 4))  # Left shoe
        elif i == 2:
            pygame.draw.rect(run, BLUE, (10, 38, 6, 10))  # Left leg
            pygame.draw.rect(run, BLUE, (16, 38, 6, 10))  # Right leg
            pygame.draw.rect(run, BROWN, (10, 44, 6, 4))  # Left shoe
            pygame.draw.rect(run, BROWN, (16, 44, 6, 4))  # Right shoe
        else:
            pygame.draw.rect(run, BLUE, (5, 36, 10, 12))  # Left leg
            pygame.draw.rect(run, BLUE, (20, 40, 10, 8))  # Right leg
            pygame.draw.rect(run, BROWN, (5, 44, 10, 4))  # Left shoe
            pygame.draw.rect(run, BROWN, (20, 44, 10, 4))  # Right shoe
        
        pygame.image.save(run, os.path.join('assets', 'images', f'player_run{i}.png'))
    
    # Player jump
    jump = pygame.Surface((32, 48), pygame.SRCALPHA)
    
    # Hat and hair
    pygame.draw.rect(jump, RED, (0, 0, 32, 12))  # Hat
    pygame.draw.rect(jump, BROWN, (0, 12, 32, 4))  # Hair
    
    # Face
    pygame.draw.rect(jump, SKIN, (0, 16, 32, 12))  # Face
    pygame.draw.rect(jump, BLACK, (8, 20, 4, 4))  # Left eye
    pygame.draw.rect(jump, BLACK, (20, 20, 4, 4))  # Right eye
    pygame.draw.rect(jump, BROWN, (12, 24, 8, 4))  # Mustache
    
    # Body
    pygame.draw.rect(jump, RED, (0, 28, 32, 12))  # Shirt
    pygame.draw.rect(jump, BLUE, (0, 40, 32, 8))  # Overalls
    
    # Legs in jumping position
    pygame.draw.rect(jump, BLUE, (8, 42, 8, 6))  # Left leg
    pygame.draw.rect(jump, BLUE, (16, 42, 8, 6))  # Right leg
    pygame.draw.rect(jump, BROWN, (8, 44, 8, 4))  # Left shoe
    pygame.draw.rect(jump, BROWN, (16, 44, 8, 4))  # Right shoe
    
    pygame.image.save(jump, os.path.join('assets', 'images', 'player_jump.png'))
    
    # Player death
    death = pygame.Surface((32, 48), pygame.SRCALPHA)
    
    # Hat and hair
    pygame.draw.rect(death, RED, (0, 0, 32, 12))  # Hat
    pygame.draw.rect(death, BROWN, (0, 12, 32, 4))  # Hair
    
    # Face with X eyes
    pygame.draw.rect(death, SKIN, (0, 16, 32, 12))  # Face
    pygame.draw.line(death, BLACK, (8, 20), (12, 24), 2)  # X eye left
    pygame.draw.line(death, BLACK, (8, 24), (12, 20), 2)  # X eye left
    pygame.draw.line(death, BLACK, (20, 20), (24, 24), 2)  # X eye right
    pygame.draw.line(death, BLACK, (20, 24), (24, 20), 2)  # X eye right
    pygame.draw.rect(death, BROWN, (12, 24, 8, 4))  # Mustache
    
    # Body
    pygame.draw.rect(death, RED, (0, 28, 32, 12))  # Shirt
    pygame.draw.rect(death, BLUE, (0, 40, 32, 8))  # Overalls
    
    pygame.image.save(death, os.path.join('assets', 'images', 'player_death.png'))
    
    # Life icon for UI
    life_icon = pygame.Surface((24, 24), pygame.SRCALPHA)
    
    # Mini Mario head for life icon
    pygame.draw.rect(life_icon, RED, (0, 0, 24, 10))  # Hat
    pygame.draw.rect(life_icon, BROWN, (0, 10, 24, 2))  # Hair
    pygame.draw.rect(life_icon, SKIN, (0, 12, 24, 8))  # Face
    pygame.draw.rect(life_icon, BLACK, (6, 14, 3, 3))  # Left eye
    pygame.draw.rect(life_icon, BLACK, (15, 14, 3, 3))  # Right eye
    pygame.draw.rect(life_icon, BROWN, (9, 17, 6, 3))  # Mustache
    
    pygame.image.save(life_icon, os.path.join('assets', 'images', 'life_icon.png'))

# Create improved Mario sprites
create_improved_mario()
print("Improved Mario sprites created successfully!")
