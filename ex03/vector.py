class Vector:
    def __init__(self, values):
        assert isinstance(values, int) or isinstance(values, range) or isinstance(values, tuple) or\
            all(isinstance(x, float) for x in values),\
            "vector should be an int or a list of floats"
        if type(values) is int:
            self.values = [float(i) for i in range(0, values)]
            self.size = values
        elif type(values) is range:
            self.values = [float(i) for i in values]
            self.size = len(values)
        elif type(values) is tuple:
            assert len(values) is 2 and values[0] < values[1] and all(isinstance(x, int) for x in values),\
                "tuple should be composed of 2 int"
            self.values = [float(i) for i in range(values[0], values[1])]
            self.size = abs(values[1] - values[0])
        else:
            self.values = list(values)
            self.size = len(values)

    def transform(self, param):
        assert isinstance(param, int) or isinstance(param, Vector)
        if isinstance(param, int):
            new_list = [float(param) for i in range(0, self.size)]
            return Vector(new_list)
        else:
            assert param.size == self.size
            return param

    def __str__(self):
        formatted_string = "(Vector {0})"
        return formatted_string.format(self.values)

    def __repr__(self):
        return {'values': self.values, 'size': self.size}

    def __add__(self, other):
        other = self.transform(other)
        return self.sum(other)

    def __radd__(self, other):
        other = self.transform(other)
        return self.sum(other)

    def sum(self, right):
        new_list = [float(self.values[i] + right.values[i]) for i in range(0, self.size)]
        return Vector(new_list)

    def __sub__(self, other):
        left = self.transform(other)
        return self.sub(left, self)

    def __rsub__(self, other):
        right = self.transform(other)
        return self.sub(self, right)

    def sub(self, left, right):
        new_list = [float(left.values[i] - right.values[i]) for i in range(0, left.size)]
        return Vector(new_list)

    def __truediv__(self, other):
        assert isinstance(other, int) and other != 0, "must be an in different of 0"
        right = self.transform(other)
        return self.div(self, right)

    def __rtruediv__(self, other):
        assert isinstance(self, int) and other != 0, "must be an in different of 0"
        left = self.transform(other)
        return self.div(left, self)

    def div(self, left, right):
        new_list = [float(left.values[i] / right.values[i]) for i in range(0, left.size)]
        return Vector(new_list)

    def __mul__(self, other):
        if type(self) is Vector and type(other) is Vector:
            return self.vector_mul(other)
        else:
            return self.mul(self.transform(other))

    def __rmul__(self, other):
        return self.mul(self.transform(other))

    def mul(self, other):
        new_list = [float(self.values[i] * other.values[i]) for i in range(0, self.size)]
        return Vector(new_list)

    def vector_mul(self, other):
        nb = 0
        for i in range(0, self.size):
            nb += float(self.values[i] * other.values[i])
        return nb

