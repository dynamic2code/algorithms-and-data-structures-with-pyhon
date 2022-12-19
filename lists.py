#the file is to show how to work on lists

#creating a list 

class MyList:
    def __init__(self):
        self.names = []
    
    def showItem(self):
        item  = int(input('enter the item index you wish to show: '))
        try:
           print( self.names[item])
        except:
            print("value enterd s not of valid type")


    def addToList(self):
        #the lst will take inputs from user 
        userInPut = input("enter your inputs separated by a whitespace: ")
        self.names.extend(userInPut.split())
        print("The new list is: \n {}".format(self.names))
    
    def removeFromList(self):
        removeWithIndex = int(input("Enter the position you want removed: "))
        removeWithItemName = input("Enter the name of the item you wish removed: ")

        self.names.pop(removeWithIndex)

    def showAll(self):
        pass

    
if __name__ == "__main__":
    myList = MyList()
    myList.addToList()
    myList.removeFromList()