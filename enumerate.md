
普通写法获取列表元素的下标

```python
>>> furits = ["apple", "orange", "banala"]
>>> index  = 0
>>> for f in furits:
...     print(index, f)
...     index += 1
...
0 apple
1 orange
2 banala
```

pythonic 方法：用 `enumerate` 获取元素下标

```python

>>> for index, item in enumerate(furits):
...     print(index, item)
...
0 apple
1 orange
2 banala
>>>
```