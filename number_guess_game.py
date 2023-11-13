class Game:
    """
    Number guessing game. To run, create an
    instance of class and run start_game().
    """

    def __init__(self) -> None:
        """Initialization function."""
        self.target_num: int

    def start_game(self) -> None:
        """Starts the game loop. Runs until correct number has been guessed"""
        self.target_num = random.randint(0,100)
        while True:
            guess = self._get_user_guess()
            if self.check_guess(guess):
                break
        
    def _get_user_guess(self) -> int:
        """
        Retrieves integer guess from player.

        Returns:
        value of player's guess.    
        """
        while True:
            guess = input("Please enter a positive integer between 0 and 10: ")
            try:
                if float(guess).is_integer() and int(guess) >= 0 and int(guess) <=100:
                    return int(guess)
            except:
                print("Guess was not a valid int.")
    def _check_guess(self, guess) -> bool:
        """
        Checks provided guess against the target value. Prints 'Higher' or 
        'lower' if incorrect guess. Returns true if correct.

        Returns:
        True if correct guess, false otherwise
        """
        if guess < self.target_num:
            print("Higher!\n")
            return False
        if guess > self.target_num:
            print("Lower!\n")
        print(f"Correct guess! The number was {self.target_num}")
        return True

if __name__ == "__main__":
    game: Game = Game()
    game.start_game()