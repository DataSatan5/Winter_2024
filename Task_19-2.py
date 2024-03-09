class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        #self.a, self.b = self.b, self.a + self.b
        tmp = self.a + self.b
        self.a = self.b
        self.b = tmp
        return self.a

x = Fibonacci()
for _ in range(15):
    print(next(x), end=' ')