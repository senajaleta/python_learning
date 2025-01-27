import random
import string
import math
def calculate_area(shape,**kwargs):
    if shape == "circle":
        return math.pi*kwargs.get('r')**2
    elif shape == "rectangle":
        return kwargs.get('w')*kwargs.get('l')
    else:
        shape =="triangle"
        return 0.5* (kwargs.get('b')*kwargs.get('h'))



print(calculate_area("circle",r=2))
print(calculate_area("rectangle",w=4,l=3))
print(calculate_area("triangle",b=4,h=3))


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
    characters = "abc"
    characters += "123"
    #characters += string.punctuation
    characters  += "@#"
    password =''.join([random.choice(characters)for i in range (length) ])
    print("your random password is: ",password)

random_password()