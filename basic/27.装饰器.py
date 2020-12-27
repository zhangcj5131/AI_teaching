'''

装饰器的功能特点:

不修改已有函数的源代码
不修改已有函数的调用方式
给已有函数增加额外的功能

闭包函数有且只有一个参数，必须是函数类型，这样定义的函数才是装饰器。
写代码要遵循开放封闭原则，它规定已经实现的功能代码不允许被修改，但可以被扩展。
'''

# 添加一个登录验证的功能
def check(fn):
    def inner():
        print("请先登录....")
        fn()
    return inner


# def comment():
#     print("发表评论")
#
# # 使用装饰器来装饰函数
# comment = check(comment)
# comment()

@check
def comment():
    print("发表评论")


comment()