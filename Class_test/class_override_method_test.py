class X:
    def __init__(self, a = None):
        self.a = a
        if a:
            self.z_train = self.train
            self.train = self.a_train
    def train(self):
        print('normal_train')
    def a_train(self):
        print('a_train')

A = X()
A.train()
B = X(a = 1)
B.train()
B.z_train()

print(B.a_train is B.train)
print(B.a_train == B.train)
print(B.z_train is B.train)
print(B.z_train == B.train)

