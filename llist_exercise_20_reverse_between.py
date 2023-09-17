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
        '''changed the set up: check the note'''
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
        # create the runner pointer and it goes at the end of the group to reverse
        runner = fast
        for i in range(runner_steps):
            runner = runner.next
        # create pointer (first value of the llist after the reverse group)
        cont = runner.next
        ############### LOOP ########################################################
        for i in range(end_index - start_index):
            # moving the last node of the reverse group at the beginning of the same group
            slow.next = runner
            runner.next = fast
            runner = fast
            runner_steps -= 1
            # moving runner at the end of the node of the revers group
            for i in range(runner_steps):
                runner = runner.next
            slow = slow.next
        fast.next = cont


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)


linked_list.reverse_between(4, 7)
linked_list.print_list()


