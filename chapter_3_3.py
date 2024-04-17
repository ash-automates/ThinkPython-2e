def print_beam():
    print("+ - - - -", end=" ")  # Print a horizontal beam of the grid


def print_post():
    print("|        ", end=" ")  # Print a vertical post of the grid


def print_beams():
    """
    Prints the top and bottom beams of a row in the grid.
    """
    do_twice(print_beam)  # Print two horizontal beams
    print("+")  # Print the closing plus sign of the row


def print_posts():
    """
    Prints the vertical posts of a row in the grid.
    """
    do_twice(print_post)  # Print two vertical posts
    print("|")  # Print the closing vertical post of the row


def print_row():
    """
    Prints a single row of the grid.
    """
    print_beams()  # Print the top and bottom beams of the row
    do_four(print_posts)  # Print four vertical posts of the row


def print_grid():
    """
    Prints a 2x2 grid using rows and columns.
    """
    do_twice(print_row)  # Print two rows of the grid
    print_beams()  # Print the final bottom beams to complete the grid


# Test the print_grid function to see the grid output
print_grid()
