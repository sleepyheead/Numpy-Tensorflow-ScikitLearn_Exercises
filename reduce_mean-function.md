#### First the primer on Linear Regressiion

The first step in TensorFlow training involves choosing an initial expression for the model. For linear regression, this decision is easy. The model
is a line whose equation is y mx b, where m is the line’s slope, and b is the y-intercept (the y-value when x equals 0). The goal of linear regression is to deter-mine m and b so that the resulting line best approximates (or fits) the set of points

The loss is also simple to compute. If the graph contains the point (x, y), the ­difference between the system and the model is

```
y - ( mx b )

```
