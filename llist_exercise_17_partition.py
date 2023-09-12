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

        temp = self.head

        while temp is not None:
            if temp.value < x:
                ll_list1.append(temp.value)
                temp = temp.next
            elif temp.value >= x:
                ll_list2.append(temp.value)
                temp = temp.next


        temp = ll_list1.head
        ll_temp = self.head
        while temp is not None:
            ll_temp.value = temp.value
            temp = temp.next
            ll_temp = ll_temp.next
            
        temp = ll_list2.head
        ll_temp = ll_temp
        while temp is not None:
            ll_temp.value = temp.value
            temp = temp.next
            ll_temp = ll_temp.next

        # if self.ll_result is not None:
        #     self.ll_result.print_list()


ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

print()
ll.partition_list(10)

print()
ll.print_list()
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
