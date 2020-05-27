from vector import Vector


class Matrix:
    def __init__(self, *argv):
        assert 2 >= len(argv) >= 1, "too much arguments"
        if len(argv) is 2:
            assert isinstance(argv[0], list) and all(isinstance(x, list)
                                                     for x in argv[0]) and \
                   all(all(isinstance(x, float) for x in argv[0][y])
                       for y in range(0, len(argv[0]))) \
                   and isinstance(argv[1], tuple) and \
                   argv[1][0] is len(argv[0]) and \
                   argv[1][1] is len(argv[0][0]), \
                   "argv[0] must be a list of float and argv[1] a tuple"
            self.data = argv[0]
            self.shape = argv[1]
        else:
            matrix = argv[0]
            if type(matrix) is list:
                line_size = len(matrix[0])
                i = 0
                for line in matrix:
                    if len(line) != line_size:
                        raise ValueError('not the same length for each list')
                    assert all(isinstance(x, float) for x in line),\
                        "Matrix should be composed of floats only"
                    i += 1
                self.data = []
                for line in matrix:
                    self.data.append(line)
                self.shape = (i, line_size)
            elif type(matrix) is tuple:
                self.data = [[float(0) for i in range(0, matrix[0])]
                             for i in range(0, matrix[1])]
                self.shape = (matrix[0], matrix[1])

    def __str__(self):
        formatted_string = "(Matrix ["
        for i in range(0, len(self.data)):
            formatted_string += "{0[" + str(i) + "]}, "
        formatted_string = formatted_string[:len(formatted_string) - 2] + "])"
        return formatted_string.format(self.data)

    def __repr__(self):
        return {'data': self.data, 'shape': self.shape}

    def __mul__(self, other):
        assert isinstance(other, Vector)\
               or isinstance(other, Matrix) or isinstance(other, int)
        return self.mul(other)

    def __rmul__(self, other):
        assert isinstance(self, Vector) or isinstance(self, Matrix) or\
               isinstance(self, int)
        return Matrix(self.mul(other))

    def mul(self, arg):
        if type(arg) is int:
            new_matrix = []
            for i in range(0, self.shape[0]):
                new_matrix.append([float(self.data[i][x] * arg)
                                   for x in range(0, self.shape[1])])
            return Matrix(new_matrix, self.shape)
        elif type(arg) is Vector:
            assert self.shape[1] is arg.size,\
                "matrix.shape[0] must equal to vector.size"
            new_vector = []
            for i in range(0, self.shape[0]):
                new_vector.append(0.0)
                new_vector[i] += sum(float(self.data[i][x] * arg.values[x])
                                     for x in range(0, arg.size))
            return Vector(new_vector)
        elif type(arg) is Matrix:
            assert self.shape[0] is arg.shape[1],\
                "self.shape[0] must equal to arg.shape[1]"
            new_size = self.shape[1]
            new_matrix = []
            for i in range(0, new_size):
                new_matrix.append([])
                for j in range(0, new_size):
                    new_matrix[i].append([])
                    new_matrix[i][j] =\
                        (sum(float(self.data[k][i] * arg.data[j][k])
                             for k in range(0, self.shape[0])))
            return new_matrix

    def __add__(self, other):
        assert isinstance(self, Matrix) and isinstance(other, Matrix) and\
               self.shape[0] is other.shape[0] and \
               self.shape[1] is other.shape[1]
        return self.add(other)

    def __radd__(self, other):
        assert isinstance(self, Matrix) and isinstance(other, Matrix) and \
               self.shape[0] is other.shape[0] and \
               self.shape[1] is other.shape[1]
        return self.add(other)

    def add(self, other):
        new_matrix = []
        for i in range(0, self.shape[0]):
            new_matrix.append([float(self.data[i][j] + other.data[i][j])
                               for j in range(0, self.shape[1])])
        return new_matrix

    def __sub__(self, other):
        assert isinstance(self, Matrix) and isinstance(other, Matrix) and\
               self.shape[0] is other.shape[0] and \
               self.shape[1] is other.shape[1]
        return self.sub(other)

    def __rsub__(self, other):
        assert isinstance(self, Matrix) and isinstance(other, Matrix) and \
               self.shape[0] is other.shape[0] and \
               self.shape[1] is other.shape[1]
        return self.sub(other)

    def sub(self, other):
        new_matrix = []
        for i in range(0, self.shape[0]):
            new_matrix.append([float(self.data[i][j] - other.data[i][j])
                               for j in range(0, self.shape[1])])
        return new_matrix

    def __truediv__(self, other):
        assert isinstance(self, Matrix) and isinstance(other, int)
        return self.div(other)

    def __rtruediv__(self, other):
        assert isinstance(self, Matrix) and isinstance(other, int)
        return self.div(other)

    def div(self, other):
        new_matrix = []
        for i in range(0, self.shape[0]):
            new_matrix.append([float(self.data[i][j] / other)
                               for j in range(0, self.shape[1])])
        return new_matrix
