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
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0



    def reverse_between(self, start_index, end_index):
        # creating pointers
        slow = None
        fast = self.head
        
    
         # create var cointaining how many steps runner will do
        runner_steps = end_index - start_index
       
        # the pointer fast achieves the first Node of the group to reverse
        # and slow a step back
        for i in range(start_index):
            slow = fast
            fast = fast.next

        ############## loop ########################################

        # create the runner pointer and it goes at the end of the group to reverse
        runner = fast
        for i in range(runner_steps):
            runner = runner.next
        

        # connecting the 2 sides of the normal llist
        fast.next = runner.next



        # last node of reverse group at the beginning

        slow.next = runner
        runner.next = fast
        return self.head.next.next.next.next.value
        # moving the pointers (fast remains still)
        slow = slow.next
        runner = fast
        runner_steps -= 1
        





linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)

print(linked_list.reverse_between(2, 4))

