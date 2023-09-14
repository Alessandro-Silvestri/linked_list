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
        '''using 3 pointers'''
        head_temp = self.head
        while head_temp:
            slow = head_temp
            fast = slow.next

            while fast: 
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

    def remove_duplicates_set(self):
        '''using set{} and 2 pointers that become 3 when the iteration meets a duplicate value'''
        #setting the 2 pointers and the set
        slow = self.head
        fast = slow.next
        set_values = {slow.value}
        # iteration
        while fast is not None:
            # if the node is not a duplicate
            if fast.value not in set_values:
                set_values.add(fast.value)
                slow = fast
                fast = fast.next
            else:
            # if the node is a duplicate
                self.length -= 1
                fast_fast = fast.next
                fast.next = None
                slow.next = fast_fast
                fast = fast_fast
        

                




        

my_linked_list = LinkedList(1)
my_linked_list.append(1)



my_linked_list.print_all()

print()
my_linked_list.remove_duplicates_set()

print("removed")
my_linked_list.print_all()

print(f"length: {my_linked_list.length}")
