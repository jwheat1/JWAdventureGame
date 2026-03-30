import time
import random
from JWglobalvariables import player, creature, GameState

def chapter3(player, creature, game_state):
    print("\nChapter 3: Lifeform detected!")

    while True:
        print("\nGreenhouse:")
        print("1. Fight")
        print("2. Hide")
        print("3. Run")
        print("4. Scan")

        choice = input("Choice: ")

        if choice == "1":
            damage = random.randint(10, 25)
            creature.update_health(damage)
            print(f"You hit the creature for {damage}")

            if creature.get_health() <= 0:
                print("Creature defeated!")
                game_state.current_chapter = 4
                break
            else:
                player.update_health(-10)
                print("It hits back!")

        elif choice == "2":
            print("You hide but get hurt.")
            player.update_health(-5)

        elif choice == "3":
            game_state.current_chapter = 2
            break

        elif choice == "4":
            print("It was created in the lab.")
            game_state.hasCreatureData = True

        else:
            print("Invalid choice.")

        if player.get_health() <= 0:
            print("You died.")
            game_state.game_ended = True
            break