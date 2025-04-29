# Richard Lay-Flurrie
# Text-based game for IY499 Introduction to Programming Assignment 2

import time

def print_text_slowly(text, delay=0.02):
    """Prints text slowly to the console."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Print a newline at the end

def main():


    print_text_slowly("Test print text slowly function")

if __name__ == "__main__":
    main()