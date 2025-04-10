def main():
    # Prompt the user for temperature in Fahrenheit
    fahrenheit_input = input("Enter temperature in Fahrenheit: ")
    
    # Convert the input to a float
    fahrenheit = float(fahrenheit_input)
    
    # Convert Fahrenheit to Celsius using the provided formula
    celsius = (fahrenheit - 32) * 5.0/9.0
    
    # Format the user input with bold and italic using ANSI escape codes
    # Bold: \033[1m, Italic: \033[3m, Reset: \033[0m
    formatted_input = f"\033[1m\033[3m{fahrenheit_input}\033[0m"
    
    # Display the result with the original input formatted
    print(f"\nEnter temperature in Fahrenheit: {formatted_input}")
    print(f"\nTemperature: {fahrenheit}F = {celsius}C")

if __name__ == "__main__":
    main()