# this file demonstrates on how to work with sets in pyhton

class MySet:
    def __init__(self):
        self.set = {}

    def addToSet(self):
        elements  = input("enter the elements: ")
        self.set.add(elements)

    def accesingSetElements(self):
        pass

    def removingFromSet(self):
        pass

    def deleteFromSet(self):
        pass


if __name__ == "__main__":
    myset = MySet()
    myset.addToSet()
    myset.accesingSetElements()
    myset.removingFromSet()
    myset.deleteFromSet()