'''
Python:
Data Structures and Algorithms

I built a nodes linked list class and it is possible to execute operations like:
      print all the nodes
      add nodes (last position)
      add nodes (first position)
      pop last node
      pop first node
      return a node given an index value
      changing value of a node
      insert a node in a give position
      remove a node
      reverse the list
All the methods handel edge cases

Solved by Alessandro Silvestri - 2023 <alessandro.silvestri.work@gmail.com>
'''

class Node():
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList():
  def __init__(self, value):
    self.new_node = Node(value)
    self.head = self.new_node
    self.tail = self.new_node
    self.length = 1

  def print_list(self):
    self.temp = self.head
    while self.temp is not None:
      print(self.temp.value)
      self.temp = self.temp.next

  def append(self, value):
    self.new_node = Node(value)
    # edge case: if the l list is empty
    if self.head is None:
      self.head = self.new_node
      self.tail = self.new_node
    # normal case
    else:
      self.tail.next = self.new_node
      self.tail = self.new_node
    self.length += 1
    # optional now (but useful later)
    return True

  def pop(self):
    self.temp = self.head
    # edge case: empty list
    if self.head is None:
      return None
    # normal case
    else:
      temp = self.head
      pre = self.head
    while temp.next is not None:
      temp = temp.next
      if temp.next is not None:
        pre = pre.next
    pre.next = None
    self.tail = pre
    self.length -= 1
    # edge case: empty list after removing
    # all the items
    if self.length == 0:
      self.head = None
      self.tail = None
    return temp

  def prepend(self, value):
    self.new_node = Node(value)
    # edge case: empty list
    if self.length == 0:
      self.head == self.new_node
      self.tail == self.new_node
    # normal case
    self.new_node.next = self.head
    self.head = self.new_node
    self.length += 1
    return True

  def pop_first(self):
    # edge case: empty list
    if self.length == 0:
      return None
    # normal case
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    # edge case: empty list after removing all the items
    if self.length == 0:
      self.tail = None
    return temp

  def get(self, index):
    # edge case: index out of range (pos. or neg.)
    if index > self.length - 1 or index < 0:
      return None
    # normale case
    temp = self.head
    for i in range(index):
      temp = temp.next
    return temp

  def set_value(self, index, value):
    temp = self.get(index)
    if temp == None:
      return False
    temp.value = value

  def insert(self, index, value):
    # edge cases: insert in the firts position
    if index == 0:
      self.prepend(value)
    # edge cases: insert in the firts position
    elif index == self.length:
      self.append(value)
    # edge cases: index out of range
    elif index > self.length -1 or index < 0:
      return False
    # normal case
    else:
      self.new_node = Node(value)
      temp = self.get(index - 1)
      self.new_node.next = temp.next
      temp.next = self.new_node
      self.length += 1
      return True

  def remove(self, index):
    # edge cases: index out of range
    if index < 0 or index > self.length - 1:
      return None
    # edge cases: remove the firts or last item
    elif index == 0:
      return self.pop_first()
    elif index == self.length - 1:
      return self.pop()
    # normal case
    else:
      prev = self.get(index - 1)
      temp = self.get(index)
      prev.next = temp.next
      temp.next = None
      self.length -= 1
      return temp

  def reverse(self):
    # reverse head with tail
    self.head, self.tail = self.tail, self.head
    # creating 3 variable I'll use for iterating the list
    temp = self.tail
    before = None
    # loop for reversing the list step by step
    for i in range(self.length):
      after = temp.next
      temp.next = before
      # moving ahead before and temp
      before = temp
      temp = after
    
