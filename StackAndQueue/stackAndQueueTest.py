from stackIt import Stack, Queue

s = Stack()
q = Queue()

s.push(7)
q.add(4)
s.push(2*3)
s.push(1)
q.add(7)
s.push(q.remove())
q.add(9)
q.add(10)

print(s.pop())
print(q.remove())