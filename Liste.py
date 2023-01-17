class ListElement:

    def __init__(self, obj):
        self.obj = obj
        self.nextElem = None

    def setNextElem(self, nextElem):
        self.nextElem = nextElem

    def getNextElem(self):
        return self.nextElem
    
    def getObj(self):
        return self.obj
    
class List:

    startElem = ListElement('test')

    def __init__(self):
        pass

    def addLast(self, o):
        newElem = ListElement(o)
        lastElem = self.getLastElem()
        lastElem.setNextElem(newElem)
    
    def insertAfter(self, prevItem, newItem):
        pointerElem = self.startElem.getNextElem()
        while pointerElem != None and not pointerElem.getObj() == prevItem:
            pointerElem = pointerElem.getNextElem()
        
        newElem = ListElement(newItem)
        nextElem = pointerElem.getNextElem()
        pointerElem.setNextElem(newElem)
        newElem.setNextElem(nextElem)
    
    def delete(self, o):
        le = self.startElem.getNextElem()
        while le.getNextElem() != None and not le.getObj() == o:
            if le.getNextElem().getObj() == o:
                if le.getNextElem().getNextElem() != None:
                    le.setNextElem(le.getNextElem().getNextElem())
                else:
                    le.setNextElem(None)
                    break
            le = le.getNextElem()
        
    def find(self, o):
        le = self.startElem.getNextElem()
        while le != None:
            if le.getObj() == o:
                return True
            le = le.nextElem
        return False
    
    def getFirstElem(self):
        return self.startElem.getNextElem()

    def getLastElem(self):
        le = self.startElem
        while le.getNextElem() != None:
            le = le.getNextElem()
        return le
    
    def writeList(self):
        le = self.startElem.getNextElem()
        s = ""
        while le != None:
            if le.getNextElem() == None:
                s = s + str(le.getObj())
            else:
                s = s + str(le.getObj()) + ', '
            le = le.getNextElem()
        print(s)
    
    def length(self):
        le = self.startElem.getNextElem()
        l = -1
        while le != None:
            l = l + 1
            le = le.getNextElem()
        print(l)
    

if __name__ == "__main__":
    list = List()
    list.addLast(1)
    list.addLast(2)
    list.addLast(3)
    list.addLast(4)
    list.addLast(5)
    #list.insertAfter(2, 1)
    #list.delete(3)
    list.writeList()
    list.length()
    print("erstes Element: " + str(list.getFirstElem().getObj()))
    print("ist '3' enthalten? " + str(list.find(3)))
    print("ist '5' enthalten? " + str(list.find(5)))
    print("letztes Element: " + str(list.getLastElem().getObj()))
    