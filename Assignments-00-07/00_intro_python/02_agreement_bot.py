def main():
    # Ask the user for their favorite animal
    favorite_animal = input("What's your favorite animal? ")
    
    # Format the animal name with bold and italic using ANSI escape codes
    # Bold: \033[1m, Italic: \033[3m, Reset: \033[0m
    formatted_animal = f"\033[3m\033[3m{favorite_animal}\033[0m"
    
    # Respond with the message
    print(f"My favorite animal is also {formatted_animal}!")

if __name__ == "__main__":
    main()