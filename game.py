"""
Number Guessing Game
-----------------------
The computer randomly picks a number within a given range.
Your job is to guess it in limited attempts.

Features:
- Hints (higher/lower) after each wrong guess
- 10 chances to guess
- Bonus hint (even/odd) after the 5th attempt
- High score tracking (minimum attempts used to win)
- Option to play multiple rounds
"""

import random

def number_guessing_game():
    high_score = None  # stores the fewest attempts needed to win
    
    while True:
        # Game setup
        number = random.randint(1, 100)
        attempts_left = 10
        attempts_used = 0
        print("\nGame Started!")
        print("Choose a number between 1 and 100")
        print(f"You have {attempts_left} chances.\n")

        # Game loop
        while attempts_left > 0:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            attempts_used += 1
            attempts_left -= 1

            if guess == number:
                print(f"Correct! You guessed it in {attempts_used} attempts.")

                # update high score
                if high_score is None or attempts_used < high_score:
                    high_score = attempts_used
                    print("New High Score!")

                break
            elif guess < number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

            # Bonus hint after 5th attempt
            if attempts_used == 5:
                if number % 2 == 0:
                    print("Hint: The number is EVEN.")
                else:
                    print("Hint: The number is ODD.")

            print(f"Attempts left: {attempts_left}\n")

        else:  # runs if loop ends without break
            print(f"Out of attempts! The number was {number}.")

        # Show high score
        if high_score:
            print(f"Current High Score: {high_score} attempts")

        # Replay option
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ("yes", "y"):
            print("Thanks for playing! Goodbye.")
            break

# Run the game
number_guessing_game()
