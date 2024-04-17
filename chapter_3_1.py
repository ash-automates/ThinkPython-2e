# Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter of the string is in column 70
# of the display.


def right_justify(word: str):
    """
    Prints the given word with leading spaces to right-justify it in a 70-column display.

    Args:
        word (str): The word to be right-justified.
    """
    spaces_needed = 70 - len(word)  # Calculate the number of spaces needed
    print(" " * spaces_needed + word)  # Print the word with leading spaces


# Test cases
right_justify("cat")
right_justify("bulldog")
right_justify("extravagant")
