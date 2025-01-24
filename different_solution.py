import random
import string
import math
def calculate_area():
    def circle_area(r):
        cir_Area = math.pi * r**2
        print("The circle Area is: ", cir_Area)

    def rectangle_area(w,l):
        rec_Area = l*w
        print("The Area of rectangle: ", rec_Area)

    def triangle_area(b,h):
        tri_area = 1/2*b*h
        print("The Area of triangle: ",tri_area)

    circle_area(2)
    rectangle_area(3,4)
    triangle_area(4,2)


calculate_area()


def is_palindrome():
    word = input("Enter any word to check for palindrome: ")
    reverse = word[::-1]
    if word == reverse:
        print("It's palindrome!")
    else:
        print("It's not palindrome!")


is_palindrome()

def random_password():
    length = int(input("Enter your password length: "))
    characters = string.ascii_letters
    characters += string.digits
    characters += string.punctuation
    password =''.join([random.choice(characters)for i in range (length) ])
    print("your random password is: ",password)

random_password()