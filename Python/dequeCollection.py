from collections import deque

d = deque([1,2,3])
print(d)

# enqueuing at the right end using .append()
d.append(10)
print(d)

# enqueuing at the left emd using .appendleft()
d.appendleft(90)
print(d)

# popping at the right end using pop()
d.pop()
print(d)

# popping at the left end using popleft()
d.popleft()
print(d)

