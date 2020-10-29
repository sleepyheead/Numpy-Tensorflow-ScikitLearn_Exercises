# https://stackoverflow.com/questions/51691259/how-prediction-and-score-works-in-scikit-learn
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

''' Explanation of the negative R-Squared value

From Docs -

"score(X, y, sample_weight=None)[source]
Return the coefficient of determination R^2 of the prediction.

The coefficient R^2 is defined as (1 - u/v), where u is the residual sum of squares ((y_true - y_pred) ** 2).sum() and v is the total sum of squares ((y_true - y_true.mean()) ** 2).sum(). The best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse). A constant model that always predicts the expected value of y, disregarding the input features, would get a R^2 score of 0.0."

Now, the negative R-squared means - your model has to be so bad that predicting a simple average every time would be better. Usually this means that your model is over fitting.


What can be done in this situation - The important question now is whether this is due to the fact that linear models just do not find anything in your data, or to something else that may be fixed in the preprocessing of your data.

We can try scaling our columns to have mean 0 and variance 1.

We can do this using sklearn.preprocessing.StandardScaler. As a matter of fact, we should create a new estimator by concatenating a StandardScaler and the LinearRegression into a pipeline using sklearn.pipeline.Pipeline. Next you may want to try Ridge regression.


Also remember that the syntax of the score function is as below

(And this is a common bug - that you should double check is that you are passing in parameters correctly:)

r2_score(y_true, y_pred) # Correct!
r2_score(y_pred, y_true) # Incorrect!!!!



'''