
from collections import deque

f0 = deque()
d0 = deque()

f = deque(['a','b','c'])
d = deque([1,2,3])

f.append('d')
d.append(4)
d.appendleft(0)

print(f[0])
print(d[0])
print(d[len(d)-1])

print(f.popleft())
print(d.pop())
print(d.popleft())

print(len(f))
print(len(d))

print(f.count('b'))
print(d.count(3))
