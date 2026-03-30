# Space Adventure Game - Technical Documentation

## 1. Code Hosting
- Hosted on GitHub: https://github.com/YourUsername/SpaceAdventureGame
- Folder contents:
  JWglobalvariables.py
  JWchapter1.py
  JWchapter2.py
  JWchapter3.py
  JWchapter4.py
  JWchapter5.py
  JWstartgame.py
  readme.txt

## 2. External Services
- None required; runs entirely in Python console.

## 3. Languages and Technologies
- Python 3.x
- Libraries used: 
  - random
  - time

## 4. System Requirements
- Python 3 installed
- Works on Windows, MacOS, Linux
- Optional: Visual Studio Code for editing

## 5. Coding / Naming Conventions
- Class names: CamelCase (Player, Creature, GameState)
- Function names: snake_case (chapter1, chapter2, etc.)
- File names: lowercase, no spaces, prefixed with JW (JWchapter1.py)
- Indentation: 4 spaces

## 6. How to Run
1. Open terminal in folder containing JWstartgame.py
2. Run: `python3 JWstartgame.py`
3. Use number inputs (1-4) to choose actions

## 7. Architecture Overview
- JWglobalvariables.py: Class definitions and global objects
- JWchapterX.py: Each chapter’s events and interactions
- JWstartgame.py: Main game loop; calls chapter functions based on current_chapter

## 8. Starting the Game
- Game starts in Chapter 1 with a welcome message
- Player choices affect story and ending
- Multiple endings: Good (report to Earth), Secret (delete data), Neutral (shut down station)

## 9. Additional Notes
- Player health and inventory are tracked across chapters
- Loops and if-elif-else statements allow repeated actions and branching decisions