
`else` 语句块将在for循环正常完成之后被执行，如果遇到了`break`语句，else 就不会执行了。

```python
for i in range(3):
    print(i)
    if i % 2 == 0:
        break
else:
    print("end")
```