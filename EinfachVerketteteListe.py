class ListElement:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data): # O(n)
        new_element = ListElement(data)
        if not self.head:
            self.head = new_element
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element
        self.length += 1

    def prepend(self, data): # O(1)
        new_element = ListElement(data)
        new_element.next = self.head
        self.head = new_element
        self.length += 1

    def insert(self, data, position): # O(n)
        new_element = ListElement(data)
        if position == 0:
            self.prepend(data)
        else:
            element = self.go_to_index(position-1)
            new_element.next = element.next
            element.next = new_element

    def remove(self, index): # O(n)
        if index < 0 or index > self.length:
            print("List Index out of range!")
            return
        element = self.go_to_index(index).data
        self.delete(element)

    def delete(self, data): # O(n)
        if not self.head:
            print("List is empty.")
            return
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.length -= 1
                return
            current = current.next
        print("Element not found in the list.")

    def getByIndex(self, index): # O(n)
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        return self.go_to_index(index).data
    
    def go_to_index(self, index): # O(n)
        current_element = self.head
        current_index = 0
        while current_index != index:
            current_element = current_element.next
            current_index += 1
        return current_element
    
    def clear(self): # O(1)
        self.head = None
        self.length = 0

#--------------------------------------------------
    def reverse(self):  # O(n)
        previous_element = None
        current_element = self.head
        while current_element is not None:
            next_element = current_element.next
            current_element.next = previous_element
            previous_element = current_element
            current_element = next_element
        self.head = previous_element
#--------------------------------------------------

    def sort(self): # O(n^2)
        # bubble-sort
        for step in range(1, self.length):
            key = self.go_to_index(step).data
            j = step - 1       
            while j >= 0 and key < self.go_to_index(j).data:
                self.go_to_index(j + 1).data = self.go_to_index(j).data
                j = j - 1
            self.go_to_index(j + 1).data = key

    def pop(self): # O(n)
        current = self.head
        while current.next:
            current = current.next
        return current.data

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
    
def main():
    list = LinkedList()
    list.append(3)
    list.append(4)
    list.append(1)
    list.append(2)
    list.prepend(5)

    list.sort()

    print(list)

    list.reverse()

    print(list)

if __name__ == "__main__":
    main()
