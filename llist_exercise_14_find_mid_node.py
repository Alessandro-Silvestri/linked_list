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


########## UNTIL HERE bug: it has to be only 1 loop ########
    def find_middle_node(self):
        temp = self.head
        index = 0
        while temp.next != None:
            temp = temp.next
            index += 1
        # if index % 2 == 0:
        #     index += 1
        index //= 2




        temp = self.head
        index2 = 0
        for i in range(index):
            temp = temp.next
            index2 += 1
        return temp
############################################################




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)


# print(my_linked_list.find_middle_node().value)
print(my_linked_list.find_middle_node().value)

