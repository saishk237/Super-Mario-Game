import pygame
import os

# Initialize pygame
pygame.init()

# Create directories if they don't exist
os.makedirs('assets/images', exist_ok=True)

# Colors
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BROWN = (139, 69, 19)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
SKY_BLUE = (135, 206, 235)
WHITE = (255, 255, 255)

def create_improved_ui_elements():
    # Improved coin icon for UI
    coin_icon = pygame.Surface((24, 24), pygame.SRCALPHA)
    pygame.draw.circle(coin_icon, YELLOW, (12, 12), 10)
    pygame.draw.circle(coin_icon, BLACK, (12, 12), 10, 1)  # Border
    
    # Add some detail to make it look more like a coin
    pygame.draw.circle(coin_icon, (220, 220, 0), (12, 12), 7)  # Inner circle
    pygame.draw.line(coin_icon, BLACK, (12, 4), (12, 20), 1)  # Vertical line
    
    pygame.image.save(coin_icon, os.path.join('assets', 'images', 'coin_icon.png'))
    
    # Improved coin sprites
    for i in range(1, 5):
        coin = pygame.Surface((16, 16), pygame.SRCALPHA)
        
        if i == 1:  # Full coin
            pygame.draw.circle(coin, YELLOW, (8, 8), 7)
            pygame.draw.circle(coin, (220, 220, 0), (8, 8), 5)  # Inner circle
            pygame.draw.line(coin, BLACK, (8, 3), (8, 13), 1)  # Vertical line
        
        elif i == 2:  # Slightly turned
            pygame.draw.ellipse(coin, YELLOW, (3, 1, 10, 14))
            pygame.draw.ellipse(coin, (220, 220, 0), (4, 2, 8, 12))  # Inner ellipse
            pygame.draw.line(coin, BLACK, (8, 3), (8, 13), 1)  # Vertical line
        
        elif i == 3:  # Edge view
            pygame.draw.line(coin, YELLOW, (8, 2), (8, 14), 3)
            pygame.draw.line(coin, (220, 220, 0), (8, 3), (8, 13), 1)
        
        else:  # Slightly turned (other direction)
            pygame.draw.ellipse(coin, YELLOW, (3, 1, 10, 14))
            pygame.draw.ellipse(coin, (220, 220, 0), (4, 2, 8, 12))  # Inner ellipse
            pygame.draw.line(coin, BLACK, (8, 3), (8, 13), 1)  # Vertical line
        
        pygame.image.save(coin, os.path.join('assets', 'images', f'coin{i}.png'))
    
    # Improved question block
    question = pygame.Surface((32, 32), pygame.SRCALPHA)
    pygame.draw.rect(question, YELLOW, (0, 0, 32, 32))
    pygame.draw.rect(question, BLACK, (0, 0, 32, 32), 1)  # Border
    
    # Add some texture to the question block
    pygame.draw.rect(question, (220, 220, 0), (2, 2, 28, 28))  # Inner rectangle
    pygame.draw.rect(question, (240, 240, 0), (4, 4, 24, 24))  # Another inner rectangle
    
    # Draw the question mark
    font = pygame.font.Font(None, 36)
    text = font.render("?", True, BLACK)
    question.blit(text, (12, 8))
    
    pygame.image.save(question, os.path.join('assets', 'images', 'question_block.png'))
    
    # Improved question block inactive
    inactive = pygame.Surface((32, 32), pygame.SRCALPHA)
    pygame.draw.rect(inactive, GRAY, (0, 0, 32, 32))
    pygame.draw.rect(inactive, BLACK, (0, 0, 32, 32), 1)  # Border
    
    # Add some texture to the inactive block
    pygame.draw.rect(inactive, (100, 100, 100), (2, 2, 28, 28))  # Inner rectangle
    pygame.draw.rect(inactive, (120, 120, 120), (4, 4, 24, 24))  # Another inner rectangle
    
    pygame.image.save(inactive, os.path.join('assets', 'images', 'question_block_inactive.png'))
    
    # Improved ground tile
    ground = pygame.Surface((32, 32), pygame.SRCALPHA)
    pygame.draw.rect(ground, BROWN, (0, 0, 32, 32))
    
    # Add texture to ground
    for i in range(4):
        for j in range(4):
            if (i + j) % 2 == 0:
                pygame.draw.rect(ground, (120, 60, 20), (i*8, j*8, 8, 8))
    
    pygame.draw.rect(ground, BLACK, (0, 0, 32, 32), 1)  # Border
    
    pygame.image.save(ground, os.path.join('assets', 'images', 'ground_tile.png'))
    
    # Improved brick tile
    brick = pygame.Surface((32, 32), pygame.SRCALPHA)
    pygame.draw.rect(brick, ORANGE, (0, 0, 32, 32))
    
    # Draw brick pattern
    pygame.draw.rect(brick, (200, 100, 0), (0, 0, 16, 16))
    pygame.draw.rect(brick, (200, 100, 0), (16, 16, 16, 16))
    pygame.draw.rect(brick, (220, 120, 20), (16, 0, 16, 16))
    pygame.draw.rect(brick, (220, 120, 20), (0, 16, 16, 16))
    
    # Draw mortar lines
    pygame.draw.line(brick, (100, 50, 0), (0, 16), (32, 16), 1)
    pygame.draw.line(brick, (100, 50, 0), (16, 0), (16, 32), 1)
    pygame.draw.rect(brick, BLACK, (0, 0, 32, 32), 1)  # Border
    
    pygame.image.save(brick, os.path.join('assets', 'images', 'brick_tile.png'))
    
    # Improved pipe tile
    pipe = pygame.Surface((32, 32), pygame.SRCALPHA)
    pygame.draw.rect(pipe, GREEN, (0, 0, 32, 32))
    
    # Add highlights and shadows for 3D effect
    pygame.draw.rect(pipe, (0, 200, 0), (2, 2, 28, 28))  # Lighter green
    pygame.draw.rect(pipe, (0, 180, 0), (4, 4, 24, 24))  # Mid green
    pygame.draw.rect(pipe, (0, 100, 0), (28, 0, 4, 32))  # Shadow on right
    pygame.draw.rect(pipe, (0, 100, 0), (0, 28, 32, 4))  # Shadow on bottom
    
    pygame.draw.rect(pipe, BLACK, (0, 0, 32, 32), 1)  # Border
    
    pygame.image.save(pipe, os.path.join('assets', 'images', 'pipe_tile.png'))

