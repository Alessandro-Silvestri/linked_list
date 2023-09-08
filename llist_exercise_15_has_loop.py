class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def has_loop(self):
        '''using 2 pointers: slow and fast
        slow steps one and fast steps 2, if they meet it's a loop.
        Edge cases: empty list, only 1 node, only 2 nodes
        '''
        slow = self.head
        fast = self.head
        
        '''
        in the following loop I used 'and', I don't have to use the 'or' otherwise
        the second part of the line will not be read
        '''
        while fast is not None and fast.next is not None:
            print(f"slow: {slow.value} - next: {fast.value}")
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    
        # def has_loop(self):
        #     '''using 2 pointers: slow and fast
        #     slow steps one and fast steps 2, if they meet it's a loop.
        #     Edge cases: empty list, only 1 node, only 2 nodes
        #     '''
        #     # edge cases: empty list, only 1 node, only 2 nodes
        #     if self.head is None:
        #         return False
        #     elif self.head.next is None or self.head.next.next is None:
        #         return False
        #     # normal case
        #     slow = self.head
        #     fast = self.head
        #     while True:
        #         slow = slow.next
        #         fast = fast.next.next
        #         if slow is fast:
        #             return True
        #         elif fast.next is None or fast.next.next is None:
        #             return False



    

    
  
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head


print(my_linked_list_1.has_loop()) # Returns True



my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() ) # Returns False


"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""
