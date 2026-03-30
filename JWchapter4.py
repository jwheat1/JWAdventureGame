import time
from JWglobalvariables import player, creature, GameState

def chapter4(player, creature, game_state):
    print("\nChapter 4: Control room locked.")

    while True:
        print("\nControl Door:")
        print("1. Use data log")
        print("2. Force door")
        print("3. Use power cell")
        print("4. Go back")

        choice = input("Choice: ")

        if choice == "1":
            if game_state.hasDataLog:
                print("Door unlocked!")
                game_state.current_chapter = 5
                break
            else:
                print("Need data log.")

        elif choice == "2":
            print("Alarm triggered! Creature attacks!")
            player.update_health(-15)

        elif choice == "3":
            if game_state.hasBackupPowerCell:
                print("Door powered open!")
                game_state.current_chapter = 5
                break
            else:
                print("No power cell.")

        elif choice == "4":
            game_state.current_chapter = 3
            break

        else:
            print("Invalid choice.")

        if player.get_health() <= 0:
            print("You died.")
            game_state.game_ended = True
            break