# Astro Space - Game Jam Submission

## Game Overview

Astro Space is a 2D space shooter that explores "The Changing of Time" through a dynamic progression system where players experience the passage of time across four distinct cosmic phases. Each phase lasts exactly 30 seconds and represents a different time of day in space, from the gentle Dawn through vibrant Noon, intense Dusk, to the chaotic Midnight. The game creates an endless temporal loop where time accelerates with each cycle, making survival increasingly challenging.

## Theme Implementation

The game embodies "The Changing of Time" by making time progression the core mechanic. Players witness the visual transformation of space as they move through Dawn's purple-blue serenity, Noon's bright nebula colors, Dusk's orange twilight with atmospheric vignette, and Midnight's dark void with electric effects. After completing all four phases, time loops back to Dawn but with 10% increased difficulty, creating an infinite cycle where players must adapt to the ever-accelerating pace of time itself.

Install pygame and run the game from the AstroSpace directory using `python main.py`. Control your spaceship with arrow keys or WASD, fire bullets with spacebar, and use X for energy blasts. The game automatically progresses through time phases every 30 seconds, with each phase bringing unique visuals and increasing difficulty. Survive as long as possible while time loops infinitely, each cycle making the cosmic chaos more intense.

## Technical Details

Built with Python and Pygame, the game features a sophisticated time-based level system with dynamic gradient backgrounds, particle effects, and atmospheric rendering. Each time phase has distinct visual identity through color gradients, particle systems, and screen effects like vignetting. The temporal loop system scales difficulty exponentially while maintaining smooth 60 FPS performance through optimized rendering techniques.

**GitHub Repository**: https://github.com/your-username/Astro-Time-Rift  
**Run Instructions**: `cd AstroSpace && python main.py`

Astro Space transforms the classic arcade shooter by making time itself the ultimate challenge, where survival depends on adapting to the relentless march of cosmic time.
