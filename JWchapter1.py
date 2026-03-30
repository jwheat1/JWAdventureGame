import time
from JWglobalvariables import player, GameState

def chapter1(player, game_state):
    print("\nChapter 1: The station floated in silence...")
    explored = False
    powered = False

    while True:
        print("\nDocking Bay:")
        print("1. Explore")
        print("2. Check communications")
        print("3. Restore power")
        print("4. Go to hallway")

        choice = input("Choice: ")

        if choice == "1":
            if not explored:
                print("You find a broken robot.")
                game_state.hasCreatureData = True
                explored = True
            else:
                print("Nothing new here.")

        elif choice == "2":
            if powered:
                print("You detect a weak signal.")
            else:
                print("No signal. Try restoring power.")

        elif choice == "3":
            if not powered:
                print("Power restored.")
                game_state.hasBackupPowerCell = True
                powered = True
            else:
                print("Power already on.")

        elif choice == "4":
            if powered:
                game_state.current_chapter = 2
                break
            else:
                print("Door is locked. Restore power first.")

        else:
            print("Invalid choice.")