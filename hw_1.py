class Matrix:

    def __init__(self, n: int, m: int) -> None:
        self.x = n
        self.y = m
        self.mat = []

    def matrix_insert(self) -> None:
        for i in range(self.x):
            self.mat.append([])
        print("Insert matrix elements :")
        for i in range(len(self.mat)):
            for j in range(self.y):
                print(f"({i};{j}):")
                self.mat[i].append(input())

    def make_readable(self) -> str:
        print("Your Matrix :")
        st = str()
        for i in range(len(self.mat)):
            st += "\n"
            for j in self.mat[i]:
                st = st + "\t" + j
        return st

    def __str__(self) -> str:
        return self.make_readable()


new = Matrix(3, 3)


new.matrix_insert()
print(new)
