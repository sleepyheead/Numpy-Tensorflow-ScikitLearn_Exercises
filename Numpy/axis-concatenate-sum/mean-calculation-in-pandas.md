```python
import numpy as np
import pandas as pd


df = pd.DataFrame([[10, 20, 30, 40], [2, 2, 2, 2], [3, 3, 3, 3]], columns=["col1", "col2", "col3", "col4"])
print(np.round(df.mean(axis=1), decimals=0))

# 0    25.0
# 1     2.0
# 2     3.0
# dtype: float64

```
