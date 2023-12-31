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
            return False
        elif index > self.length - 1:
            return False
        else:
            temp = self.get(index)
            temp.value = value
            return True

    def insert(self, index, value):
        self.new_node = Node(value)
        # edge cases: out of range, insert in first or last position
        if index < 0 or index >= self.length + 1:
            return None
        elif index == 0:
            self.prepend(value)
            return True
        elif index == self.length:
            self.append(value)
            return True
        # normal cases
        else:
            pre = self.get(index - 1)
            temp = pre.next
            pre.next = self.new_node
            self.new_node.next = temp
            self.length += 1
            return True
        
    def remove(self, index):
        # edge cases: out of range
        if index < 0 or index > self.length - 1:
            return None
        # the list contains only 1 node
        elif self.length == 1 and index == 0:
            return self.pop()
        # removing the first node
        elif index == 0:
            return self.pop_first()
        else:
            # normal case
            pre = self.get(index - 1)
            temp = pre.next
            after = temp.next
            temp.next = None
            pre.next = after
            self.length -= 1
            return temp
    
    def reverse(self):
        self.tail, self.head = self.head, self.tail
        temp = self.tail
        pre = None
        after = temp.next
        for i in range(self.length - 1):
            temp.next = pre        
            pre = temp
            temp = after
            after = temp.next
        self.head.next = pre
    

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)

my_linked_list.print_list()

my_linked_list.reverse()

print()
my_linked_list.print_list()
