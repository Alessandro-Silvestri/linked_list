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
    

    def pop_first(self):
        #edge cases: empty list or with 1 node
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        # normal case
        pre = self.head
        temp = self.head.next
        self.head = temp
        pre.next = None
        self.length -= 1
        return pre
    
    def get(self, index):
        # edge cases: out of range
        if self.length == 1:
            return self.head
        elif index < 0 or index > self.length - 1:
            return None
        else:
            # normale case
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp
    
    def set_value(self, index, value):
        if index < 0:
            return None
        elif index > self.length - 1:
            return None
        else:
            temp = self.get(index)
            temp.value = value
    

    ######## until here: no works, didn't pass the test #############################
    def insert(self, index, value):
        self.new_node = Node(value)
        # edge cases: out of range, insert in first or last position
        if index < 0 or index >= self.length + 1:
            return None
        elif index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        # normal cases
        else:
            pre = self.get(index - 1)
            temp = pre.next
            pre.next = self.new_node
            self.new_node.next = temp
            self.length += 1
    ##############################################


            

          

my_linked_list = LinkedList(1)
my_linked_list.print_list

print("pop")
my_linked_list.pop()


print("\nlist")
my_linked_list.pop()
