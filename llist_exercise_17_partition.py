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
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def partition_list(self, x):
        # creating 2 empty lists 
        ll_list1 = LinkedList(1)
        ll_list2 = LinkedList(1)
        self.ll_result = LinkedList(1)
        ll_list1.make_empty()
        ll_list2.make_empty()
        self.ll_result.make_empty()

        temp = self.head

        while temp is not None:
            if temp.value < x:
                ll_list1.append(temp.value)
                temp = temp.next
            elif temp.value >= x:
                ll_list2.append(temp.value)
                temp = temp.next

        temp = ll_list1.head
        while temp is not None:
            self.ll_result.append(temp.value)
            temp = temp.next

        temp = ll_list2.head
        while temp is not None:
            self.ll_result.append(temp.value)
            temp = temp.next




ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

ll.partition_list(5)
quit()
print("LL after partition_list:")
ll.print_list() # Output: 3 2 1 5 8 10


"""
    EXPECTED OUTPUT:
    ----------------
    LL before partition_list:
    3
    5
    8
    10
    2
    1
    LL after partition_list:
    3
    2
    1
    5
    8
    10
    
"""