def create_improved_backgrounds():
    for level in range(1, 4):
        bg = pygame.Surface((800, 600), pygame.SRCALPHA)
        
        # Sky gradient
        for y in range(600):
            # Create a gradient from light blue to darker blue
            color_value = max(100, 200 - y // 3)
            pygame.draw.line(bg, (color_value, color_value + 20, 255), (0, y), (800, y))
        
        # Clouds with more detail
        for i in range(5):
            cloud_x = i * 160
            cloud_y = 50 + (i % 3) * 30
            
            # Draw multiple circles for a fluffy cloud
            pygame.draw.circle(bg, WHITE, (cloud_x + 20, cloud_y + 10), 20)
            pygame.draw.circle(bg, WHITE, (cloud_x + 40, cloud_y), 25)
            pygame.draw.circle(bg, WHITE, (cloud_x + 60, cloud_y + 10), 20)
            pygame.draw.circle(bg, WHITE, (cloud_x + 40, cloud_y + 15), 18)
            
            # Add some shading
            pygame.draw.circle(bg, (240, 240, 240), (cloud_x + 20, cloud_y + 15), 15)
            pygame.draw.circle(bg, (240, 240, 240), (cloud_x + 60, cloud_y + 15), 15)
        
        # Hills with detail
        for i in range(3):
            hill_x = i * 300
            
            # Draw the hill
            pygame.draw.polygon(bg, GREEN, [(hill_x, 500), (hill_x + 150, 350), (hill_x + 300, 500)])
            
            # Add some shading for depth
            pygame.draw.polygon(bg, (0, 180, 0), [(hill_x + 50, 470), (hill_x + 150, 370), (hill_x + 250, 470)])
            pygame.draw.polygon(bg, (0, 160, 0), [(hill_x + 80, 450), (hill_x + 150, 380), (hill_x + 220, 450)])
        
        # Different elements based on level
        if level == 2:
            # More detailed clouds
            for i in range(3):
                cloud_x = 100 + i * 200
                cloud_y = 100 + (i % 2) * 40
                
                pygame.draw.circle(bg, WHITE, (cloud_x + 25, cloud_y + 15), 25)
                pygame.draw.circle(bg, WHITE, (cloud_x + 50, cloud_y), 30)
                pygame.draw.circle(bg, WHITE, (cloud_x + 75, cloud_y + 15), 25)
                pygame.draw.circle(bg, WHITE, (cloud_x + 50, cloud_y + 20), 22)
                
                # Add some shading
                pygame.draw.circle(bg, (240, 240, 240), (cloud_x + 25, cloud_y + 20), 20)
                pygame.draw.circle(bg, (240, 240, 240), (cloud_x + 75, cloud_y + 20), 20)
        
        if level == 3:
            # Different sky gradient for level 3
            for y in range(600):
                # Create a gradient from light purple to darker blue
                r = max(100, 180 - y // 4)
                g = max(100, 150 - y // 5)
                b = max(150, 250 - y // 6)
                pygame.draw.line(bg, (r, g, b), (0, y), (800, y))
            
            # Mountains with snow caps
            for i in range(2):
                mountain_x = 100 + i * 400
                
                # Draw the mountain
                pygame.draw.polygon(bg, GRAY, [(mountain_x, 500), (mountain_x + 200, 200), (mountain_x + 400, 500)])
                
                # Add snow cap
                pygame.draw.polygon(bg, WHITE, [(mountain_x + 150, 280), (mountain_x + 200, 200), (mountain_x + 250, 280)])
                
                # Add some shading for depth
                pygame.draw.polygon(bg, (100, 100, 100), [(mountain_x + 50, 450), (mountain_x + 200, 250), (mountain_x + 350, 450)])
        
        pygame.image.save(bg, os.path.join('assets', 'images', f'background_level{level}.png'))

# Create improved UI elements and backgrounds
create_improved_ui_elements()
create_improved_backgrounds()
print("Improved UI elements and backgrounds created successfully!")
