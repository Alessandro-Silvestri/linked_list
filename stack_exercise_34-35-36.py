'''
Python: data structures and algorithms - course
Stack representation with methods: push, pop and print stack,
all the methods handle edge cases.

Solved by Alessandro Silvestri - 2023 <alessandro.silvestri.work@gmail.com>
GitHub: https://github.com/Alessandro-Silvestri
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        # if empty list
        if self.height == 0:
            self.top = new_node
        else:
        # normal case
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    
    def pop(self):
        # normal case
        temp = self.top
        # if stack has 1 node
        if self.height == 1:
            self.top = None
        # if stack is empty
        elif self.height == 0:
            return None
        # normal case
        else:
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp
