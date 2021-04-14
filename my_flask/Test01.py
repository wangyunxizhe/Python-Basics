import string

# 函数作为传参的例子
def a_func(x):
    if isinstance(x, int):
        if 0 <= x <= len(string.ascii_letters):
            return string.ascii_letters[x]
        else:
            return "x 不是数字"


def b_func(l=None, func=None):
    for index, value in enumerate(l):
        print(index, '->', func(value))

    return None


b_func(l=[1, 3, 5, 'a', 'b', '_', 10], func=a_func)

