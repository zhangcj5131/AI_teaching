'''
在函数嵌套(函数里面再定义函数)的前提下
内部函数使用了外部函数的变量(还包括外部函数的参数)
外部函数返回了内部函数
'''

# 外部函数
def config_name(name):
    # 内部函数
    def say_info(info):
        print(name + ": " + info)

    return say_info

tom = config_name("Tom")

tom("你好!")
tom("你好, 在吗?")

jerry = config_name("jerry")

jerry("不在, 不和你玩!")
