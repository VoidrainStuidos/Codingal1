class myClass:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling price =", self.__maxprice)

    def setMaxPrice(self, price):
        self.__maxprice = price

ob1 = myClass()
ob1.sell()

ob1.__maxprice = 1000
ob1.sell()

ob1.setMaxPrice(1000)
ob1.sell()