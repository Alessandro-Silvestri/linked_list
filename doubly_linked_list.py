'''
Python:
Data Structures and Algorithms
Doubly Linked list

I built a nodes linked list class and it is possible to execute operations like:
      print all the nodes
      add nodes (last position)
      add nodes (first position)
      pop last node
      pop first node
      ..... other nodes will be added
All the methods handel edge cases

Solved by Alessandro Silvestri - 2023 <alessandro.silvestri.work@gmail.com>
GitHub: https://github.com/Alessandro-Silvestri
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = self.prev = None

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
        # edge case: empty list
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            # normal case
            temp = self.tail
            temp.next = new_node
            new_node.prev = temp
            self.tail = self.tail.next
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            # if the list is empty
            self.head = self.tail = new_node       
        else:
            # normal case
            new_node.next = self.head 
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def pop(self):
        # edge case: empty list
        if self.length == 0:
            return None
        # edge case: list with just 1 node
        elif self.length == 1:
            temp = self.head
            self.head = self.tail = None
            self.length -= 1
            return temp
        # normal case    
        temp = self.tail.prev
        after = self.tail
        after.prev = None
        temp.next = None
        self.tail = temp
        self.length -= 1
        return after
    
    def pop_first(self):
        # edge case: empty list
        if self.length == 0:
            return None
        # edge case: list with just 1 node
        elif self.length == 1:
            return self.pop()
        # normal case
        temp = self.head.next
        before = self.head
        before.next = None
        temp.prev = None
        self.head = temp
        self.length -= 1
        return before
    
    def get(self, index):
        # edge case: index out of range and empty list
        if index < 0 or index > self.length - 1 or self.head is None:
            return None
        # creting mid point var        
        mid_point = self.length / 2
        if index < mid_point:
            temp = self.head
            # starting from head
            for i in range(index):
                print(f"temp.value {temp}")
                temp = temp.next
            # starting from tail
        else:
            temp = self.tail
            for i in range(self.length - 1 - index):
                print(f"temp.value {temp}")
                temp = temp.prev
        return temp
            
        




my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.print_list()

print()
print(my_doubly_linked_list.pop().value)
print(my_doubly_linked_list.pop().value)

print(my_doubly_linked_list.get(6))
# print("\nnode: ", my_doubly_linked_list.get(8))
