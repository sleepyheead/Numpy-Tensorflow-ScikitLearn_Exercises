```python
import numpy as np

data = np.arange(1,10).reshape(3,3)
# print(data)

# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

```

![](assets/2020-10-16-15-14-58.png)

```python
print(data.sum())
# 45

print(data.sum(axis=0))
# [12 15 18]

print(data.sum(axis=1))
# [ 6 15 24]
```

So if you are having problem in remembering the above, while executing aggregating functions on Numpy array - just remember that you are removing that dimension when you run mean or sum on that axis.

### axis=0 removes the row dimension

### axis=1 removes the column dimension
