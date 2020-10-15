#### `np.c_` is a way of doing array concatenate - its NOT the same as concatenate() function

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

```python
a = np.c_[np.array([[1,2,3], [11, 22, 33]]), np.array([[4,5,6], [44, 55, 66]])]
print(a)

# [[ 1  2  3  4  5  6]
#  [11 22 33 44 55 66]]

```

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
