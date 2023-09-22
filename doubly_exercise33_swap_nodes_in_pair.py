class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):
        self.before = self.head
        self.after = self.before.next


        ########## UNTIL HERE: Try with the for loop#################
        while True:
            # iteration
            # create additional pointers
            self.before1 = self.before.prev 
            self.after1 = self.after.next

            # swap pair
            self.after.next = self.before
            self.before.prev = self.after
            self.after.prev = self.before1
            self.before.next = self.after1
            
            if self.after1 is not None:
                self.after1.prev = self.before
            
            # swap self.before and after
            self.before, self.after = self.after, self.before
            
            # put head at the beginning only the first iteration 
            if self.before1 is None:
                self.head = self.before
            
            
            # # break the connection of before1 and after1 pointers (maybe doesn't need)
            # self.before1 = self.after1 = None
            
            # moving forward all the pointers
            if self.after.next is None or self.after.next.next is None:
                break
            else:
                self.before = self.before.next.next
                self.after = self.after.next.next
            





my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.print_list()
print()

my_dll.swap_pairs()
my_dll.print_list()

print(my_dll.after.value)



