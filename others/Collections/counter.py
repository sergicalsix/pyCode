from collections import Counter
a = ['a', 'b', 'c', 'd', 'a', 'a', 'b']
c = Counter(a)
d = c.most_common() #出現回数でsort
print(c)
print(c.items())


