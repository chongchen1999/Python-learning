def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')


# 下面的代码会输出什么呢？
foo() # goodbye, world!, it will be overwritten by the last foo()