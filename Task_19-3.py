class Person:
    def __init__(self, *args):
        self.args = args
    def __str__(self):
        return ''.join(self.args)[::-1]

p = Person('Иванов', 'Михаил', 'Федорович')
print(p)