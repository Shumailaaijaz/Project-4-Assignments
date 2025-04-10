def main():
    # Define ANSI escape codes for formatting
    bold_italic = "\033[1m\033[3m"
    reset = "\033[0m"
    
    # Ask the user for a number
    number_input = input(" \033[1;3m Type a number to see its square: \033[0m ")
    
    # Convert the input to a float
    number = float(number_input)
    
    # Calculate the square
    square = number * number
    
    # Print the result with the input formatted in bold and italic
    print(f"\nType a number to see its square: {bold_italic}{number_input}{reset}")
    print(f"\n{number} squared is {square}")

if __name__ == "__main__":
    main()