class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next 
            
    def print_all(self):
        if self.length == 0:
            print("Head: None")
        else:
            print("Head: ", self.head.value)
        print("Length: ", self.length)
        print("\nLinked List:")
        if self.length == 0:
            print("empty")
        else:
            self.print_list()   

    def binary_to_decimal(self):
        '''my version '''
        temp = self.head
        n = 1
        decimal = 0
        for i in range(self.length):
            n = n*2
        n = n / 2
        while temp:
            decimal += (temp.value * n)
            n = n / 2
            temp = temp.next       
        return int(decimal)

    def binary_to_decimal2(self):
        '''course version: no lenght needed'''
        num = 0
        current = self.head
        while current:
            num = num * 2 + current.value
            current = current.next
        return num




linked_list = LinkedList(1)
linked_list.append(0)
linked_list.append(1)
print(linked_list.binary_to_decimal2())