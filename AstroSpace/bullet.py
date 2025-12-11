import pygame
import math
from config import *

class Bullet:
    def __init__(self, x, y, direction, weapon_type=1, angle=0):
        self.weapon_type = weapon_type
        weapon_config = WEAPON_TYPES.get(weapon_type, WEAPON_TYPES[1])
        
        # Set bullet size based on weapon type
        bullet_size = weapon_config['bullet_size']
        self.rect = pygame.Rect(0, 0, bullet_size[0], bullet_size[1])
        self.rect.centerx = x
        self.rect.centery = y
        
        # Direction: -1 for up (player bullet), 1 for down (enemy bullet)
        self.direction = direction
        self.speed = weapon_config['bullet_speed']
        self.damage = weapon_config['damage']
        
        # Handle angled shots for spread weapons
        self.angle = angle
        self.dx = math.sin(math.radians(angle)) * self.speed
        self.dy = direction * self.speed * math.cos(math.radians(angle))
        
        # Bullet color based on weapon type
        self.color = weapon_config['bullet_color'] if direction < 0 else RED
    
    def update(self):
        # Move the bullet with angle consideration
        if self.angle != 0:
            self.rect.x += self.dx
            self.rect.y += self.dy
        else:
            self.rect.y += self.direction * self.speed
    
    def is_off_screen(self):
        # Check if the bullet has gone off the screen
        return (self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT or 
                self.rect.right < 0 or self.rect.left > SCREEN_WIDTH)
    
    def check_collision(self, sprite):
        # Check if the bullet has collided with another sprite
        return self.rect.colliderect(sprite.rect)
    
    def draw(self, surface):
        # Draw different bullet shapes based on weapon type
        if self.weapon_type == 4:  # Dark-matter railgun - draw with glow effect
            # Draw glow
            glow_rect = self.rect.inflate(4, 4)
            glow_color = tuple(min(255, c + 50) for c in self.color)
            pygame.draw.ellipse(surface, glow_color, glow_rect)
            pygame.draw.rect(surface, self.color, self.rect)
        elif self.weapon_type == 3:  # Plasma bursts - circular
            pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width // 2)
        else:  # Basic cannon and double laser - rectangular
            pygame.draw.rect(surface, self.color, self.rect)
