class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
        
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

    def remove_duplicates(self):
        temp = self.head
        slow = self.head
        fast = self.head
        fast = fast.next
        
        while fast is not None:  
            if fast.value != temp.value:
                slow = fast
                fast = fast.next
                # print(f"temp.value: {temp.value}, slow.value: {slow.value}, fast.value: {fast.value}")
            else:
                # check if 1 repeated number is at the end
                if fast.next is None:
                    slow.next = None
                    break
                # check if there are duplicates in raw
                if fast.next.value == temp.value:
                    while fast.value == temp.value and fast.next.value == temp.value:
                        fast = fast.next
                        if fast.next is None:
                            slow.next = None
                            break
                
                # pointers moove
                fast = fast.next
                slow.next = fast
                slow = fast
                
                # when the iteration achieves the end of the list
                if not fast:
                    break
                fast = fast.next

        

my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(2)
my_linked_list.append(2)



print("list: before removing the duplicates")
my_linked_list.print_all()


print()
my_linked_list.remove_duplicates()



print("\n\nremoved duplicates")
my_linked_list.print_all()
quit()


my_linked_list.print_all()
print()
print(my_linked_list.length)




"""
    EXPECTED OUTPUT:
    ----------------
    Head:  1
    Length:  4
    Linked List:
    1
    2
    3
    4
    
"""
