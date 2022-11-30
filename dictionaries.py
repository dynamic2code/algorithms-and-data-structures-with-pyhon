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
        pass

    def deleteDictionary(self):
        pass


if __name__ == "__main__":
    myDictionary = Dictionary()
