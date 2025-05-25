"""
Utility functions for loading game assets.
"""

import os
import pygame

class AssetLoader:
    """
    Class for loading and managing game assets.
    """
    
    @staticmethod
    def load_image(filename):
        """
        Load an image and convert it to the right format for PyGame.
        
        Args:
            filename (str): Path to the image file
            
        Returns:
            pygame.Surface: The loaded image
        """
        try:
            image = pygame.image.load(os.path.join('assets', 'images', filename))
            return image.convert_alpha()
        except pygame.error as e:
            print(f"Error loading image {filename}: {e}")
            # Create a small surface with error pattern
            surface = pygame.Surface((32, 32))
            surface.fill((255, 0, 255))  # Magenta for missing textures
            pygame.draw.rect(surface, (0, 0, 0), (0, 0, 16, 16))
            pygame.draw.rect(surface, (0, 0, 0), (16, 16, 16, 16))
            return surface
    
    @staticmethod
    def load_sound(filename):
        """
        Load a sound file.
        
        Args:
            filename (str): Path to the sound file
            
        Returns:
            pygame.mixer.Sound: The loaded sound or None if loading fails
        """
        try:
            return pygame.mixer.Sound(os.path.join('assets', 'sounds', filename))
        except pygame.error as e:
            print(f"Error loading sound {filename}: {e}")
            return None
    
    @staticmethod
    def load_music(filename):
        """
        Load and play background music.
        
        Args:
            filename (str): Path to the music file
            
        Returns:
            bool: True if music loaded successfully, False otherwise
        """
        try:
            pygame.mixer.music.load(os.path.join('assets', 'sounds', filename))
            return True
        except pygame.error as e:
            print(f"Error loading music {filename}: {e}")
            return False
