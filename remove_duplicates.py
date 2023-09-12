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
#########################################################
        while fast is not None:  
            if fast.value != temp.value:
                slow = fast
                fast = fast.next
            else:
                print(f"fast value: {fast.value}")
                # while fast.next == 1:
                #     print(f"repetitive number: {fast.value}")
                #     fast = fast.next
                fast = fast.next
                slow.next = fast
                slow = fast
            

        





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.append(3)
my_linked_list.print_all()

print()
my_linked_list.remove_duplicates()

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
