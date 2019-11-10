比print更好的打印函数pprint


print 将打印的结果显示在一行，可读性差

```python
>>> print(locals())
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': {'a': 1}, 'b': {'b': 2}, 'c': {'a': 1, 'b': 2}}

```

pprint 对打印结果进行了格式化处理，可读性提高了很多

```python
import pprint

pprint.pprint(locals())
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'a': {'a': 1},
 'b': {'b': 2},
 'c': {'a': 1, 'b': 2},
}
```