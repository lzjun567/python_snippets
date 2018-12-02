"""
多值判断
"""


def fun1(a):
    if a == 1 or a == 3 or a == 5:
        print('pass')

    if a in (1, 3, 5):
        print('pass')


def fun2(a, b, c):
    if a != 0 and b != 0 and c != 0:
        print("pass")

    if all([a, b, c]):
        print('pass')
