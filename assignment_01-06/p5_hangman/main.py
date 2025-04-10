import random
import time
import os
import sys
from collections import defaultdict

# ANSI color codes for colorful output
class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

# Word categories with words of varying difficulty
WORD_CATEGORIES = {
    "Animals": ["dog", "cat", "elephant", "giraffe", "penguin", "tiger", "zebra", "kangaroo", "rhinoceros", "hippopotamus"],
    "Countries": ["usa", "canada", "brazil", "france", "japan", "australia", "egypt", "india", "switzerland", "madagascar"],
    "Fruits": ["apple", "banana", "orange", "strawberry", "watermelon", "pineapple", "kiwi", "mango", "blueberry", "pomegranate"],
    "Sports": ["soccer", "basketball", "tennis", "swimming", "volleyball", "cricket", "golf", "hockey", "rugby", "skateboarding"],
    "Movies": ["avatar", "titanic", "inception", "jaws", "frozen", "gladiator", "interstellar", "matrix", "casablanca", "psycho"]
}

# Hangman stages with ASCII art
HANGMAN_STAGES = [
    # Stage 0: Empty
    f"""
    {Colors.CYAN}
    +---+
    |   |
        |
        |
        |
        |
    =========
    {Colors.RESET}""",
    
    # Stage 1: Head
    f"""
    {Colors.CYAN}
    +---+
    |   |
    {Colors.YELLOW}O   {Colors.CYAN}|
        |
        |
        |
    =========
    {Colors.RESET}""",
    
    # Stage 2: Head and torso
    f"""
    {Colors.CYAN}
    +---+
    |   |
    {Colors.YELLOW}O   {Colors.CYAN}|
    {Colors.YELLOW}|   {Colors.CYAN}|
        |
        |
    =========
    {Colors.RESET}""",
    
    # Stage 3: Head, torso, and one arm
    f"""
    {Colors.CYAN}
    +---+
    |   |
    {Colors.YELLOW}O   {Colors.CYAN}|
    {Colors.YELLOW}/|  {Colors.CYAN}|
        |
        |
    =========
    {Colors.RESET}""",
    
    # Stage 4: Head, torso, and both arms
    f"""
    {Colors.CYAN}
    +---+
    |   |
    {Colors.YELLOW}O   {Colors.CYAN}|
    {Colors.YELLOW}/|\\ {Colors.CYAN}|
        |
        |
    =========
    {Colors.RESET}""",
    
    # Stage 5: Head, torso, both arms, and one leg
    f"""
    {Colors.CYAN}
    +---+
    |   |
    {Colors.YELLOW}O   {Colors.CYAN}|
    {Colors.YELLOW}/|\\ {Colors.CYAN}|
    {Colors.YELLOW}/   {Colors.CYAN}|
        |
    =========
    {Colors.RESET}""",
    
    # Stage 6: Full hangman (game over)
    f"""
    {Colors.CYAN}
    +---+
    |   |
    {Colors.RED}O   {Colors.CYAN}|
    {Colors.RED}/|\\ {Colors.CYAN}|
    {Colors.RED}/ \\ {Colors.CYAN}|
        |
    =========
    {Colors.RESET}"""
]

# Animated hangman stages for dramatic effect when losing
ANIMATED_GAME_OVER = [
    f"""
    {Colors.CYAN}
    +---+
    |   |
    {Colors.RED}O   {Colors.CYAN}|
    {Colors.RED}/|\\ {Colors.CYAN}|
    {Colors.RED}/ \\ {Colors.CYAN}|
        |
    =========
    {Colors.RESET}""",
    
    f"""
    {Colors.CYAN}
    +---+
    |   |
    {Colors.RED}O   {Colors.CYAN}|
    {Colors.RED}/|\\/{Colors.CYAN}|
    {Colors.RED}/ \\ {Colors.CYAN}|
        |
    =========
    {Colors.RESET}""",
    
    f"""
    {Colors.CYAN}
    +---+
    |   |
    {Colors.RED}O   {Colors.CYAN}|
    {Colors.RED}\\|\\ {Colors.CYAN}|
    {Colors.RED}/ \\ {Colors.CYAN}|
        |
    =========
    {Colors.RESET}""",
    
    f"""
    {Colors.CYAN}
    +---+
    |   |
    {Colors.RED}O   {Colors.CYAN}|
    {Colors.RED}/|\\ {Colors.CYAN}|
    {Colors.RED}\\ / {Colors.CYAN}|
        |
    =========
    {Colors.RESET}"""
]

