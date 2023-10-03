class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        # if empty tree
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        # normal case
        while temp:
            # in value already in the tree
            if value == temp.value:
                return False
            # pointer goes to the right
            if value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            # pointer goes to the left
            elif value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
    
    def contains(self, value):
        temp = self.root
        while temp:
            if value == temp.value:
                return True
            elif value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
        return False




my_b_tree = BinarySearchTree()
print(my_b_tree.insert(2))
print(my_b_tree.insert(1))
print(my_b_tree.insert(3))
print(my_b_tree.insert(2))

print()
print(my_b_tree.contains(4))