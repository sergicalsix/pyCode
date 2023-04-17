class A():
    __slots__ = ('a', )
class B(A):
    pass
x = B()
y = A()
print(x.__slots__, y.__slots__)
x.hoge = 1
y.hoge = 1