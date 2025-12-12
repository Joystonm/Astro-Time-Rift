#!/usr/bin/env python3
"""
Script to fix main.py for PyGBag compatibility
"""

def fix_main_py():
    # Read the current main.py
    with open('main.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add asyncio import if not present
    if 'import asyncio' not in content:
        content = content.replace('import json', 'import json\nimport asyncio')
    
    # Convert run method to async
    old_run = '''    def run(self):
        """Main game loop"""
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)'''
    
    new_run = '''    async def run(self):
        """Main game loop"""
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
            await asyncio.sleep(0)'''
    
    content = content.replace(old_run, new_run)
    
    # Fix the main execution
    old_main = '''if __name__ == "__main__":
    game = Game()
    game.run()'''
    
    new_main = '''if __name__ == "__main__":
    game = Game()
    asyncio.run(game.run())'''
    
    content = content.replace(old_main, new_main)
    
    # Write back the fixed content
    with open('main.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed main.py for PyGBag compatibility")

if __name__ == "__main__":
    fix_main_py()
