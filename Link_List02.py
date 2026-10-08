class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def consecutive_sum(self):
        temp = self.head

        while temp and temp.next:
            print(temp.data + temp.next.data)
            temp = temp.next


list = LinkedList()

list.append(1)
list.append(2)
list.append(3)
list.append(4)

list.consecutive_sum()
