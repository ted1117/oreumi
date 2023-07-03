class item:
    def __init__(self, item, stock) -> None:
        self.__item = item
        self.__stock = stock

    def getItem(self):
        return self.__item
    def getStock(self):
        return self.__stock
    def setItem(self, item):
        self.__item = item
    def setStock(self, stock):
        self.__stock = stock

class inventory:
    def __init__(self, item, price, stock) -> None:
        self.__item = item
        self.__price = price
        self.__stock = stock
    
    def getItem(self):
        return self.__item
    
    def getStock(self):
        return self.__stock
    
    def getPrice(self):
        return self.__price
    
    def setItem(self, item):
        self.__item = item

    def setStock(self, stock):
        self.__stock = stock

    def setPrice(self, price):
        self.__price = price

    def add(self, quantity):
        self.__stock += quantity

    def sub(self, quantity):
        self.__stock -= quantity

    def getAmount(self):
        return self.__stock * self.__price

coke = inventory("coke", 1500, 10)
print(coke.getItem())
coke.add(10)
print(coke.getStock())
print(coke.getAmount())