"""
with 操作文件对象
"""


def fun0():
    try:
        f_name = "002.py"
        f = open(f_name)
        print("".join(f.readlines()))
        f.close()
    except IOError:
        print("Could not read file:", f_name)


def fun1():
    with open("003.py") as f:
        print("".join(f.readlines()))


if __name__ == '__main__':
    fun0()
