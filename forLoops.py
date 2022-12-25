#looping over data structures

class ForLoops:
    def __init__(self):
        self.list1 =[[2,1,3,56],"man",['duck','pie','chiken']]

    def loopignList(self):
    #loopign through a list
        for i in self.list1:
            print(i)

if __name__ == "__main__":
    objForLoop = ForLoops()
    objForLoop.loopignList()