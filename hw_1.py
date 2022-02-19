class Matrix:

    def __init__(self, n, m):
        self.x = n
        self.y = m
        self.matr = []

    def make_matrix(self):
        print()
        i = 0
        for i in range(self.x*self.y):
            self.matr.append(input())

    def make_readable(self):
        a = str()
        num = 0
        for i in self.matr:
            a = a + " " + i + " "
            num += 1
            if num == self.y:
                a += "\n"
                num = 0
        return a


    def __str__(self):
        return self.make_readable()

new = Matrix(3,3)
new.make_matrix()
print(new)
