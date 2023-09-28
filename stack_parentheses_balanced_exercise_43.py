class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

# create a function
def is_balanced_parentheses2(text:str):
    '''solution but the nested parentheses'''
    stack = Stack()  
    # putting text in stack list
    for i in text:
        stack.push(i)
    length = stack.size()
    # check if list is empty
    if stack.stack_list == []:
        return True
    # check if length is even
    if length % 2 != 0:
        return False
    # check ")("
    if stack.stack_list[0] == ")" or stack.peek() == "(":
        return False
    # check opposite values
    length = int(length / 2)
    for i in range(length):
        # if the opposite value are opposite parentheses
        if (text[i] == "(" and stack.peek() == ")") or (text[i] == ")" and stack.peek() == "("):
            stack.pop()
        else:
            return False
    return True




def is_balanced_parentheses(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()



def test_is_balanced_parentheses():
    try:
        assert is_balanced_parentheses('())') == True # check opposite values (first/last)
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert is_balanced_parentheses('()') == True 
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        assert is_balanced_parentheses('(()())') == True 
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert is_balanced_parentheses('(()') == False # check odd numbers
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert is_balanced_parentheses('())') == False
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert is_balanced_parentheses(')(') == False # check first or last value
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert is_balanced_parentheses('') == True # check empty
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert is_balanced_parentheses('()()()()') == True # check opposite values (first/last)
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert is_balanced_parentheses('(())(())') == True
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert is_balanced_parentheses('(()()())') == True
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')

    try:
        assert is_balanced_parentheses('((())') == False # check odd
        print('Test case 11 passed')
    except AssertionError:
        print('Test case 11 failed')

test_is_balanced_parentheses()
