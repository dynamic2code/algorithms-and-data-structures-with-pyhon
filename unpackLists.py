#to unpack a list containing other list with 
#no knowledge of the lists length
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(len(list_of_lists))

class UnpackLists:

    def __init__(self, listToUnpack):
        self.listToUnpack = listToUnpack

    def unpack(self):
        noOfValuables = len(self.listToUnpack)