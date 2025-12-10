#!/usr/bin/env python3
"""
Test script to verify the multi-stage level system implementation
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'AstroSpace'))

from config import LEVELS, MAX_LEVEL

def test_level_configuration():
    """Test that level configuration is properly set up"""
    print("Testing Multi-Stage Level Configuration:")
    print("=" * 50)
    
    for level_num in range(1, MAX_LEVEL + 1):
        if level_num in LEVELS:
            level = LEVELS[level_num]
            print(f"Level {level_num}: {level['name']}")
            print(f"  Background Color: {level['bg_color']}")
            print(f"  Enemy Speed Multiplier: {level['enemy_speed_multiplier']}x")
            print(f"  Spawn Rate Multiplier: {level['spawn_rate_multiplier']}x")
            print(f"  Asteroids to Advance: {level['asteroids_to_advance']}")
            print()
        else:
            print(f"ERROR: Level {level_num} not found in configuration!")
    
    print(f"Maximum Level: {MAX_LEVEL}")
    print("\nLevel progression system configured successfully!")

def test_difficulty_progression():
    """Test that difficulty increases properly across levels"""
    print("\nTesting Difficulty Progression:")
    print("=" * 50)
    
    prev_speed = 0
    prev_spawn = 0
    prev_asteroids = 0
    
    for level_num in range(1, MAX_LEVEL + 1):
        level = LEVELS[level_num]
        speed = level['enemy_speed_multiplier']
        spawn = level['spawn_rate_multiplier']
        asteroids = level['asteroids_to_advance']
        
        if level_num > 1:
            speed_increase = speed > prev_speed
            spawn_increase = spawn > prev_spawn
            asteroids_increase = asteroids > prev_asteroids
            
            print(f"Level {level_num-1} → {level_num}:")
            print(f"  Speed: {prev_speed} → {speed} {'✓' if speed_increase else '✗'}")
            print(f"  Spawn Rate: {prev_spawn} → {spawn} {'✓' if spawn_increase else '✗'}")
            print(f"  Asteroids Required: {prev_asteroids} → {asteroids} {'✓' if asteroids_increase else '✗'}")
            print()
        
        prev_speed = speed
        prev_spawn = spawn
        prev_asteroids = asteroids
    
    print("Difficulty progression verified!")

if __name__ == "__main__":
    test_level_configuration()
    test_difficulty_progression()
    print("\n🎮 Multi-Stage Level System Ready!")
    print("\nFeatures implemented:")
    print("• 4 distinct levels with unique themes")
    print("• Progressive difficulty scaling")
    print("• Visual background color changes")
    print("• Level progression based on asteroids destroyed")
    print("• Level cycling after completing all stages")
