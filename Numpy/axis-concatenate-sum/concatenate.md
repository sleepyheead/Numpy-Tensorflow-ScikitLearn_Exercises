![](assets/numpy-concatenate-axis-0.png)
![](assets/numpy-concatenate-axis-1.png)
![](assets/default-numpy-concatenate.png)

---

`np.c_` is a way of doing array concatenate

```python
np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])]

# [[1 2 3 0 0 4 5 6]]
```

---

Now checkout arrays with shape of (2, 3)

```python
z = np.c_[np.array([1,2,3]), np.array([4,5,6])]
print(z)

# [[1 4]
#  [2 5]
#  [3 6]]
```

In bwlow both the input arrays has shape of (2, 3)

```python
a = np.c_[np.array([[1,2,3], [11, 22, 33]]), np.array([[4,5,6], [44, 55, 66]])]
print(a)

# [[ 1  2  3  4  5  6]
#  [11 22 33 44 55 66]]

```

---

#### Note the below array [1,2,3] has a diamension of 1

```python
y = np.array([1,2,3])
print(y.ndim)
# 1
```
