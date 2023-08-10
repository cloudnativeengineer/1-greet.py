# filename: greet.py

import sys


def format_name(name: str) -> str:
    """
    Check if the name is valid and format it if necessary.

    Args:
        name (str): Name to be formatted.

    Returns:
        str: Formatted name if valid, None otherwise.
    """
    if name.isalpha():
        # Lowercase the name and then capitalize the first letter
        return name.lower().capitalize()
    return None


def main():
    # Check if a name is provided as a command line argument
    if len(sys.argv) > 1:
        name = sys.argv[1]
        formatted_name = format_name(name)

        if formatted_name:
            print(f"Hello, {formatted_name}")
        else:
            print("Invalid name format. Ensure the name is all letters.")
    else:
        print("Hello, World")


if __name__ == '__main__':
    main()
