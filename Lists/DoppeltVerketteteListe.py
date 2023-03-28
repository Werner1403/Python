class ListElement:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoppeltVerketteteListe:
    def __init__(self): # O(1)
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data): # O(1)
        new_ListElement = ListElement(data)
        if self.length == 0:
            self.head = new_ListElement
            self.tail = new_ListElement
        else:
            self.tail.next = new_ListElement
            self.tail = new_ListElement
        self.length += 1

    def prepend(self, data): # O(1)
        new_ListElement = ListElement(data)
        if self.length == 0:
            self.head = new_ListElement
            self.tail = new_ListElement
        else:
            new_ListElement.next = self.head
            self.head.prev = new_ListElement
            self.head = new_ListElement
        self.length += 1

    def insert(self, index, data): # O(n)
        if index < 0 or index > self.length:
            print("Index out of range")
            return
        if index == 0:
            self.prepend(data)
        elif index == self.length:
            self.append(data)
        else:
            new_ListElement = ListElement(data)
            leader = self.go_to_index(index - 1)
            follower = leader.next
            leader.next = new_ListElement
            new_ListElement.prev = leader
            new_ListElement.next = follower
            follower.prev = new_ListElement
            self.length += 1

    def remove(self, index): # O(n)
        if index < 0 or index >= self.length:
            print("Index out of range")
            return
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            leader = self.go_to_index(index - 1)
            ListElement_to_remove = leader.next
            follower = ListElement_to_remove.next
            leader.next = follower
            follower.prev = leader
        self.length -= 1

    def delete(self, value): # O(n)
            current_ListElement = self.head
            while current_ListElement:
                if current_ListElement.data == value:
                    if current_ListElement == self.head:
                        self.head = current_ListElement.next
                        if self.head:
                            self.head.prev = None
                        else:
                            self.tail = None
                    elif current_ListElement == self.tail:
                        self.tail = current_ListElement.prev
                        self.tail.next = None
                    else:
                        current_ListElement.prev.next = current_ListElement.next
                        current_ListElement.next.prev = current_ListElement.prev
                    self.length -= 1
                    return
                current_ListElement = current_ListElement.next
            print("Value not found in list")
        
    def getByIndex(self, index): # O(n)
        if index < 0 or index >= self.length:
            print("Index out of range")
            return
        return self.go_to_index(index).data

    def go_to_index(self, index): # O(n)
        current_ListElement = self.head
        current_index = 0
        while current_index != index:
            current_ListElement = current_ListElement.next
            current_index += 1
        return current_ListElement
    
    def clear(self): # O(1)
        self.head = None
        self.tail = None
        self.length = 0

#---------------------------------------------------------------------
    def reverse(self): # O(n)
        current_element = self.head
        self.head, self.tail = self.tail, self.head
        while current_element:
            current_element.prev, current_element.next = current_element.next, current_element.prev
            current_element = current_element.prev 
#---------------------------------------------------------------------

    def sort(self): # O(n^2)
        # Bubble-Sort
        for step in range(1, self.length):
            key = self.go_to_index(step).data
            j = step - 1       
            while j >= 0 and key < self.go_to_index(j).data:
                self.go_to_index(j + 1).data = self.go_to_index(j).data
                j = j - 1
            self.go_to_index(j + 1).data = key
    
    def pop(self): # O(1)
        if self.length == 0:
            print("Empty list!")
            return
        return self.tail.data

    def __len__(self): # O(1)
        return self.length

    def __str__(self): # O(n)
        values = ""
        current_ListElement = self.head
        if self.length == 0:
            return 'No Elements in List'
        while current_ListElement:
            values = values + '[' + (str(current_ListElement.data)) + '],' if current_ListElement.next != None else values + '[' + (str(current_ListElement.data)) + ']'
            current_ListElement = current_ListElement.next
        return values

if __name__ == '__main__':
    list = DoppeltVerketteteListe()
    list.append(1)
    list.append(2)
    list.append(4)
    print(list)
    list.insert(2,3)
    print(list)
    list.delete(4)
    print(list)
    list.prepend(0)
    print(list)
    list.insert(1,0.5)
    print(list)
    list1 = DoppeltVerketteteListe()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.reverse()
    print(list1)
    print(list)
    list.clear()
    print(list)
    list.append(1)
    print(list)
    list.append(2)
    print(list)
    print(list.pop())
    list2 = DoppeltVerketteteListe()
    list2.append(5)
    list2.append(3)
    list2.append(1)
    list2.append(6)
    list2.append(4)
    list2.append(2)
    print(list2)
    list2.sort()
    print(list2)