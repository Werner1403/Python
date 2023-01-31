import copy

class ListElement:

    def __init__(self, obj):
        self.obj = obj
        self.nextElem = None
        self.before_elem = None

    def setNextElem(self, nextElem):
        self.nextElem = nextElem

    def getNextElem(self):
        return self.nextElem        
    
    def setBeforeElem(self, before_elem):
        self.before_elem = before_elem
    
    def getBeforeElem(self):
        return self.before_elem
    
    def getObj(self):
        return self.obj
    
    def setObj(self, obj):
        self.obj = obj
    
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
            
    def count(self, o):
        le = self.startElem.getNextElem()
        c = 0
        while le != None:
            if le.getObj() == o:
                c += 1
            le = le.getNextElem()
        return c
            
        
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
            s = s + str(le.getObj()) + " "
            le = le.getNextElem()
        print(s)
    
    def length(self):
        le = self.startElem.getNextElem()
        l = -1
        while le != None:
            l = l + 1
            le = le.getNextElem()
        return l
    
    def clear(self):
        le = self.startElem.getNextElem()
        while le != None:
            le.setObj("")
            le = le.getNextElem()
        self.startElem = ListElement('start')
        return le

    def extend(self, list):
        le = self.startElem.getNextElem()
        while le.getNextElem() != None:
            pass


    #TODO letztes element von standpunkt aus    
    # def sort(self, arr):
    #     le = self.startElem.getNextElem()
    #     l = -1
    #     while le != None:
    #         l = l + 1
    #         le = le.getNextElem()
    #     for i in range(1, l):
    #         key = le.getObj()
    #         le = le.getNextElem()

    #         j = i-1
    #         while j >=0 and key < arr[j] :
    #             arr[j+1] = arr[j]
    #             j -= 1
    #         arr[j+1] = key

if __name__ == "__main__":
    list = List()
    list.addLast(1)
    list.addLast(2)
    list.addLast(3)
    list.addLast(4)
    list.addLast(5)
    list.addLast(3)
    #list.insertAfter(2, 1)
    #list.delete(3)
    list.writeList()
    list.clear()
    list.writeList()
    list.addLast(1)
    list.addLast(99)
    list.writeList()
    