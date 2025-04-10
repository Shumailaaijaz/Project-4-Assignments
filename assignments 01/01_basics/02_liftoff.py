def countdown():
    """Prints a countdown from 10 to 1 followed by 'Liftoff!'."""
    countdown_sequence = [str(10 - i) for i in range(10)]
    print(' '.join(countdown_sequence) + ' Liftoff!')

def main():
    """Orchestrates the program execution."""
    countdown()

if __name__ == '__main__':
    main()