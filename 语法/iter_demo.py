

class A:
    def __init__(self):
        self.n = 10

    def __iter__(self):
        for i in range(self.n):
            yield i


a = A()
for s in a:
    print(s)


