import pygame
import os
import wave
import struct
import math

# Initialize pygame
pygame.init()

# Create directories if they don't exist
os.makedirs('assets/images', exist_ok=True)
os.makedirs('assets/sounds', exist_ok=True)
os.makedirs('levels', exist_ok=True)

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
SKY_BLUE = (135, 206, 235)

# Player sprites
def create_player_sprites():
    # Player idle
    idle = pygame.Surface((32, 48), pygame.SRCALPHA)
    pygame.draw.rect(idle, RED, (0, 0, 32, 24))  # Head
    pygame.draw.rect(idle, BLUE, (0, 24, 32, 24))  # Body
    pygame.image.save(idle, os.path.join('assets', 'images', 'player_idle.png'))
    
    # Player run frames
    for i in range(1, 4):
        run = pygame.Surface((32, 48), pygame.SRCALPHA)
        pygame.draw.rect(run, RED, (0, 0, 32, 24))  # Head
        pygame.draw.rect(run, BLUE, (0, 24, 32, 24))  # Body
        # Different leg positions for animation
        if i == 1:
            pygame.draw.rect(run, BLUE, (5, 40, 10, 8))
            pygame.draw.rect(run, BLUE, (20, 36, 10, 12))
        elif i == 2:
            pygame.draw.rect(run, BLUE, (10, 38, 10, 10))
            pygame.draw.rect(run, BLUE, (15, 38, 10, 10))
        else:
            pygame.draw.rect(run, BLUE, (5, 36, 10, 12))
            pygame.draw.rect(run, BLUE, (20, 40, 10, 8))
        pygame.image.save(run, os.path.join('assets', 'images', f'player_run{i}.png'))
    
    # Player jump
    jump = pygame.Surface((32, 48), pygame.SRCALPHA)
    pygame.draw.rect(jump, RED, (0, 0, 32, 24))  # Head
    pygame.draw.rect(jump, BLUE, (0, 24, 32, 24))  # Body
    pygame.draw.rect(jump, BLUE, (5, 42, 10, 6))  # Left leg
    pygame.draw.rect(jump, BLUE, (20, 42, 10, 6))  # Right leg
    pygame.image.save(jump, os.path.join('assets', 'images', 'player_jump.png'))
    
    # Player death
    death = pygame.Surface((32, 48), pygame.SRCALPHA)
    pygame.draw.rect(death, RED, (0, 0, 32, 24))  # Head
    pygame.draw.rect(death, BLUE, (0, 24, 32, 24))  # Body
    pygame.draw.line(death, BLACK, (8, 8), (14, 14), 3)  # X eye left
    pygame.draw.line(death, BLACK, (8, 14), (14, 8), 3)  # X eye left
    pygame.draw.line(death, BLACK, (18, 8), (24, 14), 3)  # X eye right
    pygame.draw.line(death, BLACK, (18, 14), (24, 8), 3)  # X eye right
    pygame.image.save(death, os.path.join('assets', 'images', 'player_death.png'))

# Enemy sprites
def create_enemy_sprites():
    # Goomba
    for i in range(1, 3):
        goomba = pygame.Surface((32, 32), pygame.SRCALPHA)
        pygame.draw.rect(goomba, BROWN, (0, 0, 32, 32))
        if i == 1:
            pygame.draw.rect(goomba, BLACK, (5, 20, 8, 8))  # Left eye
            pygame.draw.rect(goomba, BLACK, (19, 20, 8, 8))  # Right eye
        else:
            pygame.draw.rect(goomba, BLACK, (5, 22, 8, 6))  # Left eye
            pygame.draw.rect(goomba, BLACK, (19, 22, 8, 6))  # Right eye
        pygame.image.save(goomba, os.path.join('assets', 'images', f'goomba{i}.png'))
    
    # Goomba squished
    squished = pygame.Surface((32, 16), pygame.SRCALPHA)
    pygame.draw.rect(squished, BROWN, (0, 0, 32, 16))
    pygame.draw.line(squished, BLACK, (5, 8), (27, 8), 2)  # Flat line for eyes
    pygame.image.save(squished, os.path.join('assets', 'images', 'goomba_squished.png'))
    
    # Koopa
    for i in range(1, 3):
        koopa = pygame.Surface((32, 48), pygame.SRCALPHA)
        pygame.draw.rect(koopa, GREEN, (0, 0, 32, 48))
        pygame.draw.rect(koopa, YELLOW, (4, 4, 24, 24))  # Shell
        if i == 1:
            pygame.draw.rect(koopa, BLACK, (8, 12, 6, 6))  # Left eye
            pygame.draw.rect(koopa, BLACK, (18, 12, 6, 6))  # Right eye
        else:
            pygame.draw.rect(koopa, BLACK, (8, 14, 6, 4))  # Left eye
            pygame.draw.rect(koopa, BLACK, (18, 14, 6, 4))  # Right eye
        pygame.image.save(koopa, os.path.join('assets', 'images', f'koopa{i}.png'))
    
    # Koopa shell
    shell = pygame.Surface((32, 32), pygame.SRCALPHA)
    pygame.draw.rect(shell, GREEN, (0, 0, 32, 32))
    pygame.draw.rect(shell, YELLOW, (4, 4, 24, 24))  # Shell
    pygame.image.save(shell, os.path.join('assets', 'images', 'koopa_shell.png'))

