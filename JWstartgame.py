from JWglobalvariables import player, creature, GameState

import JWchapter1
import JWchapter2
import JWchapter3
import JWchapter4
import JWchapter5

def main():
    game_state = GameState()

    while not game_state.game_ended:
        chapter = game_state.current_chapter

        if chapter == 1:
            JWchapter1.chapter1(player, game_state)
        elif chapter == 2:
            JWchapter2.chapter2(player, game_state)
        elif chapter == 3:
            JWchapter3.chapter3(player, creature, game_state)
        elif chapter == 4:
            JWchapter4.chapter4(player, creature, game_state)
        elif chapter == 5:
            JWchapter5.chapter5(player, creature, game_state)
        else:
            print("Invalid chapter. Ending the game.")
            game_state.game_ended = True

if __name__ == "__main__":
    main()