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

    def make_empty(self):
        self.tail = None
        self.head = None
        self.length = 0

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

    def pop(self):
        # edge cases: list with 1 element or empty
        if self.length == 1:
            temp = self.head
            self.tail = None
            self.head = None
            self.length = 0
            return temp
        elif self.length == 0:
            return None
        # normal case
        temp = self.head
        pre = self.head
        while temp.next != None:
            temp = temp.next
            if temp.next != None:
                pre = temp
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        #edge case: empty list
        self.new_node = Node(value)
        if self.length == 0:
            self.append(value)
        else:
            # normal case
            self.new_node.next = self.head
            self.head = self.new_node
            self.length += 1

            

          

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()
print("\npop")
my_linked_list.pop()
my_linked_list.pop()
my_linked_list.print_list()

print("\nlength:")
print(my_linked_list.length)

my_linked_list.prepend(8)

print("\nprepend:")
my_linked_list.print_list()
                                                                         
