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
        head_temp = self.head

        for i in range(2):
            slow = head_temp
            fast = slow.next

            while fast is not None: 
                if fast.value != head_temp.value:
                    slow = fast
                    fast = fast.next
                else:
                    # check if 1 repeated number is at the end
                    if fast.next is None:
                        slow.next = None
                        self.length -= 1
                        break
                    # check if there are duplicates in raw
                    if fast.next.value == head_temp.value:
                        while fast.value == head_temp.value and fast.next.value == head_temp.value:
                            fast = fast.next
                            self.length -= 1
                            if fast.next is None:
                                slow.next = None
                                break           
                    # normal case pointers move
                    fast = fast.next
                    slow.next = fast
                    slow = fast
                    self.length -= 1                
                    # when the iteration achieves the end of the list
                    if not fast:
                        break
                    fast = fast.next
            head_temp = head_temp.next



 


        

my_linked_list = LinkedList(1)
my_linked_list.append(3)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.append(3)



my_linked_list.print_all()

print()
my_linked_list.remove_duplicates()
print("duplicate 1st value removed")


my_linked_list.print_all()




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