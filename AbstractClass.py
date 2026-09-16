from abc import ABC, abstractmethod
class AbstractClass(ABC):

    def print(self, x):
        print("The value of x =", x)

    @abstractmethod
    def task(self):
        print("We are inside Abstract Method!")

class NormalClass(AbstractClass):

    def task(self):
        print("We are inside the Normal Method!")

ob1 = NormalClass()
ob1.task()
ob1.print(5)