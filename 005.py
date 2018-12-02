"""
格式化字符串的N种方式
"""

name = "军哥"
# no1
print("hello %s" % name)

# no2
print("hello %(name)s" % {"name": name})

# no3
print("hello {}".format(name))

# no4
print("hello {name}".format(name=name))

# no5
print(f"hello {name}")

# no6
from string import Template

t = Template('hello $name')
print(t.substitute(name=name))
