import time

def chapter3(player, creature, game_state):
    game_state.current_chapter = 3

    print("Chapter 3: A red warning light flashed ahead: Lifeform Detected!")
    time.sleep(2)

    while True:
        print("\nYou are in the Greenhouse.")
        print("Actions:")
        print("1. Fight the creature")
        print("2. Hide and sneak past")
        print("3. Run back to Main Hallway")
        print("4. Scan the creature")

        choice = input("Choose an action (1-4): ")

        if choice == "1":
            print("You engage the creature in combat! It fights back but is injured.")
            creature.update_health(20)
            print(f"Creature remaining health: {creature.get_health()}")
            time.sleep(2)
            print("Path cleared. You move forward to the Control Room.")
            game_state.current_chapter = 4
            break

        elif choice == "2":
            print("You try to hide. The creature notices you! You are slightly injured.")
            player.update_health(-10)
            print(f"Your health: {player.get_health()}")
            time.sleep(2)

        elif choice == "3":
            print("You retreat to the Main Hallway.")
            game_state.current_chapter = 2
            time.sleep(2)
            break

        elif choice == "4":
            print("You scan the creature and learn it was created in the lab!")
            game_state.hasCreatureData = True
            time.sleep(2)

        else:
            print("Invalid choice. Please choose 1-4.")