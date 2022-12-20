# this file demonstrates on how to work with sets in pyhton

class MySet:
    def __init__(self):
        self._set = {}

    def addToSet(self):
        elements  = input("enter the elements: ")
        self._set.add(elements)

    def serchingSetElements(self):
        want = input('enter the element you wish to search: ')
        if want in self._set:
            print ('the element you searched s precent')


    def deleteFromSet(self):
        desition = int(input('Enter \n 1 to delete the whole set \n 2 to delete an item: '))

        if desition == 1 :
            self._set.clear()
        elif desition == 2:
            print(self._set)
            d2 = int(input('Enter the index you wish to remove: '))
            self._set.pop(d2)


if __name__ == "__main__":
    myset = MySet()
    myset.addToSet()
    myset.accesingSetElements()
    myset.removingFromSet()
    myset.deleteFromSet()