# Victory animation frames
VICTORY_ANIMATION = [
    f"""
    {Colors.GREEN}
       \\O/
        |
       / \\
    {Colors.RESET}""",
    
    f"""
    {Colors.GREEN}
        O
       /|\\
       / \\
    {Colors.RESET}""",
    
    f"""
    {Colors.GREEN}
       \\O/
        |
       / \\
    {Colors.RESET}""",
    
    f"""
    {Colors.GREEN}
        O
       \\|/
       / \\
    {Colors.RESET}"""
]

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03):
    """Print text with a slight delay between characters."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_title():
    """Display the game title with ASCII art."""
    title = f"""
    {Colors.YELLOW}{Colors.BOLD}
     _   _                                         
    | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
    |  _  | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                       |___/                       
    {Colors.RESET}
    """
    print(title)

def display_menu():
    """Display the main menu."""
    print(f"\n{Colors.CYAN}{Colors.BOLD}===== HANGMAN GAME ====={Colors.RESET}")
    print(f"{Colors.WHITE}1. Start New Game")
    print("2. Choose Difficulty")
    print("3. Choose Word Category")
    print("4. How to Play")
    print(f"5. Quit{Colors.RESET}")
    
    choice = input(f"\n{Colors.YELLOW}Enter your choice (1-5): {Colors.RESET}")
    return choice

def display_difficulty_menu():
    """Display the difficulty selection menu."""
    print(f"\n{Colors.CYAN}{Colors.BOLD}===== DIFFICULTY LEVEL ====={Colors.RESET}")
    print(f"{Colors.GREEN}1. Easy (8 attempts, shorter words)")
    print(f"{Colors.YELLOW}2. Medium (6 attempts, medium words)")
    print(f"{Colors.RED}3. Hard (4 attempts, longer words){Colors.RESET}")
    
    while True:
        choice = input(f"\n{Colors.YELLOW}Select difficulty (1-3): {Colors.RESET}")
        if choice in ['1', '2', '3']:
            return int(choice)
        print(f"{Colors.RED}Invalid choice. Please try again.{Colors.RESET}")

def display_category_menu():
    """Display the category selection menu."""
    print(f"\n{Colors.CYAN}{Colors.BOLD}===== WORD CATEGORIES ====={Colors.RESET}")
    for i, category in enumerate(WORD_CATEGORIES.keys(), 1):
        print(f"{Colors.WHITE}{i}. {category}{Colors.RESET}")
    
    while True:
        choice = input(f"\n{Colors.YELLOW}Select category (1-{len(WORD_CATEGORIES)}): {Colors.RESET}")
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(WORD_CATEGORIES):
                return list(WORD_CATEGORIES.keys())[choice_num - 1]
        except ValueError:
            pass
        print(f"{Colors.RED}Invalid choice. Please try again.{Colors.RESET}")

def display_how_to_play():
    """Display game instructions."""
    clear_screen()
    print(f"\n{Colors.CYAN}{Colors.BOLD}===== HOW TO PLAY ====={Colors.RESET}")
    print(f"{Colors.WHITE}1. The computer will select a random word.")
    print("2. You need to guess the word one letter at a time.")
    print("3. Each incorrect guess adds a part to the hangman.")
    print("4. If the hangman is completed before you guess the word, you lose.")
    print("5. If you guess the word before the hangman is completed, you win!")
    print(f"\n{Colors.YELLOW}Tips:{Colors.WHITE}")
    print("- Start with common vowels (a, e, i, o, u)")
    print("- Look for patterns in the revealed letters")
    print(f"- You can use a hint if you're stuck (costs an attempt){Colors.RESET}")
    
    input(f"\n{Colors.GREEN}Press Enter to return to the main menu...{Colors.RESET}")

def select_word(category, difficulty):
    """Select a random word based on category and difficulty."""
    words = WORD_CATEGORIES[category]
    
    # Filter words by length based on difficulty
    if difficulty == 1:  # Easy
        filtered_words = [w for w in words if len(w) <= 5]
    elif difficulty == 2:  # Medium
        filtered_words = [w for w in words if 4 <= len(w) <= 8]
    else:  # Hard
        filtered_words = [w for w in words if len(w) >= 6]
    
    # If no words match the criteria, use all words from the category
    if not filtered_words:
        filtered_words = words
    
    return random.choice(filtered_words)

def get_max_attempts(difficulty):
    """Get the maximum number of attempts based on difficulty."""
    if difficulty == 1:  # Easy
        return 8
    elif difficulty == 2:  # Medium
        return 6
    else:  # Hard
        return 4

def display_word_state(word, guessed_letters):
    """Display the current state of the word with guessed letters."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += f"{Colors.GREEN}{letter}{Colors.RESET} "
        else:
            display += f"{Colors.WHITE}_{Colors.RESET} "
    return display

