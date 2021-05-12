#### `np.c_` is a way of doing array concatenate - its NOT the same as concatenate() function

### It concats your first array into the last dimension (axis) of your last array in the function.

## All you have to do is add along second axis.

---

### Example-1

https://stackoverflow.com/a/51884244/1902852

Now checkout with arrays of shape of (3, 1)
In below both the input arrays has shape of (3,) But there isn't second axis. So we mentally add one. so shape of both array becomes (3,1).

```python

x = np.c_[np.array([1,2,3]), np.array([4,5,6])]

print(x)

# [[1 4]
#  [2 5]
#  [3 6]]

```

#### So following the rule of adding along second axis - Resultant shape would be (3, 1+1) which is (3,2). which is the shape of result -

```
[[1 4]
 [2 5]
 [3 6]]
```

---

### Example-2

Now checkout with arrays of shape of (2, 3) - In below both the input arrays has shape of (2, 3)

#### We know the c\_ function concatenates your first array into the **last dimension (axis)** of your last array in the function.

For example:

    # both are 2 dimensional array
    a = array([[1, 2, 3], [4, 5, 6]])
    b = array([[7, 8, 9], [10, 11, 12]])

Now, let's take a look at `np.c_(a, b)`:

**First, let's look at the shape:**

The shape of both a and b are `(2, 3)`. Concating a (2, 3) into the last axis of b (3), while keeping other axises unchanged (1) will become

    (2, 3 + 3) = (2, 6)

That's the new shape.

**Now, let's look at the result:**

In b, the 2 items in the last axis are:

    1st: [7, 8, 9]
    2nd: [10, 11, 12]

Adding a to it means:

    1st item: [1,2,3] + [7,8,9] = [1,2,3,7,8,9]
    2nd item: [4,5,6] + [10,11,12] = [4,5,6,10,11,12]

So, the result is

    [
      [1,2,3,7,8,9],
      [4,5,6,10,11,12]
    ]

It's shape is (2, 6)

---

### Example-3

#### Note the below array [1,2,3] has a diamension of 1

```python
y = np.array([1,2,3])
print(y.ndim)
# 1
```

---

### Example-4

```python
np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])]

# [[1 2 3 0 0 4 5 6]]
```

Calculate the shapes:

`np.array([[1,2,3]])` = `1,3`

`np.array([[4,5,6]])` = `1,3`

`0` so we can think of it as `[[0]]` = `1,1`

So result `1, 3+1+1+3` = `1,8`

## which is the shape of result : `array([[1, 2, 3, 0, 0, 4, 5, 6]])`
