import pygame
import os

# Initialize pygame
pygame.init()

# Create directories if they don't exist
os.makedirs('assets/images', exist_ok=True)

# Colors
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

def create_improved_enemies():
    # Improved Goomba
    for i in range(1, 3):
        goomba = pygame.Surface((32, 32), pygame.SRCALPHA)
        
        # Body
        pygame.draw.rect(goomba, BROWN, (0, 8, 32, 24))
        
        # Feet
        if i == 1:
            pygame.draw.rect(goomba, (100, 50, 0), (2, 28, 12, 4))  # Left foot
            pygame.draw.rect(goomba, (100, 50, 0), (18, 28, 12, 4))  # Right foot
        else:
            pygame.draw.rect(goomba, (100, 50, 0), (4, 28, 10, 4))  # Left foot
            pygame.draw.rect(goomba, (100, 50, 0), (18, 28, 10, 4))  # Right foot
        
        # Head/cap
        pygame.draw.ellipse(goomba, (180, 100, 50), (0, 0, 32, 16))
        
        # Face
        pygame.draw.rect(goomba, WHITE, (6, 16, 6, 6))  # Left eye white
        pygame.draw.rect(goomba, WHITE, (20, 16, 6, 6))  # Right eye white
        pygame.draw.rect(goomba, BLACK, (8, 18, 2, 2))  # Left pupil
        pygame.draw.rect(goomba, BLACK, (22, 18, 2, 2))  # Right pupil
        
        # Eyebrows - angry look
        pygame.draw.line(goomba, BLACK, (5, 14), (12, 16), 2)  # Left eyebrow
        pygame.draw.line(goomba, BLACK, (20, 16), (27, 14), 2)  # Right eyebrow
        
        # Mouth - frowning
        pygame.draw.arc(goomba, BLACK, (10, 22, 12, 8), 3.14, 2*3.14, 2)
        
        pygame.image.save(goomba, os.path.join('assets', 'images', f'goomba{i}.png'))
    
    # Goomba squished
    squished = pygame.Surface((32, 16), pygame.SRCALPHA)
    
    # Flattened body
    pygame.draw.ellipse(squished, BROWN, (0, 0, 32, 16))
    pygame.draw.ellipse(squished, (100, 50, 0), (2, 2, 28, 12))
    
    # Flattened face - X eyes
    pygame.draw.line(squished, BLACK, (8, 4), (12, 8), 2)  # Left X eye
    pygame.draw.line(squished, BLACK, (8, 8), (12, 4), 2)  # Left X eye
    pygame.draw.line(squished, BLACK, (20, 4), (24, 8), 2)  # Right X eye
    pygame.draw.line(squished, BLACK, (20, 8), (24, 4), 2)  # Right X eye
    
    # Flattened mouth
    pygame.draw.line(squished, BLACK, (14, 10), (18, 10), 2)
    
    pygame.image.save(squished, os.path.join('assets', 'images', 'goomba_squished.png'))
    
    # Improved Koopa
    for i in range(1, 3):
        koopa = pygame.Surface((32, 48), pygame.SRCALPHA)
        
        # Body
        pygame.draw.rect(koopa, GREEN, (4, 16, 24, 24))
        
        # Shell on back
        pygame.draw.ellipse(koopa, YELLOW, (2, 12, 28, 32))
        pygame.draw.ellipse(koopa, (220, 200, 0), (6, 16, 20, 24))
        
        # Pattern on shell
        for j in range(3):
            pygame.draw.rect(koopa, (200, 150, 0), (10, 20 + j*8, 12, 4))
        
        # Head
        pygame.draw.ellipse(koopa, GREEN, (8, 0, 16, 20))
        
        # Face
        pygame.draw.rect(koopa, WHITE, (10, 6, 4, 4))  # Left eye white
        pygame.draw.rect(koopa, WHITE, (18, 6, 4, 4))  # Right eye white
        
        if i == 1:
            pygame.draw.rect(koopa, BLACK, (11, 7, 2, 2))  # Left pupil
            pygame.draw.rect(koopa, BLACK, (19, 7, 2, 2))  # Right pupil
        else:
            pygame.draw.rect(koopa, BLACK, (11, 8, 2, 2))  # Left pupil
            pygame.draw.rect(koopa, BLACK, (19, 8, 2, 2))  # Right pupil
        
        # Beak/mouth
        pygame.draw.polygon(koopa, RED, [(14, 12), (16, 14), (18, 12)])
        
        # Feet
        if i == 1:
            pygame.draw.rect(koopa, YELLOW, (6, 40, 8, 8))  # Left foot
            pygame.draw.rect(koopa, YELLOW, (18, 40, 8, 8))  # Right foot
        else:
            pygame.draw.rect(koopa, YELLOW, (8, 40, 6, 8))  # Left foot
            pygame.draw.rect(koopa, YELLOW, (18, 40, 6, 8))  # Right foot
        
        pygame.image.save(koopa, os.path.join('assets', 'images', f'koopa{i}.png'))
    
    # Koopa shell
    shell = pygame.Surface((32, 32), pygame.SRCALPHA)
    
    # Shell
    pygame.draw.ellipse(shell, YELLOW, (0, 0, 32, 32))
    pygame.draw.ellipse(shell, (220, 200, 0), (4, 4, 24, 24))
    
    # Pattern on shell
    for j in range(3):
        pygame.draw.rect(shell, (200, 150, 0), (8, 8 + j*6, 16, 4))
    
    # Border
    pygame.draw.ellipse(shell, BLACK, (0, 0, 32, 32), 1)
    
    pygame.image.save(shell, os.path.join('assets', 'images', 'koopa_shell.png'))

# Create improved enemy sprites
create_improved_enemies()
print("Improved enemy sprites created successfully!")