def display_game_state(word, guessed_letters, incorrect_attempts, max_attempts, category):
    """Display the current game state."""
    # Display hangman
    stage = min(incorrect_attempts, len(HANGMAN_STAGES) - 1)
    print(HANGMAN_STAGES[stage])
    
    # Display category and word state
    print(f"{Colors.YELLOW}Category: {Colors.WHITE}{category}{Colors.RESET}")
    print(f"\n{Colors.YELLOW}Word: {Colors.RESET}{display_word_state(word, guessed_letters)}")
    
    # Display guessed letters
    print(f"\n{Colors.YELLOW}Guessed letters: {Colors.RESET}", end="")
    for letter in sorted(guessed_letters):
        if letter in word:
            print(f"{Colors.GREEN}{letter}{Colors.RESET}", end=" ")
        else:
            print(f"{Colors.RED}{letter}{Colors.RESET}", end=" ")
    
    # Display attempts remaining
    attempts_left = max_attempts - incorrect_attempts
    print(f"\n\n{Colors.YELLOW}Attempts remaining: ", end="")
    if attempts_left <= 2:
        print(f"{Colors.RED}{attempts_left}{Colors.RESET}")
    elif attempts_left <= 4:
        print(f"{Colors.YELLOW}{attempts_left}{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}{attempts_left}{Colors.RESET}")

def get_hint(word, guessed_letters):
    """Provide a hint by revealing an unguessed letter."""
    unguessed = [letter for letter in word if letter not in guessed_letters]
    if unguessed:
        return random.choice(unguessed)
    return None

def animate_game_over():
    """Display an animation when the player loses."""
    for _ in range(3):  # Repeat the animation 3 times
        for frame in ANIMATED_GAME_OVER:
            clear_screen()
            print(frame)
            print(f"\n{Colors.RED}{Colors.BOLD}GAME OVER!{Colors.RESET}")
            time.sleep(0.3)

def animate_victory():
    """Display an animation when the player wins."""
    for _ in range(3):  # Repeat the animation 3 times
        for frame in VICTORY_ANIMATION:
            clear_screen()
            print(frame)
            print(f"\n{Colors.GREEN}{Colors.BOLD}VICTORY!{Colors.RESET}")
            time.sleep(0.3)

