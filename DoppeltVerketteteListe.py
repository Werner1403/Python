class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoppeltVerketteteListe:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def insert(self, index, data):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(data)
        elif index == self.length:
            self.append(data)
        else:
            new_node = Node(data)
            leader = self._traverse_to_index(index - 1)
            follower = leader.next
            leader.next = new_node
            new_node.prev = leader
            new_node.next = follower
            follower.prev = new_node
            self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

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
            leader = self._traverse_to_index(index - 1)
            node_to_remove = leader.next
            follower = node_to_remove.next
            leader.next = follower
            follower.prev = leader
        self.length -= 1

    def delete(self, value):
            current_node = self.head

            while current_node:
                if current_node.data == value:
                    if current_node == self.head:
                        self.head = current_node.next
                        if self.head:
                            self.head.prev = None
                        else:
                            self.tail = None
                    elif current_node == self.tail:
                        self.tail = current_node.prev
                        self.tail.next = None
                    else:
                        current_node.prev.next = current_node.next
                        current_node.next.prev = current_node.prev
                    self.length -= 1
                    return
                current_node = current_node.next
            raise ValueError("Value not found in list")
        
    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        return self._traverse_to_index(index).data

    def _traverse_to_index(self, index):
        current_node = self.head
        current_index = 0

        while current_index != index:
            current_node = current_node.next
            current_index += 1

        return current_node

    def __len__(self):
        return self.length

    def __str__(self):
        values = ""
        current_node = self.head

        while current_node:
            values = values + '[' + (str(current_node.data)) + '],' if current_node.next != None else values + '[' + (str(current_node.data)) + ']'
            current_node = current_node.next

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