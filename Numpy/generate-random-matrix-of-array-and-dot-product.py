import numpy as np

# this will create integer as array-elements
# A = np.random.randint(10, size=(2,3))
# B = np.random.randint(10, size=(3,2))

# If instead of array-elements I just wanted
# any random value then
A = np.random.random([2, 3])
B = np.random.random([3,2])


# print(A)
# print(B)

# Dot product
print(np.dot(A, B))

# transpose
print(np.dot(A, B).T)
