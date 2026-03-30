import time
from JWglobalvariables import player, GameState

def chapter5(player, game_state):
    print("\nChapter 5: Final decision...")

    while True:
        print("\n1. Read message")
        print("2. Send report (Good)")
        print("3. Delete data (Secret)")
        print("4. Shutdown station (Neutral)")

        choice = input("Choice: ")

        if choice == "1":
            print("The experiment went wrong...")

        elif choice == "2":
            print("Good ending achieved!")
            game_state.game_ended = True
            break

        elif choice == "3":
            print("Secret ending achieved!")
            game_state.game_ended = True
            break

        elif choice == "4":
            print("Neutral ending achieved.")
            game_state.game_ended = True
            break

        else:
            print("Invalid choice.")
