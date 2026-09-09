class myClass:

    __privateVar = 30

    def __privMeth(self):
        print("I'm a private function!")

    def hello(self):
        print("Private variable value =", myClass.__privateVar)

ob1 = myClass()
ob1.hello()
ob1.__privMeth()