# Platform sprites
def create_platform_sprites():
    # Ground tile
    ground = pygame.Surface((32, 32), pygame.SRCALPHA)
    pygame.draw.rect(ground, BROWN, (0, 0, 32, 32))
    pygame.draw.line(ground, BLACK, (0, 0), (32, 0), 2)  # Top border
    pygame.draw.line(ground, BLACK, (0, 31), (32, 31), 1)  # Bottom border
    pygame.draw.line(ground, BLACK, (0, 0), (0, 32), 1)  # Left border
    pygame.draw.line(ground, BLACK, (31, 0), (31, 32), 1)  # Right border
    pygame.image.save(ground, os.path.join('assets', 'images', 'ground_tile.png'))
    
    # Brick tile
    brick = pygame.Surface((32, 32), pygame.SRCALPHA)
    pygame.draw.rect(brick, ORANGE, (0, 0, 32, 32))
    pygame.draw.line(brick, BLACK, (0, 0), (32, 0), 1)  # Top border
    pygame.draw.line(brick, BLACK, (0, 31), (32, 31), 1)  # Bottom border
    pygame.draw.line(brick, BLACK, (0, 0), (0, 32), 1)  # Left border
    pygame.draw.line(brick, BLACK, (31, 0), (31, 32), 1)  # Right border
    pygame.draw.line(brick, BLACK, (0, 16), (32, 16), 1)  # Middle horizontal
    pygame.draw.line(brick, BLACK, (16, 0), (16, 32), 1)  # Middle vertical
    pygame.image.save(brick, os.path.join('assets', 'images', 'brick_tile.png'))
    
    # Pipe tile
    pipe = pygame.Surface((32, 32), pygame.SRCALPHA)
    pygame.draw.rect(pipe, GREEN, (0, 0, 32, 32))
    pygame.draw.rect(pipe, BLACK, (0, 0, 32, 32), 1)  # Border
    pygame.image.save(pipe, os.path.join('assets', 'images', 'pipe_tile.png'))
    
    # Question block
    question = pygame.Surface((32, 32), pygame.SRCALPHA)
    pygame.draw.rect(question, YELLOW, (0, 0, 32, 32))
    pygame.draw.rect(question, BLACK, (0, 0, 32, 32), 1)  # Border
    font = pygame.font.Font(None, 36)
    text = font.render("?", True, BLACK)
    question.blit(text, (12, 8))
    pygame.image.save(question, os.path.join('assets', 'images', 'question_block.png'))
    
    # Question block inactive
    inactive = pygame.Surface((32, 32), pygame.SRCALPHA)
    pygame.draw.rect(inactive, GRAY, (0, 0, 32, 32))
    pygame.draw.rect(inactive, BLACK, (0, 0, 32, 32), 1)  # Border
    pygame.image.save(inactive, os.path.join('assets', 'images', 'question_block_inactive.png'))

# Coin sprites
def create_coin_sprites():
    for i in range(1, 5):
        coin = pygame.Surface((16, 16), pygame.SRCALPHA)
        if i == 1:
            pygame.draw.circle(coin, YELLOW, (8, 8), 8)
        elif i == 2:
            pygame.draw.ellipse(coin, YELLOW, (2, 0, 12, 16))
        elif i == 3:
            pygame.draw.line(coin, YELLOW, (8, 0), (8, 16), 4)
        else:
            pygame.draw.ellipse(coin, YELLOW, (2, 0, 12, 16))
        pygame.image.save(coin, os.path.join('assets', 'images', f'coin{i}.png'))
    
    # Coin icon for UI
    coin_icon = pygame.Surface((24, 24), pygame.SRCALPHA)
    pygame.draw.circle(coin_icon, YELLOW, (12, 12), 12)
    pygame.draw.circle(coin_icon, BLACK, (12, 12), 12, 1)  # Border
    pygame.image.save(coin_icon, os.path.join('assets', 'images', 'coin_icon.png'))
    
    # Life icon for UI
    life_icon = pygame.Surface((24, 24), pygame.SRCALPHA)
    pygame.draw.rect(life_icon, RED, (0, 0, 24, 12))  # Head
    pygame.draw.rect(life_icon, BLUE, (0, 12, 24, 12))  # Body
    pygame.image.save(life_icon, os.path.join('assets', 'images', 'life_icon.png'))

