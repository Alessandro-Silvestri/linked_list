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

    def is_palindrome(self):
        '''using 2 pointers: start and end and checking the values'''
        start = self.head
        end = self.tail
        # calculate the number of iterations
        iter_n = self.length // 2
        for i in range(iter_n):
            if not start.value == end.value:
                return False
            #moving the pointers
            start = start.next
            end = end.prev
        return True
        
        




my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(2)
my_dll_1.append(1)
my_dll_1.append(4)
print(my_dll_1.is_palindrome())