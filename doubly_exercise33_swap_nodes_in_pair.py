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
        '''using 4 pointers'''
        # edge case: empty list
        if self.length == 0 or self.length == 1:
            return
        before = self.head
        after = before.next
        # calculate the number of iterations
        iter_n = self.length
        if iter_n % 2 != 0:
            iter_n -= 1
        iter_n = int((iter_n / 2))
        #iteration
        for i in range(iter_n):
            # create additional pointers
            before1 = before.prev 
            after1 = after.next
            # swap after/before connections (internal/external)
            after.next = before
            before.prev = after
            before.next = after1
            after.prev = before1
            # considering before1 and after1
            if before1:
                before1.next = after
            if after1:
                after1.prev =before
            # swap before and after
            before, after = after, before
            # put head at the beginning only the first iteration 
            if not before1:
                self.head = before         
            # moving forward all the pointers
            if not after1:
                break
            before = before.next.next
            after = after.next.next


            

my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.append(5)
my_dll.append(6)
my_dll.append(7)
my_dll.append(8)
my_dll.print_list()

my_dll.swap_pairs()

print()
my_dll.print_list()
