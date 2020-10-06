import numpy as np

# For example, to create an array filled with random values between 0 and 1, use random function.
# This is particularly useful for problems where you need a random state to get started.
# But here the elements will be decimals

A = np.random.rand(2,3)
print(A)

""" Output of above
[[0.62857547 0.14598864 0.93991874]
 [0.65560569 0.29442998 0.3354452 ]] """


A = np.random.random([2,3]) # Or this is also equivalent
print(A)

'''
numpy.random.random like many of the other numpy.random methods accept shapes, i.e. N-tuples. So really the outside parenthesis represent calling the method numpy.random.random(), and the inside parenthesis are syntactic sugar for instantiating the tuple (3, 3) that is passed into the function.
'''

# Create Matrix (2,3) with random between 0 and 1 and INTEGER (i.e. NOT decimal)
B = np.random.randint(10, size=(3,2))
# print(B)
print(B.T)

# Dot product
print(np.dot(A, B))

# transpose
# print(np.dot(A, B).T)
