https://towardsdatascience.com/a-beginners-guide-to-xgboost-87f5d4c30ed7

XGBoost is an open source library providing a high-performance implementation of gradient boosted decision trees. An underlying C++ codebase combined with a Python interface sitting on top makes for an extremely powerful yet easy to implement package.
The performance of XGBoost is no joke — it’s become the go-to library for winning many Kaggle competitions.

### Boosting Trees

With a regular machine learning model, like a decision tree, we’d simply train a single model on our dataset and use that for prediction. We might play around with the parameters for a bit or augment the data, but in the end we are still using a single model. Even if we build an ensemble, all of the models are trained and applied to our data separately.

Boosting, on the other hand, takes a more iterative approach. It’s still technically an ensemble technique in that many models are combined together to perform the final one, but takes a more clever approach.

Rather than training all of the models in isolation of one another, boosting trains models in succession, with each new model being trained to correct the errors made by the previous ones. Models are added sequentially until no further improvements can be made.

The advantage of this iterative approach is that the new models being added are focused on correcting the mistakes which were caused by other models. In a standard ensemble method where models are trained in isolation, all of the models might simply end up making the same mistakes!
Gradient Boosting specifically is an approach where new models are trained to predict the residuals (i.e errors) of prior models. I’ve outlined the approach in the diagram below.

#### `eta` parameter of the model

From our theory, Gradient Boosting involves creating and adding decision trees to an ensemble model sequentially. New trees are created to correct the residual errors in the predictions from the existing ensemble.
Due to the nature of an ensemble, i.e having several models put together to form what is essentially a very large complicated one, makes this technique prone to overfitting. The eta parameter gives us a chance to prevent this overfitting
The eta can be thought of more intuitively as a learning rate. Rather than simply adding the predictions of new trees to the ensemble with full weight, the eta will be multiplied by the residuals being adding to reduce their weight. This effectively reduces the complexity of the overall model.

### Training and Testing

We can finally train our model similar to how we do so with Scikit Learn:

```
model = xgb.train(param, D_train, steps)
```
