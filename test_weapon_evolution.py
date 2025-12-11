#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'AstroSpace'))

from config import WEAPON_TYPES

def test_weapon_evolution():
    """Test the weapon evolution system configuration"""
    print("Testing Weapon Evolution System")
    print("=" * 40)
    
    # Test all weapon types
    for level in range(1, 5):
        weapon = WEAPON_TYPES[level]
        print(f"\nLevel {level} - {weapon['name']}:")
        print(f"  Bullet Count: {weapon['bullet_count']}")
        print(f"  Bullet Speed: {weapon['bullet_speed']}")
        print(f"  Bullet Color: {weapon['bullet_color']}")
        print(f"  Bullet Size: {weapon['bullet_size']}")
        print(f"  Spread: {weapon['spread']}°")
        print(f"  Damage: {weapon['damage']}")
    
    print("\n" + "=" * 40)
    print("Weapon Evolution Test Complete!")

if __name__ == "__main__":
    test_weapon_evolution()
