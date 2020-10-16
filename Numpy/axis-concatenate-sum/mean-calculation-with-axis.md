## What may make more sense from a pure programming perspective of action on array elements :

### Axis 0 will act on all the ROWS in each COLUMN

### Axis 1 will act on all the COLUMNS in each ROW

### So a `mean` on axis 0 will be the mean of all the rows in each column, and a mean on axis 1 will be a mean of all the columns in each row.

---

When applying certain Numpy functions like np.mean(), we can specify what axis we want to calculate the values across.

For axis=0, this means that we apply a function along each “column”, or all values that occur vertically.

For axis=1, this means that we apply a function along each “row”, or all values horizontally.

```python
values = np.array([
[10, 20, 30, 40],
[50, 60, 70, 80],
])

# Axis=0
# along each "column"
print np.mean(values, axis=0)
# [30, 40, 50, 60]

# Axis=1
# along each "row"
print np.mean(values, axis=1)
# [25, 65]

```
