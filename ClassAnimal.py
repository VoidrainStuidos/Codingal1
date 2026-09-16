from abc import ABC, abstractmethod
class Animal(ABC):

    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("I can walk and run.")

class Snake(Animal):

    def move(self):
        print("I can crawl.")

class Dog(Animal):

    def move(self):
        print("I can bark.")

class Lion(Animal):

    def move(self):
        print("I can roar.")

ob1 = Human()
ob1.move()
ob2 = Snake()
ob2.move()
ob3 = Dog()
ob3.move()
ob4 = Lion()
ob4.move()