![](assets/numpy-concatenate-axis-0.png)

---

![](assets/numpy-concatenate-axis-1.png)

---

![](assets/default-numpy-concatenate.png)

```python
x = np.concatenate(([
       [2, 5, 9],
       [4, 1, 3]],
       [
        [5, 8, 3],
        [4, 6, 1]]), axis=0)

print(x)

# [[2 5 9]
#  [4 1 3]
#  [5 8 3]
#  [4 6 1]]

```

---

```python

x = np.concatenate(([1,2,3], [4,5,6]), axis=0)
print(x)
# [1 2 3 4 5 6]
```
