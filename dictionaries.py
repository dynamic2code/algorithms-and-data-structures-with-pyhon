#ths file shows how to work with python dictionaries

class Dictionary:
    def __init__(self):
        # creating an empty dctionary
        self.dictionary = {}
    
    def addToDictionary(self):
        # user inputs the values
        key = input("Enter your key: ")
        values = input("Enter your value/ values: ")
        self.dictionary.update( key = values.split())
        print(self.dictionary)
    
    def accecingDictionaryElement(self):
        #with the key
        key = input("Enter the key you want to access: ")
        print(self.dictionary[key])

    def removeFromDictionary(self):
        method = int(input("Enter the method you wish to use\n 1 to use index \n 2 to remove by item name"))

        if method == 1:
            print(self.dictionary)
            itemToDelete = int(input('Enter the idex you wish to delete: '))
            self.dictionary.pop(itemToDelete)

        elif method == 2:
            
            print(self.dictionary)
            itemToDelete_string = input('Enter the item you wish to delete: ')
            self.dictionary.pop(itemToDelete_string)

    def deleteDictionary(self):
        comand = input("Enter del to delete the full dictionary: ")
        if comand =='del':
            self.dictionary.clear()

if __name__ == "__main__":
    myDictionary = Dictionary()
    myDictionary.addToDictionary()
    myDictionary.accecingDictionaryElement()
    myDictionary.removeFromDictionary()
    myDictionary.deleteDictionary()
