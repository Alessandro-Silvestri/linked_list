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
        ll_list1.make_empty()
        ll_list2.make_empty()

        # for debugging
        lista1 = []
        lista2 = []

        temp = self.head

        while temp is not None:
            if temp.value < x:
                ll_list1.append(temp)
                lista1.append(temp.value) # debugging
                temp = temp.next
            elif temp.value >= x:
                ll_list2.append(temp)
                lista2.append(temp.value) # debugging
                temp = temp.next

        # for debugging: checking if the 2 lists are right
        print(lista1)
        print()
        print(lista2)
        
        





ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)



ll.partition_list(4)
quit()



print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

ll.partition_list(5)

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
