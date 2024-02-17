from game_controller import GameController


def main():
    game = GameController()
    game.welcome_message()
    game.roll_initial_dice()


if __name__ == "__main__":
    main()