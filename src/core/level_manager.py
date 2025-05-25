import json
import os

class LevelManager:
    def __init__(self):
        self.levels = {}
        self.current_level = 1
        
        # Create default levels if level files don't exist
        self.create_default_levels()
        
        # Load all levels
        self.load_all_levels()
    
    def create_default_levels(self):
        # Level 1 - Tutorial level
        level1 = {
            'level_width': 3200,
            'player_start_x': 100,
            'player_start_y': 400,
            'flagpole_x': 3000,
            'platforms': [
                # Ground
                {'x': 0, 'y': 500, 'width': 800, 'height': 100, 'type': 'ground'},
                {'x': 900, 'y': 500, 'width': 400, 'height': 100, 'type': 'ground'},
                {'x': 1400, 'y': 500, 'width': 1800, 'height': 100, 'type': 'ground'},
                
                # Platforms
                {'x': 500, 'y': 350, 'width': 100, 'height': 50, 'type': 'brick'},
                {'x': 700, 'y': 250, 'width': 100, 'height': 50, 'type': 'brick'},
                {'x': 1200, 'y': 350, 'width': 100, 'height': 50, 'type': 'brick'},
                
                # Pipes
                {'x': 600, 'y': 400, 'width': 80, 'height': 100, 'type': 'pipe'},
                {'x': 1600, 'y': 400, 'width': 80, 'height': 100, 'type': 'pipe'},
                {'x': 2200, 'y': 400, 'width': 80, 'height': 100, 'type': 'pipe'}
            ],
            'enemies': [
                {'x': 400, 'y': 470, 'type': 'goomba'},
                {'x': 1000, 'y': 470, 'type': 'goomba'},
                {'x': 1800, 'y': 470, 'type': 'goomba'},
                {'x': 2400, 'y': 470, 'type': 'goomba'}
            ],
            'coins': [
                {'x': 300, 'y': 400},
                {'x': 350, 'y': 400},
                {'x': 400, 'y': 400},
                {'x': 1000, 'y': 400},
                {'x': 1050, 'y': 400},
                {'x': 1100, 'y': 400},
                {'x': 1800, 'y': 350},
                {'x': 1850, 'y': 350},
                {'x': 1900, 'y': 350},
                {'x': 2500, 'y': 400},
                {'x': 2550, 'y': 400},
                {'x': 2600, 'y': 400}
            ],
            'question_blocks': [
                {'x': 500, 'y': 300, 'content': 'coin'},
                {'x': 700, 'y': 200, 'content': 'coin'},
                {'x': 1200, 'y': 300, 'content': 'coin'},
                {'x': 2000, 'y': 300, 'content': 'coin'}
            ]
        }
        
        # Level 2 - More challenging
        level2 = {
            'level_width': 4000,
            'player_start_x': 100,
            'player_start_y': 400,
            'flagpole_x': 3800,
            'platforms': [
                # Ground with gaps
                {'x': 0, 'y': 500, 'width': 600, 'height': 100, 'type': 'ground'},
                {'x': 700, 'y': 500, 'width': 400, 'height': 100, 'type': 'ground'},
                {'x': 1200, 'y': 500, 'width': 300, 'height': 100, 'type': 'ground'},
                {'x': 1600, 'y': 500, 'width': 400, 'height': 100, 'type': 'ground'},
                {'x': 2100, 'y': 500, 'width': 500, 'height': 100, 'type': 'ground'},
                {'x': 2700, 'y': 500, 'width': 1300, 'height': 100, 'type': 'ground'},
                
                # Elevated platforms
                {'x': 900, 'y': 350, 'width': 200, 'height': 50, 'type': 'brick'},
                {'x': 1300, 'y': 300, 'width': 100, 'height': 50, 'type': 'brick'},
                {'x': 1700, 'y': 350, 'width': 200, 'height': 50, 'type': 'brick'},
                {'x': 2200, 'y': 250, 'width': 300, 'height': 50, 'type': 'brick'},
                
                # Pipes
                {'x': 500, 'y': 400, 'width': 80, 'height': 100, 'type': 'pipe'},
                {'x': 1400, 'y': 400, 'width': 80, 'height': 100, 'type': 'pipe'},
                {'x': 2000, 'y': 400, 'width': 80, 'height': 100, 'type': 'pipe'},
                {'x': 2600, 'y': 350, 'width': 80, 'height': 150, 'type': 'pipe'},
                {'x': 3200, 'y': 300, 'width': 80, 'height': 200, 'type': 'pipe'}
            ],
            'enemies': [
                {'x': 400, 'y': 470, 'type': 'goomba'},
                {'x': 800, 'y': 470, 'type': 'goomba'},
                {'x': 1000, 'y': 320, 'type': 'goomba'},
                {'x': 1300, 'y': 270, 'type': 'goomba'},
                {'x': 1800, 'y': 320, 'type': 'goomba'},
                {'x': 2300, 'y': 220, 'type': 'goomba'},
                {'x': 2400, 'y': 220, 'type': 'goomba'},
                {'x': 2800, 'y': 470, 'type': 'koopa'},
                {'x': 3300, 'y': 470, 'type': 'koopa'}
            ],
            'coins': [
                {'x': 300, 'y': 400},
                {'x': 350, 'y': 400},
                {'x': 850, 'y': 400},
                {'x': 900, 'y': 400},
                {'x': 950, 'y': 250},
                {'x': 1000, 'y': 250},
                {'x': 1050, 'y': 250},
                {'x': 1750, 'y': 250},
                {'x': 1800, 'y': 250},
                {'x': 1850, 'y': 250},
                {'x': 2250, 'y': 150},
                {'x': 2300, 'y': 150},
                {'x': 2350, 'y': 150},
                {'x': 2400, 'y': 150},
                {'x': 2450, 'y': 150},
                {'x': 3000, 'y': 400},
                {'x': 3050, 'y': 400},
                {'x': 3100, 'y': 400},
                {'x': 3400, 'y': 400},
                {'x': 3450, 'y': 400},
                {'x': 3500, 'y': 400}
            ],
            'question_blocks': [
                {'x': 400, 'y': 300, 'content': 'coin'},
                {'x': 950, 'y': 200, 'content': 'coin'},
                {'x': 1350, 'y': 150, 'content': 'coin'},
                {'x': 1800, 'y': 200, 'content': 'coin'},
                {'x': 2350, 'y': 100, 'content': 'coin'},
                {'x': 3000, 'y': 300, 'content': 'coin'}
            ]
        }
        
        # Level 3 - Most challenging
        level3 = {
            'level_width': 5000,
            'player_start_x': 100,
            'player_start_y': 400,
            'flagpole_x': 4800,
            'platforms': [
                # Ground with larger gaps
                {'x': 0, 'y': 500, 'width': 500, 'height': 100, 'type': 'ground'},
                {'x': 600, 'y': 500, 'width': 300, 'height': 100, 'type': 'ground'},
                {'x': 1000, 'y': 500, 'width': 200, 'height': 100, 'type': 'ground'},
                {'x': 1300, 'y': 500, 'width': 300, 'height': 100, 'type': 'ground'},
                {'x': 1700, 'y': 500, 'width': 400, 'height': 100, 'type': 'ground'},
                {'x': 2200, 'y': 500, 'width': 300, 'height': 100, 'type': 'ground'},
                {'x': 2600, 'y': 500, 'width': 200, 'height': 100, 'type': 'ground'},
                {'x': 2900, 'y': 500, 'width': 400, 'height': 100, 'type': 'ground'},
                {'x': 3400, 'y': 500, 'width': 300, 'height': 100, 'type': 'ground'},
                {'x': 3800, 'y': 500, 'width': 1200, 'height': 100, 'type': 'ground'},
                
                # Complex platform arrangement
                {'x': 400, 'y': 350, 'width': 100, 'height': 50, 'type': 'brick'},
                {'x': 550, 'y': 250, 'width': 100, 'height': 50, 'type': 'brick'},
                {'x': 700, 'y': 150, 'width': 100, 'height': 50, 'type': 'brick'},
                {'x': 850, 'y': 250, 'width': 100, 'height': 50, 'type': 'brick'},
                {'x': 1000, 'y': 350, 'width': 100, 'height': 50, 'type': 'brick'},
                
                {'x': 1400, 'y': 350, 'width': 100, 'height': 50, 'type': 'brick'},
                {'x': 1600, 'y': 250, 'width': 100, 'height': 50, 'type': 'brick'},
                
                {'x': 2000, 'y': 350, 'width': 100, 'height': 50, 'type': 'brick'},
                {'x': 2300, 'y': 250, 'width': 100, 'height': 50, 'type': 'brick'},
                {'x': 2500, 'y': 150, 'width': 100, 'height': 50, 'type': 'brick'},
                
                {'x': 3000, 'y': 350, 'width': 200, 'height': 50, 'type': 'brick'},
                {'x': 3300, 'y': 250, 'width': 200, 'height': 50, 'type': 'brick'},
                {'x': 3600, 'y': 350, 'width': 100, 'height': 50, 'type': 'brick'},
                
                # Pipes
                {'x': 300, 'y': 400, 'width': 80, 'height': 100, 'type': 'pipe'},
                {'x': 1200, 'y': 350, 'width': 80, 'height': 150, 'type': 'pipe'},
                {'x': 1900, 'y': 400, 'width': 80, 'height': 100, 'type': 'pipe'},
                {'x': 2700, 'y': 350, 'width': 80, 'height': 150, 'type': 'pipe'},
                {'x': 3500, 'y': 300, 'width': 80, 'height': 200, 'type': 'pipe'},
                {'x': 4200, 'y': 400, 'width': 80, 'height': 100, 'type': 'pipe'}
            ],
            'enemies': [
                {'x': 400, 'y': 470, 'type': 'goomba'},
                {'x': 700, 'y': 470, 'type': 'goomba'},
                {'x': 850, 'y': 220, 'type': 'goomba'},
                {'x': 1100, 'y': 470, 'type': 'koopa'},
                {'x': 1500, 'y': 320, 'type': 'goomba'},
                {'x': 1600, 'y': 220, 'type': 'goomba'},
                {'x': 1800, 'y': 470, 'type': 'koopa'},
                {'x': 2000, 'y': 320, 'type': 'goomba'},
                {'x': 2300, 'y': 220, 'type': 'goomba'},
                {'x': 2400, 'y': 470, 'type': 'koopa'},
                {'x': 3100, 'y': 320, 'type': 'goomba'},
                {'x': 3400, 'y': 220, 'type': 'koopa'},
                {'x': 3900, 'y': 470, 'type': 'goomba'},
                {'x': 4000, 'y': 470, 'type': 'goomba'},
                {'x': 4100, 'y': 470, 'type': 'koopa'},
                {'x': 4300, 'y': 470, 'type': 'koopa'},
                {'x': 4500, 'y': 470, 'type': 'koopa'}
            ],
            'coins': [
                # Coin paths and formations
                {'x': 200, 'y': 400},
                {'x': 250, 'y': 380},
                {'x': 300, 'y': 360},
                {'x': 350, 'y': 340},
                {'x': 400, 'y': 320},
                
                {'x': 700, 'y': 120},
                {'x': 750, 'y': 120},
                {'x': 800, 'y': 120},
                
                {'x': 1050, 'y': 320},
                {'x': 1100, 'y': 320},
                {'x': 1150, 'y': 320},
                
                {'x': 1600, 'y': 200},
                {'x': 1650, 'y': 200},
                
                {'x': 2000, 'y': 300},
                {'x': 2050, 'y': 300},
                {'x': 2100, 'y': 300},
                
                {'x': 2500, 'y': 100},
                {'x': 2550, 'y': 100},
                {'x': 2600, 'y': 100},
                
                {'x': 3000, 'y': 300},
                {'x': 3050, 'y': 300},
                {'x': 3100, 'y': 300},
                {'x': 3150, 'y': 300},
                
                {'x': 3300, 'y': 200},
                {'x': 3350, 'y': 200},
                {'x': 3400, 'y': 200},
                {'x': 3450, 'y': 200},
                
                {'x': 4000, 'y': 400},
                {'x': 4050, 'y': 380},
                {'x': 4100, 'y': 360},
                {'x': 4150, 'y': 340},
                {'x': 4200, 'y': 320},
                {'x': 4250, 'y': 340},
                {'x': 4300, 'y': 360},
                {'x': 4350, 'y': 380},
                {'x': 4400, 'y': 400}
            ],
            'question_blocks': [
                {'x': 400, 'y': 300, 'content': 'coin'},
                {'x': 700, 'y': 100, 'content': 'coin'},
                {'x': 1100, 'y': 300, 'content': 'coin'},
                {'x': 1600, 'y': 150, 'content': 'coin'},
                {'x': 2050, 'y': 250, 'content': 'coin'},
                {'x': 2500, 'y': 50, 'content': 'coin'},
                {'x': 3100, 'y': 250, 'content': 'coin'},
                {'x': 3400, 'y': 150, 'content': 'coin'},
                {'x': 4200, 'y': 300, 'content': 'coin'}
            ]
        }
        
        # Save levels to files
        if not os.path.exists('levels'):
            os.makedirs('levels')
        
        with open(os.path.join('levels', 'level1.json'), 'w') as f:
            json.dump(level1, f, indent=4)
        
        with open(os.path.join('levels', 'level2.json'), 'w') as f:
            json.dump(level2, f, indent=4)
        
        with open(os.path.join('levels', 'level3.json'), 'w') as f:
            json.dump(level3, f, indent=4)
    
    def load_all_levels(self):
        # Load all level files
        level_files = [f for f in os.listdir('levels') if f.startswith('level') and f.endswith('.json')]
        
        for level_file in sorted(level_files):
            level_number = int(level_file.replace('level', '').replace('.json', ''))
            with open(os.path.join('levels', level_file), 'r') as f:
                self.levels[level_number] = json.load(f)
    
    def load_level(self, level_number):
        self.current_level = level_number
        return self.levels[level_number]
    
    def get_current_level(self):
        return self.levels[self.current_level]
    
    def get_level_count(self):
        return len(self.levels)
