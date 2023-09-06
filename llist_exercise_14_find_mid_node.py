'''
Implement the find_middle_node

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True



    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast.next != None:
            if fast.next.next is None:
                fast = fast.next
                slow = slow.next
                return slow
            slow = slow.next
            fast = fast.next.next
        return slow


my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.append(5)
my_linked_list_1.append(6)
my_linked_list_1.append(7)
my_linked_list_1.append(8)


print(my_linked_list_1.find_middle_node().value)