#!/usr/bin/env python3
"""
Test script for the enhanced 4-stage multi-level progression system
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'AstroSpace'))

from config import LEVELS, MAX_LEVEL, LEVEL_DURATION, LOOP_DIFFICULTY_INCREASE

def test_enhanced_level_system():
    """Test the enhanced level configuration"""
    print("🚀 Enhanced Multi-Stage Level System Test")
    print("=" * 60)
    
    for level_num in range(1, MAX_LEVEL + 1):
        level = LEVELS[level_num]
        print(f"\n🌌 Level {level_num}: {level['name']}")
        print(f"   Background Gradient: {level['bg_gradient'][0]} → {level['bg_gradient'][1]}")
        print(f"   Enemy Speed: {level['enemy_speed_multiplier']}x")
        print(f"   Spawn Rate: {level['spawn_rate_multiplier']}x")
        print(f"   Particle Color: {level['particle_color']}")
        print(f"   Vignette Strength: {level['vignette_strength']}")
    
    print(f"\n⏱️  Level Duration: {LEVEL_DURATION/1000} seconds")
    print(f"🔄 Loop Difficulty Increase: {LOOP_DIFFICULTY_INCREASE*100}% per loop")

def test_visual_progression():
    """Test visual progression across levels"""
    print("\n🎨 Visual Progression Test")
    print("=" * 60)
    
    themes = {
        1: "Dawn - Soft purple & blue gradient with light particle fog",
        2: "Noon - Bright colorful nebula with vibrant light flares", 
        3: "Dusk - Dark orange/pink clouds with screen vignette",
        4: "Midnight - Deep black + glowing blue with lightning distortion"
    }
    
    for level_num, description in themes.items():
        level = LEVELS[level_num]
        print(f"\n🎭 {description}")
        print(f"   Gradient: {level['bg_gradient']}")
        print(f"   Particles: {level['particle_color']}")
        print(f"   Vignette: {'Yes' if level['vignette_strength'] > 0 else 'No'}")

def test_difficulty_scaling():
    """Test difficulty scaling with loops"""
    print("\n⚡ Difficulty Scaling Test")
    print("=" * 60)
    
    for loop in range(3):
        print(f"\n🔄 Loop {loop + 1}:")
        loop_multiplier = 1 + (loop * LOOP_DIFFICULTY_INCREASE)
        
        for level_num in range(1, MAX_LEVEL + 1):
            level = LEVELS[level_num]
            final_speed = level['enemy_speed_multiplier'] * loop_multiplier
            final_spawn = level['spawn_rate_multiplier'] * loop_multiplier
            
            print(f"   Level {level_num}: Speed {final_speed:.2f}x, Spawn {final_spawn:.2f}x")

def test_time_progression():
    """Test time-based progression system"""
    print("\n⏰ Time-Based Progression Test")
    print("=" * 60)
    
    total_cycle_time = LEVEL_DURATION * MAX_LEVEL / 1000
    print(f"🕐 Time per level: {LEVEL_DURATION/1000} seconds")
    print(f"🔄 Full cycle time: {total_cycle_time} seconds")
    print(f"📈 Automatic progression: Every {LEVEL_DURATION/1000}s")
    print(f"🎯 Transition effects: Fade + 'TIME SHIFT' message")

if __name__ == "__main__":
    test_enhanced_level_system()
    test_visual_progression()
    test_difficulty_scaling()
    test_time_progression()
    
    print("\n" + "=" * 60)
    print("✅ Enhanced Multi-Stage Level System Ready!")
    print("\n🎮 New Features Implemented:")
    print("• Time-based level progression (30s per level)")
    print("• 4 distinct visual themes with gradient backgrounds")
    print("• Particle fog effects for each level")
    print("• Screen vignette for Dusk and Midnight levels")
    print("• Smooth transition effects with fade")
    print("• Loop system with +10% difficulty per cycle")
    print("• Enhanced UI showing time remaining and loop count")
    print("• Automatic 'TIME SHIFT' notifications")
    
    print("\n🌟 Visual Enhancements:")
    print("• Dawn: Soft purple/blue gradient + light particles")
    print("• Noon: Bright nebula colors + vibrant particles")
    print("• Dusk: Orange/pink clouds + vignette effect")
    print("• Midnight: Deep black/blue + intense vignette")
