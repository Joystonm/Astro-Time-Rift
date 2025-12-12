# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
NEON_BLUE = (0, 191, 255)

# Player settings
PLAYER_SPEED = 5
PLAYER_SHOOT_DELAY = 250  # milliseconds
PLAYER_LIVES = 3
INVINCIBILITY_DURATION = 2000  # milliseconds

# Enemy settings
MAX_ENEMIES = 10
ENEMY_SPAWN_RATE = 1000  # milliseconds
ENEMY_SPEED_INCREASE_INTERVAL = 15000  # milliseconds
ENEMY_SPEED_INCREASE_AMOUNT = 0.5

# Bullet settings
BULLET_SPEED = 10

# Power-up settings
POWERUP_SPAWN_CHANCE = 0.2  # 20% chance when enemy is destroyed
POWERUP_DURATION = 5000  # milliseconds
POWERUP_FALL_SPEED = 2

# Time Loop Wave settings
WAVE_DURATION = 30000  # 30 seconds per wave
MAX_WAVES = 4  # Reset after 4 waves

# Scoring
SCORE_ASTEROID_DESTROYED = 10
SCORE_SURVIVAL_BONUS = 50
SCORE_SURVIVAL_INTERVAL = 30000  # milliseconds
SCORE_POWERUP_COLLECTED = 20
SCORE_HIT_PENALTY = -50

# Asset paths - using absolute paths to ensure files are found
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")

# Image files
PLAYER_IMG = os.path.join(IMAGES_DIR, "battle_ship.png")
ENEMY_IMG = os.path.join(IMAGES_DIR, "asteroid_1.png")
BULLET_IMG = os.path.join(IMAGES_DIR, "bullet.png")
BACKGROUND_IMG = os.path.join(IMAGES_DIR, "seamless_space.png")
BACKGROUND_BIG_IMG = os.path.join(IMAGES_DIR, "bg_big.png")
BACKGROUND_SPACE3_IMG = os.path.join(IMAGES_DIR, "space3.jpg")
BACKGROUND_MENU_IMG = os.path.join(IMAGES_DIR, "background_menu.jpg")
PLAYER_EXPLODED_IMG = os.path.join(IMAGES_DIR, "ship_exploded.png")

# Power-up images (we'll create colored rectangles for now)
POWERUP_DOUBLE_IMG = None  # Will create in code
POWERUP_SHIELD_IMG = None  # Will create in code
POWERUP_SPEED_IMG = None   # Will create in code
POWERUP_LIFE_IMG = None    # Will create in code

# Sound files
SHOOT_SOUND = os.path.join(SOUNDS_DIR, "shot.ogg")
EXPLOSION_SOUND = os.path.join(SOUNDS_DIR, "boom.ogg")
BACKGROUND_MUSIC = os.path.join(SOUNDS_DIR, "Cool Space Music.ogg")
POWERUP_SOUND = os.path.join(SOUNDS_DIR, "shot.ogg")  # Reusing existing sound as placeholder

# Font files
MAIN_FONT = os.path.join(FONTS_DIR, "simkai.ttf")

# Game states
STATE_SPLASH = 0
STATE_MENU = 1
STATE_INSTRUCTIONS = 2
STATE_GAMEPLAY = 3
STATE_PAUSE = 4
STATE_GAME_OVER = 5
STATE_SETTINGS = 6
STATE_BEST_SCORE = 7

# High score file
HIGH_SCORE_FILE = os.path.join(BASE_DIR, "high_score.txt")

# Energy Blast settings
ENERGY_MAX = 10
ENERGY_BLAST_RADIUS = 175
ENERGY_BLAST_DURATION = 15  # frames
BLAST_SLOW_MOTION_DURATION = 30  # frames
SCORE_BLAST_BONUS = 10  # Bonus points per asteroid destroyed by energy blast
# Energy Blast settings
ENERGY_MAX = 10
ENERGY_BLAST_RADIUS = 175
ENERGY_BLAST_DURATION = 15  # frames
BLAST_SLOW_MOTION_DURATION = 30  # frames
SCORE_BLAST_BONUS = 10  # Bonus points per asteroid destroyed by energy blast

# Sound files for Energy Blast
BLAST_SOUND = os.path.join(SOUNDS_DIR, "boom.ogg")  # Reusing explosion sound for now
# Energy Blast settings
ENERGY_MAX = 10
ENERGY_BLAST_RADIUS = 175
ENERGY_BLAST_DURATION = 15  # frames
BLAST_SLOW_MOTION_DURATION = 30  # frames
SCORE_BLAST_BONUS = 10  # Bonus points per asteroid destroyed by energy blast

# Fullscreen settings
FULLSCREEN_TRANSITION_DURATION = 300  # milliseconds
SAVE_DISPLAY_PREFERENCES = True
DISPLAY_PREFERENCES_FILE = os.path.join(BASE_DIR, "display_prefs.json")

# Multi-Stage Level settings - Time-based progression
LEVEL_DURATION = 30000  # 30 seconds per level
LEVELS = {
    1: {
        'name': 'Dawn in Space',
        'bg_gradient': [(75, 50, 125), (50, 75, 150)],  # Soft purple & blue
        'enemy_speed_multiplier': 0.8,
        'spawn_rate_multiplier': 0.7,
        'particle_color': (200, 180, 255),
        'vignette_strength': 0.0
    },
    2: {
        'name': 'Noon Nebula',
        'bg_gradient': [(255, 100, 150), (100, 200, 255)],  # Bright colorful nebula
        'enemy_speed_multiplier': 0.9,
        'spawn_rate_multiplier': 0.8,
        'particle_color': (255, 200, 100),
        'vignette_strength': 0.0
    },
    3: {
        'name': 'Dusk Void',
        'bg_gradient': [(150, 75, 50), (200, 100, 150)],  # Dark orange/pink
        'enemy_speed_multiplier': 1.4,
        'spawn_rate_multiplier': 1.3,
        'particle_color': (255, 150, 100),
        'vignette_strength': 0.3
    },
    4: {
        'name': 'Midnight Collapse',
        'bg_gradient': [(10, 10, 20), (0, 50, 100)],  # Deep black + glowing blue
        'enemy_speed_multiplier': 1.8,
        'spawn_rate_multiplier': 1.6,
        'particle_color': (100, 200, 255),
        'vignette_strength': 0.5
    }
}
MAX_LEVEL = 4
LOOP_DIFFICULTY_INCREASE = 0.1  # 10% per loop

# Weapon Evolution System
WEAPON_TYPES = {
    1: {  # Dawn - Basic Cannon
        'name': 'Basic Cannon',
        'bullet_count': 1,
        'bullet_speed': 10,
        'bullet_color': (100, 150, 255),
        'bullet_size': (4, 8),
        'spread': 0,
        'damage': 1
    },
    2: {  # Noon - Double Laser
        'name': 'Double Laser',
        'bullet_count': 2,
        'bullet_speed': 12,
        'bullet_color': (255, 255, 100),
        'bullet_size': (3, 12),
        'spread': 15,
        'damage': 1
    },
    3: {  # Dusk - Plasma Bursts
        'name': 'Plasma Bursts',
        'bullet_count': 3,
        'bullet_speed': 8,
        'bullet_color': (255, 100, 255),
        'bullet_size': (6, 6),
        'spread': 25,
        'damage': 2
    },
    4: {  # Midnight - Dark-matter Railgun
        'name': 'Dark-matter Railgun',
        'bullet_count': 1,
        'bullet_speed': 20,
        'bullet_color': (150, 50, 255),
        'bullet_size': (8, 20),
        'spread': 0,
        'damage': 3
    }
}
