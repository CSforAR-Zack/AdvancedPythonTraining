
class Stack:
    ''' LIFO data structure. '''

    def __init__(self):
      self.stack = []

    def pop(self):
      if self.is_empty():
        return None
      else:
        return self.stack.pop()

    def push(self,num):
      return self.stack.append(num)

    def peek(self):
      if self.is_empty():
        return None
      else:
        return self.stack[-1]

    def size(self):
      return len(self.stack)

    def is_empty(self):
      return self.size() == 0

    def __str__(self):
      return str(self.stack)


class Queue:
    ''' FIFO data structure.'''

    def __init__(self):
      self.queue = []

    def add(self,num):
      self.queue.insert(0,num)

    def remove(self):
      if self.is_empty():
        return None
      else:
        return self.queue.pop()

    def peek(self):
      if self.is_empty():
        return None
      else:
        return self.queue[self.size() - 1]

    def size(self):
      return len(self.queue)

    def is_empty(self):
      return self.size() == 0

    def __str__(self):
      return str(self.queue)

