def main():
    # Define ANSI escape codes for formatting
    bold_italic = "\033[1m\033[3m"
    reset = "\033[0m"
    
    # Prompt for the three sides
    side1_input = input("What is the length of side 1? ")
    side1 = float(side1_input)
    
    side2_input = input("What is the length of side 2? ")
    side2 = float(side2_input)
    
    side3_input = input("What is the length of side 3? ")
    side3 = float(side3_input)
    
    # Calculate the perimeter
    perimeter = side1 + side2 + side3
    
    # Display the inputs with formatting and the result
    print("\nUser inputs (bold and italic):")
    print(f"What is the length of side 1? {bold_italic}{side1_input}{reset}")
    print(f"What is the length of side 2? {bold_italic}{side2_input}{reset}")
    print(f"What is the length of side 3? {bold_italic}{side3_input}{reset}")
    
    # Print the perimeter
    print(f"\nThe perimeter of the triangle is {perimeter}")

if __name__ == "__main__":
    main()