# JWAdventureGame

Adventure Game – Technical Documentation


1. Code Hosting
- GitHub: https://github.com/jwheat1/JWAdventureGame

2. Languages and Technologies
- Python 3, console-based interactive game

3. System Requirements
- Python 3.x installed
- Works on Windows, Mac, or Linux
- Terminal or command prompt access

4. Coding/Naming Conventions
- Classes use PascalCase (Player, Creature, GameState)
- Variables use lowercase_with_underscores
- Functions use lowercase_with_underscores
- Each chapter in a separate Python file
- Main game flow controlled in JWstartgame.py

5. How to Run
- Run locally: `python JWstartgame.py` from terminal

6. Architecture Overview
- `JWstartgame.py` controls game loop and chapter transitions
- `JWglobalvariables.py` defines Player, Creature, and GameState classes
- Chapters (`JWchapter1.py` to `JWchapter5.py`) contain story logic
- Player progression tracked via `GameState.current_chapter` and flags

7. How to Start the Game
- Run JWstartgame.py in console
- Follow the prompts in each chapter
- Make choices using numbers 1-4
- Game ends when Chapter 5 conclusion is reached
- Multiple endings depending on player decisions

8. Notes for Developers / Administrators
- To add new chapters, create a new `.py` file and update main loop
- Global flags in GameState control progression and inventory
- Creature and Player classes store dynamic stats (health, items)
- Use time.sleep(seconds) for narrative pacing
