from vector import Vector
from matrix import Matrix


m1 = Matrix([[7.0, 8.0, 4.0], [3.0, 2.0, 1.0]], (2, 3))
m2 = Matrix([[0.0, 3.0], [2.0, 4.0], [3.0, 5.0]], (3, 2))
m3 = Matrix([[7.0, 3.0, 4.0], [8.0, 2.0, 1.0]])
m4 = Matrix([[0.0, 2.0, 3.0], [3.0, 4.0, 5.0]])
v1 = Vector([3.0, 4.0, 3.0])
v2 = Matrix((5, 1))
print(m1 * 2)
print(m1 * v1)
print(m1.__rmul__(m2))
print(m3.__radd__(m4))
print(m3 / 3)
