from collections import deque
"""
listのlikeで両端の処理に強い,
random_accessについてはO(n)なのでlist参照
"""
d=deque([1,2,3,4])
print(d.rotate(1)) #same as  d.appendleft(d.pop())
d.pop()
d.popleft()
d.appendleft(4)
d.append(1)


