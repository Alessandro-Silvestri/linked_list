class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

# this time the exercise require a function and not a method
def find_kth_from_end(llist, value):
    ''' It uses 2 pointers (slow/fast)
    The fast pointer moves value nodes ahead in the list
    then they move together one step at the time, when fast achievese the end
    (becoming None), return slow
    '''
    slow = llist.head
    fast = llist.head
    # just moving fast pointer ahead (value times)
    for i in range(value):
        '''if fast become None the value is out of range'''
        if fast is None:
            return None
        fast = fast.next
    
    # the 2 pointers move together until fast is None
    while fast is not None:
        slow = slow.next
        fast = fast.next
    
    return slow




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

