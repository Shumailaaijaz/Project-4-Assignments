def main():
    # Ask the user for a starting number
    user_input = input("Enter a number: ")
    
    # Convert the input to a number
    curr_value = float(user_input)
    
    # Create a list to store all values (including the initial one)
    values = [curr_value]
    
    # Double the value until it reaches or exceeds 100
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the current value
        values.append(curr_value)    # Add to our list of values
    
    # Print all the doubled values
    print(" ".join(str(int(value)) if value.is_integer() else str(value) for value in values))

if __name__ == "__main__":
    main()