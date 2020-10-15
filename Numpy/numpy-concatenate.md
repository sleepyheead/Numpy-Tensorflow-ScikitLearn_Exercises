![](assets/numpy-concatenate-axis-0.png)
![](assets/numpy-concatenate-axis-1.png)
![](assets/default-numpy-concatenate.png)

---

`np.c_` is another way of doing array concatenate

```python
np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])]

# [[1 2 3 0 0 4 5 6]]
```
