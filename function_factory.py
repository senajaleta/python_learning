import math
import random
import string


def calculate_area(shape, *args):
    """Calculates the area of different shapes."""
    if shape.lower() == 'rectangle':
        if len(args) != 2:
            raise ValueError("Rectangle requires 2 arguments: width and height.")
        width, height = args
        return width * height
    elif shape.lower() == 'circle':
        if len(args) != 1:
            raise ValueError("Circle requires 1 argument: radius.")
        radius = args[0]
        return math.pi * (radius ** 2)
    elif shape.lower() == 'triangle':
        if len(args) != 2:
            raise ValueError("Triangle requires 3 arguments: base and height.")
        base, height = args[0], args[1]
        return 0.5 * base * height
    else:
        raise ValueError("Unsupported shape: {}".format(shape))


def is_palindrome(word):
    """Checks if a given word is a palindrome."""
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]

def generate_random_password(length):
    """Generates a random password of the specified length."""
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
#calculate_area(rectangle,2 )
def main():
    # Calculate area examples
    print("Area of rectangle (5 x 10):", calculate_area('rectangle', 5, 10))
    print("Area of circle (radius 7):", calculate_area('circle', 7))
    print("Area of triangle (base 10, height 5):", calculate_area('triangle', 10, 5))

    # Palindrome check examples
    print("Is 'racecar' a palindrome?", is_palindrome('racecar'))
    print("Is 'hello' a palindrome?", is_palindrome('hello'))

    # Generate random password
    print("Random password (length 12):", generate_random_password(12))

main()