class Matrix:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
    def __add__(self):
        matr = [[0 0 0,
                 0 0 0,
                 0 0 0]]
        for i in range(len(self.list1)):
            for j in range (len(self.list2[1])):
                matr[i][j] = self.list1[i][j] + self.list2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

def __str__(self):
    return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

my_matrix = Matrix([[7, 12, 10],
                        [8, 15, 27],
                        [32, 80, 9]],
                       [[11, 5, 8],
                        [1, 9, 96],
                        [82, 7, 91]])

    print(my_matrix.__add__())
