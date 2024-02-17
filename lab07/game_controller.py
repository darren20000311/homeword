from pair_of_dice import PairOfDice


class GameController:
    def __init__(self):
        self.pair_of_dice = PairOfDice()
        self.point = None

    def welcome_message(self):
        print("Welcome to street craps!\n")
        print("Rules:")
        print("If you roll 7 or 11 on your first roll, you win.")
        print("If you roll 2, 3, or 12 on your first roll, you lose.")
        print("If you roll anything else, that's your point, ")
        print("and you keep rolling until you either roll your point")
        print("again (win) or roll a 7 (lose)\n")

    def roll_initial_dice(self):
        input("Press enter to roll the dice...")
        self.pair_of_dice.roll_dice()
        roll_sum = self.pair_of_dice.current_value()
        print(f"\nYou rolled {roll_sum}.")

        if roll_sum == 7 or roll_sum == 11:
            print("You win!")
        elif roll_sum == 2 or roll_sum == 3 or roll_sum == 12:
            print("You lose!")
        else:
            self.point = roll_sum
            print(f"\nYour point is {self.point}.")
            self.keep_rolling()
    
    def keep_rolling(self):
        while True:
            input("Press enter to roll the dice...")
            self.pair_of_dice.roll_dice()
            roll_sum = self.pair_of_dice.current_value()
            print(f"\nYou rolled {roll_sum}")

            if roll_sum == self.point:
                print("You win!")
                break
            elif roll_sum == 7:
                print("You lose!")
                break
