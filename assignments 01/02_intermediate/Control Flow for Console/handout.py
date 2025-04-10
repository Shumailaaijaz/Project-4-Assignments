import random

def play_high_low_game(rounds=5):
    """
    Play the High-Low game for a specified number of rounds.
    
    Args:
        rounds: Number of rounds to play (default: 5)
    """
    print("\n===== WELCOME TO HIGH-LOW GAME =====")
    print("Try to guess if your number is higher or lower than the computer's number!")
    
    score = 0
    
    for round_num in range(1, rounds + 1):
        print(f"\n----- Round {round_num} of {rounds} -----")
        
        # Generate random numbers for player and computer
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is: {player_number}")
        print("The computer's number is hidden.")
        
        # Get player's guess
        while True:
            guess = input("Do you think your number is (h)igher or (l)ower than the computer's? ").lower()
            if guess in ['h', 'higher', 'l', 'lower']:
                break
            print("Invalid input! Please enter 'h' for higher or 'l' for lower.")
        
        # Determine the actual relationship
        if player_number > computer_number:
            actual = "higher"
        else:
            actual = "lower"
        
        # Check if the guess is correct
        is_correct = (guess in ['h', 'higher'] and actual == "higher") or (guess in ['l', 'lower'] and actual == "lower")
        
        # Reveal computer's number
        print(f"The computer's number was: {computer_number}")
        
        # Update score and provide feedback
        if is_correct:
            score += 1
            print("✓ Correct! You earned a point.")
        else:
            print("✗ Wrong! No point earned.")
        
        print(f"Current score: {score}")
    
    # Game over - display final results
    print("\n===== GAME OVER =====")
    print(f"Your final score: {score} out of {rounds}")
    
    # Provide feedback based on score
    percentage = (score / rounds) * 100
    if percentage >= 80:
        print("Excellent! You have great intuition!")
    elif percentage >= 60:
        print("Good job! You've got some skills!")
    elif percentage >= 40:
        print("Not bad! Keep practicing!")
    else:
        print("Better luck next time!")

# Allow the player to choose the number of rounds
def main():
    print("Welcome to the High-Low Game!")
    
    while True:
        try:
            rounds = int(input("How many rounds would you like to play? (1-10): "))
            if 1 <= rounds <= 10:
                break
            print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")
    
    play_high_low_game(rounds)
    
    # Ask if the player wants to play again
    while True:
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again in ['y', 'yes']:
            main()
            break
        elif play_again in ['n', 'no']:
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")

# Start the game
if __name__ == "__main__":
    main()