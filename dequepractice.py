from collections import deque

a = deque([2,3,4,5])
print(a)

a.append(9)

print("a.append(9) -> ",a)

a.appendleft(0)

print("a.appendleft(0) -> ", a)

a.pop()

print("a.pop -> ", a)

a.popleft()

print("a.popleft -> ", a)