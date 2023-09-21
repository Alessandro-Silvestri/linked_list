class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def reverse(self):
        if self.length == 0:
            return
        self.head, self.tail = self.tail, self.head
        before = self.tail
        after = before.next

        for i in range(self.length - 1):
            # changing arrows
            after2 = after.next
            before.prev = after
            after.next = before

            # moving forward the pointers
            before = after
            after = after2
        self.tail.next = None





my_list = DoublyLinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.print_list()
print()

my_list.reverse()

my_list.print_list()