def play_game(category="Animals", difficulty=2):
    """Main game function."""
    word = select_word(category, difficulty).lower()
    max_attempts = get_max_attempts(difficulty)
    guessed_letters = set()
    incorrect_attempts = 0
    hint_used = False
    
    while incorrect_attempts < max_attempts:
        clear_screen()
        display_title()
        display_game_state(word, guessed_letters, incorrect_attempts, max_attempts, category)
        
        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            animate_victory()
            clear_screen()
            print(HANGMAN_STAGES[incorrect_attempts])
            print(f"\n{Colors.GREEN}{Colors.BOLD}CONGRATULATIONS! You guessed the word: {Colors.YELLOW}{word.upper()}{Colors.RESET}")
            print(f"{Colors.GREEN}You had {max_attempts - incorrect_attempts} attempts remaining!{Colors.RESET}")
            return True
        
        # Get player's guess
        guess = input(f"\n{Colors.YELLOW}Enter a letter or '?' for a hint: {Colors.RESET}").lower()
        
        # Handle hint request
        if guess == '?' and not hint_used:
            hint_letter = get_hint(word, guessed_letters)
            if hint_letter:
                print(f"\n{Colors.PURPLE}Hint: The word contains the letter '{hint_letter}'{Colors.RESET}")
                guessed_letters.add(hint_letter)
                hint_used = True
                incorrect_attempts += 1  # Using a hint costs an attempt
                time.sleep(2)
                continue
        
        # Validate input
        if guess == '?' and hint_used:
            print(f"\n{Colors.RED}You've already used your hint!{Colors.RESET}")
            time.sleep(1)
            continue
        
        if len(guess) != 1 or not guess.isalpha():
            print(f"\n{Colors.RED}Please enter a single letter.{Colors.RESET}")
            time.sleep(1)
            continue
        
        if guess in guessed_letters:
            print(f"\n{Colors.RED}You've already guessed that letter!{Colors.RESET}")
            time.sleep(1)
            continue
        
        # Add the guess to guessed letters
        guessed_letters.add(guess)
        
        # Check if the guess is correct
        if guess in word:
            # Sound effect for correct guess
            print(f"\n{Colors.GREEN}Correct! '{guess}' is in the word!{Colors.RESET}")
            print(f"{Colors.YELLOW}*DING*{Colors.RESET}")
        else:
            # Sound effect for incorrect guess
            print(f"\n{Colors.RED}Wrong! '{guess}' is not in the word!{Colors.RESET}")
            print(f"{Colors.RED}*BUZZ*{Colors.RESET}")
            incorrect_attempts += 1
        
        time.sleep(1)
    
    # Game over - player lost
    animate_game_over()
    clear_screen()
    print(HANGMAN_STAGES[6])
    print(f"\n{Colors.RED}{Colors.BOLD}GAME OVER! You ran out of attempts.{Colors.RESET}")
    print(f"{Colors.YELLOW}The word was: {Colors.WHITE}{word.upper()}{Colors.RESET}")
    return False

def main():
    """Main function to run the game."""
    difficulty = 2  # Default: Medium
    category = "Animals"  # Default category
    stats = {"wins": 0, "losses": 0}
    
    while True:
        clear_screen()
        display_title()
        
        if stats["wins"] > 0 or stats["losses"] > 0:
            print(f"\n{Colors.PURPLE}Stats: {Colors.GREEN}Wins: {stats['wins']} {Colors.RED}Losses: {stats['losses']}{Colors.RESET}")
        
        choice = display_menu()
        
        if choice == '1':
            # Start new game
            result = play_game(category, difficulty)
            if result:
                stats["wins"] += 1
            else:
                stats["losses"] += 1
            
            play_again = input(f"\n{Colors.YELLOW}Would you like to play again? (y/n): {Colors.RESET}").lower()
            if play_again != 'y':
                break
        
        elif choice == '2':
            # Choose difficulty
            difficulty = display_difficulty_menu()
        
        elif choice == '3':
            # Choose category
            category = display_category_menu()
        
        elif choice == '4':
            # How to play
            display_how_to_play()
        
        elif choice == '5':
            # Quit
            print(f"\n{Colors.GREEN}Thanks for playing Hangman! Goodbye!{Colors.RESET}")
            break
        
        else:
            print(f"\n{Colors.RED}Invalid choice. Please try again.{Colors.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Game interrupted. Thanks for playing!{Colors.RESET}")