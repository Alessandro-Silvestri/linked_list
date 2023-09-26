class Stack:
    def __init__(self):
        self.stack_list = []
    
    def print_stack(self):
        for i in self.stack_list:
            print(i)
    
    def push(self, value):
        self.stack_list.append(value)
    
    def pop(self):
        # empty list
        if self.stack_list == []:
            return None
        # normal case
        temp = self.stack_list[-1]
        self.stack_list = self.stack_list[:-1]
        return temp


my_stack = Stack()
my_stack.push(1)
my_stack.print_stack()
print()
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print()
my_stack.print_stack()