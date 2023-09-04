class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.new_node = Node(value) 
        self.head = self.new_node
        self.tail = self.new_node
        self.length = 1

    def print_list(self):
        if self.length == 0:
            return None
        temp = self.head
        print(temp.value)
        while temp.next != None:
            temp = temp.next
            print(temp.value)

    def append(self, value):
        self.new_node = Node(value)
        if  self.length == 0:
            self.head = self.new_node
            self.tail = self.new_node
            self.length = 1
        else:
            self.tail.next = self.new_node
            self.tail = self.new_node
            self.length += 1


################ until here: do with 2 pointers ##########################
    def pop(self):
        temp = self.head
        pre = self.head
        while temp.next != None:
            pass
        pass
######################################################
            

    def make_empty(self):
        self.tail = None
        self.head = None
        self.length = 0
          

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print(my_linked_list.pop().value) 
print(my_linked_list.pop().value) 
print("")
my_linked_list.print_list()

                                                                         
