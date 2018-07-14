# double-ended queue
# 双端队列在需要按照元素增加的顺序来溢出元素时非常有用

from collections import deque
# 双端队列通过可迭代对象（比如集合）创建
q = deque(range(5))
q.append(5)
q.appendleft(6)
print q
q.pop()
print q
q.popleft()
print q
q.rotate(3)
print q
q.rotate(-1)
print q
