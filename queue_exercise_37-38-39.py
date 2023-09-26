class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = self.last = new_node
        self.length = 1
    
    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self, value):
        new_node = Node(value)
        # edge case: empty queue
        if self.length == 0:
            self.first = self.last = new_node
        # normal case
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    
    def dequeue(self):
        # edge case: empty queue
        if self.length == 0:
            return None
        temp = self.first
        # edge case: with only 1 node
        if self.length == 1:
            self.first = self.last = None
        # normal case
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp



my_queue = Queue(5)
my_queue.enqueue(4)
my_queue.print_queue()

print()
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())

my_queue.enqueue(5)
print()
my_queue.print_queue()

print()
print(my_queue.length)
