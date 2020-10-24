import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


X = [[1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 2, 1, 1],
     [1, 3, 1, 1],
     [1, 4, 1, 1],
     [1, 2, 1, 1],
     [1, 3, 1, 1],
     [2, 4, 1, 1],
     [1, 1, 1, 1],
     [2, 1, 1, 1],
     [2, 4, 1, 1],
     [1, 5, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1]]


y = [
    [1],
    [1],
    [1],
    [3],
    [2],
    [1],
    [3],
    [2],
    [1],
    [1],
    [2],
    [1],
    [1],
    [1],
   ]


# Now split X and y to for training and test data set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

print(regression_model.score(X_test, y_test))
# -1.1817143658810325