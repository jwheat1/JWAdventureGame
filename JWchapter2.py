import time
from JWglobalvariables import player, GameState

def chapter2(player, game_state):
    print("\nChapter 2: The hallway echoes...")
    found_log = False

    while True:
        print("\nLaboratory:")
        print("1. Search lab")
        print("2. Listen to log")
        print("3. Continue forward")
        print("4. Go back")

        choice = input("Choice: ")

        if choice == "1":
            if not found_log:
                print("You found a data log!")
                game_state.hasDataLog = True
                found_log = True
            else:
                print("Nothing else found.")

        elif choice == "2":
            if game_state.hasDataLog:
                print("The log reveals a dangerous experiment.")
            else:
                print("You need the log first.")

        elif choice == "3":
            game_state.current_chapter = 3
            break

        elif choice == "4":
            game_state.current_chapter = 1
            break

        else:
            print("Invalid choice.")