import numpy as np

"""
https://stackoverflow.com/questions/36300334/understanding-argmax

How argmax() function works in Numpy

### argmax is a function which gives the index of the greatest number in the given row or column and the row or column can be decided using axis attribute of argmax funcion.

### If we give axis=0 then the function will now try to find the maximum value along the rows of the matrix. And  give the index from rows. If the maximum value is in the 2-nd row (i.e. index of 1), then 1 will be returned.

### If we give axis=1 then it will give the index from column. If the maximum value is in the 3rd column, index 2 then that index number will be returned.



"""

A = np.matrix([[]])

A = np.matrix([[1, 2, 3, 33], [4, 5, 6, 66], [7, 8, 9, 99]])

print(np.argmax(A))
# 11, which is the position of 99

print(np.argmax(A[:, :]))
# 11, which is the position of 99

print(np.argmax(A[:1]))
# 3, which is the position of 33

print(np.argmax(A[:, 2]))
# 2, which is the position of 9

np.argmax(A[1:, 2])
# 1, which is the position of 9
""" A[1:, 2] it will first fetch the values from 1st row on wards and the only 2nd column value from those rows, then it will find the index of max value from into the resulted matrix. """


a = [[1, 2, 3], [4, 5, 6]]
print(np.argmax(a))
"""
# 5

the array is 2 dimensional, with shape (2,3). Since no axis parameter is specified in the function, the numpy library flattens the array to a 1 dimensional array and then returns the index of the maximum value. In this case the array is transformed to [[1,2,3,4,5,6]] and then returns the index of 6, which is 5.

"""

# When parameter is axis = 0 in argmax()

a = [[1, 2, 3], [4, 5, 6]]
print(np.argmax(a, axis=0))
# array([1, 1, 1])

""" The result here is a bit confusing at first.

#### First repeating the original rule -

### If we give axis=0 then the function will now try to find the maximum value along the rows of the matrix. And  give the index from rows. If the maximum value is in the 2-nd row (i.e. index of 1), then 1 will be returned.

### If we give axis=1 then it will give the index from column. If the maximum value is in the 3rd column, index 2 then that index number will be returned.

Since the axis is defined to be 0, the function will now try to find the maximum value along the rows of the matrix.

The maximum value, 6, is in the second row of the matrix. The index of the second row is 1. According to the documentation https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.argmax.html the dimension specified in the axis parameter will be removed. Since the shape of the original matrix was (2,3) and axis specified as 0, the returned matrix will have a shape of(3,) instead, since the 2 in the original shape(2,3) is removed.The row in which the maximum value was found is now repeated for the same number of elements as the columns in the original matrix i.e. 3.


"""

# When parameter is axis = 1 in argmax()

a = [[1, 2, 3], [4, 5, 6]]
print(np.argmax(a, axis=1))
# array([2, 2])

""" Same concept as above but now index of the column is returned at which the maximum value is available. In this example the maximum value 6 is in the 3rd column, index 2. The column of the original matrix with shape (2,3) will be removed, transforming to (2,) and so the return array will display two elements, each showing the index of the column in which the maximum value was found. """