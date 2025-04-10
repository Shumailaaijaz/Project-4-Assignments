import random
import time
import sys

def slow_print(text, delay=0.03):
    """Print text with a slight delay for better readability."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_header():
    """Display the game header."""
    header = """
    ╭━━━╮╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╭━━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
    ┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
    ┃╰━╯┣━━┣━━┣╮╭╮┃╰━╯┣━━┣━━┣━━╮╰╯┃┃╰┻━┳━━┳━━┳━━┳━┳━━┳━╮
    ┃╭╮╭┫╭╮┃╭╮┃╰╯┃┃╭━━┫╭╮┃╭╮┃━━┫╱╱┃┃╭━╮┃┃━┫━━┫━━┫╭┫╭╮┃╭╯
    ┃┃┃╰┫╰╯┃╰╯┃┃┃┃┃┃╱╱┃╰╯┃╰╯┣━━┃╱╱┃┃╰━╯┃┃━╋━━┣━━┃┃┃╰╯┃┃╱
    ╰╯╰━┻━━┻━━┻┻┻╯╰╯╱╱╰━━┻━━┻━━╯╱╱╰┻━━━┻━━┻━━┻━━┻╯╰━━┻╯╱
    """
    print(header)

def display_choices():
    """Display the game choices with ASCII art."""
    choices = """
    [1] ROCK     [2] PAPER    [3] SCISSORS
    
    ╭─────────╮  ╭─────────╮  ╭─────────╮
    │  _____  │  │ _____   │  │    _    │
    │ /     \ │  │|     |  │  │   / \   │
    │(   O   )│  │|     |  │  │  /   \  │
    │ \_____/ │  │|_____|  │  │ <     > │
    │         │  │         │  │  \   /  │
    │         │  │         │  │   \_/   │
    ╰─────────╯  ╰─────────╯  ╰─────────╯
    """
    print(choices)

def get_player_choice():
    """Get and validate the player's choice."""
    valid_choices = {"1": "rock", "2": "paper", "3": "scissors", 
                    "rock": "rock", "paper": "paper", "scissors": "scissors",
                    "r": "rock", "p": "paper", "s": "scissors"}
    
    while True:
        choice = input("\nEnter your choice (1-Rock, 2-Paper, 3-Scissors): ").lower()
        if choice in valid_choices:
            return valid_choices[choice]
        print("Invalid choice! Please try again.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    """Determine the winner of the round."""
    if player_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if winning_combinations[player_choice] == computer_choice:
        return "player"
    else:
        return "computer"

def display_choices_animation(player_choice, computer_choice):
    """Display an animation of the choices."""
    print("\nRock... Paper... Scissors... Shoot!")
    time.sleep(0.5)
    
    choice_symbols = {
        "rock": "👊",
        "paper": "✋",
        "scissors": "✌️"
    }
    
    print(f"\nYou chose: {player_choice.upper()} {choice_symbols[player_choice]}")
    time.sleep(0.5)
    print(f"Computer chose: {computer_choice.upper()} {choice_symbols[computer_choice]}")
    time.sleep(0.5)

def display_result(result, player_choice, computer_choice):
    """Display the result of the round with explanation."""
    if result == "tie":
        print("\n🔄 It's a TIE! Both chose the same.")
    elif result == "player":
        if player_choice == "rock" and computer_choice == "scissors":
            print("\n🎉 You WIN! Rock crushes Scissors.")
        elif player_choice == "paper" and computer_choice == "rock":
            print("\n🎉 You WIN! Paper covers Rock.")
        elif player_choice == "scissors" and computer_choice == "paper":
            print("\n🎉 You WIN! Scissors cut Paper.")
    else:  # computer wins
        if computer_choice == "rock" and player_choice == "scissors":
            print("\n❌ You LOSE! Rock crushes Scissors.")
        elif computer_choice == "paper" and player_choice == "rock":
            print("\n❌ You LOSE! Paper covers Rock.")
        elif computer_choice == "scissors" and player_choice == "paper":
            print("\n❌ You LOSE! Scissors cut Paper.")

def play_game():
    """Main game function."""
    display_header()
    slow_print("Welcome to Rock, Paper, Scissors!")
    slow_print("Can you defeat the computer in this classic game?")
    
    player_score = 0
    computer_score = 0
    ties = 0
    round_num = 1
    
    # Ask for number of rounds
    while True:
        try:
            best_of = int(input("\nHow many rounds would you like to play? "))
            if best_of > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    
    while round_num <= best_of:
        print(f"\n===== ROUND {round_num}/{best_of} =====")
        print(f"Score: You {player_score} - {computer_score} Computer (Ties: {ties})")
        
        display_choices()
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        display_choices_animation(player_choice, computer_choice)
        
        result = determine_winner(player_choice, computer_choice)
        display_result(result, player_choice, computer_choice)
        
        # Update scores
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            ties += 1
        
        round_num += 1
        
        if round_num <= best_of:
            input("\nPress Enter to continue to the next round...")
    
    # Display final results
    print("\n" + "=" * 40)
    print("FINAL RESULTS")
    print("=" * 40)
    print(f"You: {player_score} | Computer: {computer_score} | Ties: {ties}")
    
    if player_score > computer_score:
        slow_print("\n🏆 Congratulations! You won the game! 🏆")
    elif computer_score > player_score:
        slow_print("\n😢 The computer won this time. Better luck next time! 😢")
    else:
        slow_print("\n🤝 It's a tie game! Great match! 🤝")
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again in ["y", "yes"]:
        play_game()
    else:
        slow_print("\nThanks for playing! See you next time!")

if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")