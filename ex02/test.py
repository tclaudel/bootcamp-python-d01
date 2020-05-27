from vector import Vector

v1 = Vector([1.0, 1.0, 1.0, 1.0])
v2 = Vector(4)
range1 = range(10, 14)
v3 = Vector(range1)
v4 = Vector((10, 12))
print(v1)
print(v3)
v5 = v1 - v3
v6 = v3 - v1
print(v5)
print(v6)
print(v2 * 3)
print(v2 * v1)
