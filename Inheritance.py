class Animal:
    def eat(self):
        print("i can eat")
class Dog(Animal):
    def bark(self):
        print("i can bark!")
class Cat(Animal):
    def get_grumpy(self):
        print("i am getting grumpy")
dog1 = Dog()
dog1.bark()
dog1.eat()
cat1 = Cat()
cat1.eat()


