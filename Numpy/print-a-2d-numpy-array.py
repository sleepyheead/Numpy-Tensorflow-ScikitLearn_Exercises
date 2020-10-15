import numpy as np

b = np.array([[0,0,0],[1,2,3],[2,2,2],[9,9,9]])
# 2

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in b]))

# 0   0   0
# 1   2   3
# 2   2   2
# 9   9   9