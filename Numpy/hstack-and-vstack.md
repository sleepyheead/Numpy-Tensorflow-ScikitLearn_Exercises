## hstack - 1

https://www.w3resource.com/numpy/manipulation/hstack.php

numpy.hstack() function is used to stack the sequence of input arrays horizontally (i.e. column wise) to make a single array.

#### Below is the one form that I have used in Donor Choose dataset AML Assignment - after vectorizing for all non-sparse features (price, sentiments), I will get arrays of the form - [[3], [5], [7]]

```py

import numpy as np

x = np.array([[3], [5], [7]])
y = np.array([[5], [7], [9]])
np.hstack((x,y))

>>> array([[3, 5],
           [5, 7],
           [7, 9]])

```

![Imgur](https://imgur.com/ypYNtUk.png)


#### hstack - 2 In the special case where the sequence is all 1D arrays, this just concatenates them into a longer 1D array:

```
import numpy as np

x = np.array((3,5,7))
y = np.array((5,7,9))
np.hstack((x,y))

array([3, 5, 7, 5, 7, 9])
```

![Imgur](https://imgur.com/pz9IIdw.png)

#### And similarly `scipy.sparse.hstack` concatenates the sparse tf-idf matrices (with the same number of rows) returned by TfidfVectorizer.fit_transform.