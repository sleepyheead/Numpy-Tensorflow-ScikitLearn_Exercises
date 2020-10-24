# https://stackoverflow.com/questions/23036866/scikit-learn-is-returning-coefficient-of-determination-r2-values-less-than-1


''' R² = 1 - RSS / TSS, where RSS is the residual sum of squares ∑(y - f(x))² and TSS is the total sum of squares ∑(y - mean(y))².

So, from the above formulae, for R² ≥ -1, it is required that RSS/TSS ≤ 2, but it's easy to construct a model and dataset for which this is not true: '''

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

x = np.arange(50, dtype=float)
# print('x is ', x) # for the first parameter of the above as 10
# [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

y = x

def f(x): return -100

rss = np.sum((y - f(x)) ** 2)
tss = np.sum((y - y.mean()) ** 2)

print ('rss is ', rss)
# rss is  109285.0

print('tss is ', tss)
# tss is  82.5

r_squared = 1 - rss/tss
print(r_squared)