# Background images
def create_background_images():
    for level in range(1, 4):
        bg = pygame.Surface((800, 600), pygame.SRCALPHA)
        
        # Sky
        bg.fill(SKY_BLUE)
        
        # Clouds
        for i in range(5):
            cloud_x = i * 160
            cloud_y = 50 + (i % 3) * 30
            pygame.draw.ellipse(bg, WHITE, (cloud_x, cloud_y, 80, 40))
            pygame.draw.ellipse(bg, WHITE, (cloud_x + 40, cloud_y - 10, 60, 30))
            pygame.draw.ellipse(bg, WHITE, (cloud_x + 20, cloud_y + 10, 70, 35))
        
        # Hills
        for i in range(3):
            hill_x = i * 300
            pygame.draw.polygon(bg, GREEN, [(hill_x, 500), (hill_x + 150, 350), (hill_x + 300, 500)])
        
        # Different elements based on level
        if level == 2:
            # More clouds
            for i in range(3):
                cloud_x = 100 + i * 200
                cloud_y = 100 + (i % 2) * 40
                pygame.draw.ellipse(bg, WHITE, (cloud_x, cloud_y, 100, 50))
        
        if level == 3:
            # Different sky color
            bg.fill((100, 150, 250))
            # Mountains
            for i in range(2):
                mountain_x = 100 + i * 400
                pygame.draw.polygon(bg, GRAY, [(mountain_x, 500), (mountain_x + 200, 200), (mountain_x + 400, 500)])
        
        pygame.image.save(bg, os.path.join('assets', 'images', f'background_level{level}.png'))

# Create sound effects using wave module
def create_sound_effects():
    # Create a simple beep sound for jump
    create_beep_sound(os.path.join('assets', 'sounds', 'jump.wav'), 440, 0.2)
    
    # Create a simple coin sound
    create_beep_sound(os.path.join('assets', 'sounds', 'coin.wav'), 880, 0.1)
    
    # Create a simple death sound
    create_beep_sound(os.path.join('assets', 'sounds', 'death.wav'), 220, 0.5)
    
    # Create a simple background music
    create_music_sound(os.path.join('assets', 'sounds', 'background_music.wav'))

def create_beep_sound(filename, frequency, duration):
    # Parameters
    sample_rate = 44100  # Hz
    amplitude = 32767 * 0.5  # Half volume
    
    # Calculate the number of frames
    num_frames = int(duration * sample_rate)
    
    # Open a new wave file
    with wave.open(filename, 'w') as wav_file:
        # Set parameters
        wav_file.setparams((2, 2, sample_rate, 0, 'NONE', 'not compressed'))
        
        # Generate frames
        for i in range(num_frames):
            # Calculate the value at time i
            value = amplitude * math.sin(2 * math.pi * frequency * i / sample_rate)
            
            # Convert to integer
            packed_value = struct.pack('h', int(value))
            
            # Write the same value to both channels
            wav_file.writeframes(packed_value + packed_value)

def create_music_sound(filename):
    # Parameters
    sample_rate = 44100  # Hz
    duration = 5.0  # seconds
    amplitude = 32767 * 0.3  # 30% volume
    
    # Notes (C4 to C5)
    notes = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]
    
    # Calculate the number of frames
    num_frames = int(duration * sample_rate)
    note_frames = num_frames // 16
    
    # Open a new wave file
    with wave.open(filename, 'w') as wav_file:
        # Set parameters
        wav_file.setparams((2, 2, sample_rate, 0, 'NONE', 'not compressed'))
        
        # Generate frames
        for i in range(num_frames):
            # Determine which note to play
            note_index = (i // note_frames) % len(notes)
            frequency = notes[note_index]
            
            # Calculate the value at time i
            value = amplitude * math.sin(2 * math.pi * frequency * i / sample_rate)
            
            # Convert to integer
            packed_value = struct.pack('h', int(value))
            
            # Write the same value to both channels
            wav_file.writeframes(packed_value + packed_value)

# Create all assets
create_player_sprites()
create_enemy_sprites()
create_platform_sprites()
create_coin_sprites()
create_background_images()
create_sound_effects()

print("All placeholder assets have been created successfully!")
